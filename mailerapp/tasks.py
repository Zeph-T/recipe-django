from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from recipe.models import Recipe
from users.models import CustomUser

@shared_task(bind=True)
def retrieve_author_likes_and_send_email(self):
    authors = CustomUser.objects.all()
    for author in authors:
        author_recipes = Recipe.objects.filter(author=author)
        recipe_likes = {}
        total_likes = 0
        if len(author_recipes) == 0:
            continue
        for recipe in author_recipes:
            recipe_likes[recipe.title] = recipe.get_total_number_of_likes()
            total_likes += recipe_likes[recipe.title]
        print(f'Sending Email for {author.email}')
        send_email_notification(author.email,recipe_likes)

def send_email_notification(author_email,recipe_likes):
    print(f'recipe content : {recipe_likes}')
    email_subject = 'Daily Likes Summary'
    email_message = f'Author : {author_email} \n'
    for recipe_name, likes in recipe_likes.items():
        email_message += f'Recipe Name : {recipe_name} Total Likes: {likes}\n'
        response = send_mail(email_subject, email_message, EMAIL_HOST_USER , [author_email])
        print(f'Send Email Response {response}')