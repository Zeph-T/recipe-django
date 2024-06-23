from rest_framework.test import APITestCase
from rest_framework import status
from recipe.models import Recipe, RecipeCategory, RecipeLike
from recipe.serializers import RecipeSerializer
from users.models import CustomUser as User

class RecipeListAPIViewTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')

        # Create test recipe categories
        self.category1 = RecipeCategory.objects.create(name='Category 1')
        self.category2 = RecipeCategory.objects.create(name='Category 2')

        # Create test recipes
        self.recipe1 = Recipe.objects.create(
            title='Recipe 1', desc='Description 1', cook_time='01:00:00', author=self.user, category=self.category1
        )
        self.recipe2 = Recipe.objects.create(
            title='Recipe 2', desc='Description 2', cook_time='00:30:00', author=self.user, category=self.category2
        )

    def test_get_recipe_list(self):
        url = '/api/recipe/'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = RecipeSerializer([self.recipe1, self.recipe2], many=True).data
        self.assertEqual(len(serializer_data) , len(response.data))


class RecipeCreateAPIViewTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')
        self.category = RecipeCategory.objects.create(name='New Category')
    def test_create_recipe(self):
        url = '/api/recipe/create/'
        self.client.force_authenticate(user=self.user)

        data = {
            "category": {
                "name": "New Category"
            },
            "picture": "string",
            "title": "New Recipe",
            "desc": "string",
            "cook_time": "12:00",
            "ingredients": "string",
            "procedure": "string"
        }


        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Recipe.objects.get().title, 'New Recipe')


class RecipeAPIViewTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')
        self.category = RecipeCategory.objects.create(name='Category 1')
        # Create a test recipe
        self.recipe = Recipe.objects.create(
            title='Test Recipe', category = self.category , desc='Test Description', cook_time='01:00:00', author=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_get_recipe(self):
        url = f'/api/recipe/{self.recipe.id}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Recipe')

    def test_update_recipe(self):
        url = f'/api/recipe/{self.recipe.id}/'

        data = {
            "category": {
                "name": "Category Updated"
            },
            "picture": "string",
            "title": "Test Recipe",
            "desc": "Test Description",
            "cook_time": "01:00:00",
            "ingredients": "test",
            "procedure": "test"
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Recipe.objects.get(id=self.recipe.id).category.name, 'Category Updated')
        
    def test_patch_recipe(self):
        url = f'/api/recipe/{self.recipe.id}/'

        data = {
            "title": "Updated Recipe",
            "desc": "Updated Description",
            "cook_time": "01:30:00",
        }

        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Recipe.objects.get(id=self.recipe.id).title, 'Updated Recipe')

    def test_delete_recipe(self):
        url = f'/api/recipe/{self.recipe.id}/'

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Recipe.objects.filter(id=self.recipe.id).exists())


class RecipeLikeAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')
        self.category = RecipeCategory.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(title='Test Recipe', category=self.category, desc='Test Description', cook_time='01:00:00', author=self.user)

    def test_like_recipe(self):
        url = f'/api/recipe/{self.recipe.pk}/like/'
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 201)  # Ensure this matches your expected status code for successful like

    def test_dislike_recipe(self):
        url = f'/api/recipe/{self.recipe.pk}/like/'
        self.client.force_authenticate(user=self.user)
        like = RecipeLike.objects.create(user=self.user, recipe=self.recipe)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)  # Ensure this matches your expected status code for successful dislike