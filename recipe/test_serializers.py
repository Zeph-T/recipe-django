from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeCategory, RecipeLike
from .serializers import RecipeSerializer, RecipeCategorySerializer, RecipeLikeSerializer

User = get_user_model()

class RecipeCategorySerializerTest(TestCase):
    def test_recipe_category_serializer(self):
        category_data = {'name': 'Desserts'}
        serializer = RecipeCategorySerializer(data=category_data)
        self.assertTrue(serializer.is_valid())

class RecipeSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', username='test_user', password='testpass')

    def test_recipe_serializer(self):
        category = RecipeCategory.objects.create(name='Desserts')
        recipe_data = {
            'category': {
                'id': category.id,
                'name': category.name,
            },
            'author': self.user.id,
            'title': 'Chocolate Cake',
            'desc': 'Delicious chocolate cake recipe',
            'cook_time': '00:30:00',
            'ingredients': 'Flour, cocoa powder, sugar, eggs',
            'procedure': 'Mix ingredients, bake in oven, enjoy!',
            'picture' : 'temp.jpg'
        }
        serializer = RecipeSerializer(data=recipe_data)
        is_valid = serializer.is_valid() 
        if not is_valid:
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())

class RecipeLikeSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', username='test_user', password='testpass')
        self.category = RecipeCategory.objects.create(name='Desserts')
        self.recipe = Recipe.objects.create(
            author=self.user,
            category=self.category,
            picture='cake.jpg',
            title='Chocolate Cake',
            desc='Delicious chocolate cake recipe',
            cook_time='00:30:00',
            ingredients='Flour, cocoa powder, sugar, eggs',
            procedure='Mix ingredients, bake in oven, enjoy!'
        )

    def test_recipe_like_serializer(self):
        like_data = {
            'user': self.user.id,
            'recipe': self.recipe.id
        }
        serializer = RecipeLikeSerializer(data=like_data)
        self.assertTrue(serializer.is_valid())