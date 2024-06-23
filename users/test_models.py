from django.test import TestCase
from django.contrib.auth import get_user_model
from psycopg2 import IntegrityError
from recipe.models import Recipe, RecipeCategory
from .models import CustomUser as User , Profile

class UserModelTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email='test.zeph1@example.com', username='testuser.zeph2', password='testpassword')
        
    def test_user_creation(self):
        self.assertEqual(str(self.user), self.user.email)
    


class ProfileModelTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(email='test.zeph@example.com', username='testuser.zeph', password='testpassword')
    
    def test_profile_creation(self):
        profile = Profile.objects.create(user=self.user, bio='Test Bio')
        self.assertEqual(str(profile), self.user.username)
    
    def test_profile_bookmarks(self):
        recipe_category = RecipeCategory.objects.create(name='Test Category')
        recipe = Recipe.objects.create(
            author=self.user,
            category=recipe_category,
            title='Test Recipe',
            desc='Test Description',
            cook_time='00:30:00',
            ingredients='Ingredient 1, Ingredient 2',
            procedure='Step 1, Step 2'
        )
        profile = Profile.objects.create(user=self.user, bio='Test Bio')
        profile.bookmarks.add(recipe)
        self.assertEqual(profile.bookmarks.count(), 1)