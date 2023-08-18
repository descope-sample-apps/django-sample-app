# Descope Django Sample App

Learn how to integrate Descope authentication in Django by building a Quillbot clone. 

## Setup ⚙️

1. Dependencies 
Run the following command to install dependencies:
```
make setup
```

2. Environment variables
Create a .env file in the root project directory
```
DESCOPE_PROJECT_ID=YOUR_DESCOPE_PROJECT_ID
```

3. Run the server
Start the app with the following command:
```
python3 manage.py runserver
```

## Roles 🥷

Sign up for Descope and set admin roles.

Create two roles in Descope, that will be mapped to Django permissions.
- is_staff
- is_superuser

Map these roles to any user you would like to make a staff or superuser in your Django app.
