from django.test import TestCase
from unittest.mock import patch
from users.models import CustomUser
from recipe.models import Recipe, RecipeCategory
from mailerapp.tasks import retrieve_author_likes_and_send_email

class RetrieveAuthorLikesAndSendEmailTest(TestCase):
    @patch('mailerapp.tasks.send_email_notification')
    def test_retrieve_author_likes_and_send_email(self, mock_send_email):
        # Setup test data
        author1 = CustomUser.objects.create_user(username='testuser1', password='12345', email='test1@example.com')
        category = RecipeCategory.objects.create(name='Category')
        recipe1 = Recipe.objects.create(author=author1, category=category, title='Recipe 1', desc='Example Description', cook_time='01:00:00', ingredients='example ingredients', procedure='example procedure')
        recipe2 = Recipe.objects.create(author=author1, category=category, title='Recipe 2', desc='Example Description', cook_time='01:00:00', ingredients='example ingredients', procedure='example procedure')

        # Mock get_total_number_of_likes method
        with patch.object(Recipe, 'get_total_number_of_likes', side_effect=[10, 5]):
            retrieve_author_likes_and_send_email()

        # Get actual calls to send_email_notification
        calls = mock_send_email.call_args_list

        # Check if send_email_notification was called with correct arguments
        self.assertEqual(len(calls), 1)