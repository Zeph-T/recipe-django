from django.test import TestCase
from recipe.models import Recipe, RecipeLike, RecipeCategory
from users.models import CustomUser

class RecipeModelTestCase(TestCase):
    def setUp(self):
        self.category = RecipeCategory.objects.create(name="Breakfast")
        self.author = CustomUser.objects.create(username='testuser', password='12345', email='test@example.com')

    def test_create_recipe(self):
        recipe = Recipe.objects.create(author=self.author, category=self.category, title='Pancakes', desc='Delicious breakfast', cook_time='00:30:00', ingredients='eggs, flour, milk', procedure='1. Mix all ingredients and cook on a pan')
        self.assertEqual(Recipe.objects.count(), 1)

class RecipeLikeModelTestCase(TestCase):
    def setUp(self):
        self.author = CustomUser.objects.create(username='testuser2', password='12345', email='test2@example.com')
        self.category = RecipeCategory.objects.create(name = 'category')
        self.recipe = Recipe.objects.create(author=self.author, category = self.category , title='Example Recipe', desc='Example Description', cook_time='01:00:00', ingredients='example ingredients', procedure='example procedure')

    def test_create_recipe_like(self):
        like = RecipeLike.objects.create(user=self.author, recipe=self.recipe)
        self.assertEqual(RecipeLike.objects.count(), 1)