# Recipe API Documentation

- This Django REST API project allows users to interact with recipes and manage their profiles. The project includes user authentication, user profile management, recipe creation, and bookmark functionality.
- The coverage report is generated and saved in the `coverage.txt` file at the root level.
- This app also comes with a celery beat configuration that emails all the authors about the likes received in their recipes every day. You can find the app under `mailerapp` folder.
- The app is deployed in an EC2 Instance at `http://ec2-3-85-102-94.compute-1.amazonaws.com`

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

## Some Endpoints

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
