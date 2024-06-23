# Recipe API Documentation

This is a Django REST API project that allows users to interact with recipes and manage their profiles. The project includes user authentication, user profile management, recipe creation, and bookmark functionality.
The coverage report is generated and saved it in coverage.txt file in the root level

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Zeph-T/recipe-api.git
    cd recipe-api
    ```

2. Create a `.env` file in the root directory and add the necessary environment variables.

3. Start the application using Docker Compose:
    ```bash
    docker-compose up -d
    ```


5. The API should now be accessible at `http://localhost:80/`.

## Endpoints

- User Registration: `POST /api/user/register/`
- User Login: `POST /api/user/login/`
- Token Refresh: `POST /api/user/token/refresh/`
- User Logout: `POST /api/user/logout/`
- Get, Update User Info: `GET, PUT /api/user/`
- Get, Update User Profile: `GET, PUT /api/user/profile/`
- Get, Update User Avatar: `GET, PUT /api/user/profile/avatar/`
- Get, Add, Delete User Bookmarks: `GET, POST, DELETE /api/user/profile/<user_id>/bookmarks/`
- Change Password: `PUT /api/user/password/change/`

## Test cases

The project includes test cases for the following components:
- User models and views
- Profile models and views
- User authentication views
- Recipe models and views
- URLs for user endpoints
