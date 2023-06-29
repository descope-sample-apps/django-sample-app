# Descope Django Sample App

## Setup ⚙️

### Dependencies 

Run the following commands:

```
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
```

### Descope

Create a .env file in the root project directory
```
DESCOPE_PROJECT_ID=YOUR_DESCOPE_PROJECT_ID
```

### Run the server!

Run the following command:

```
python3 manage.py runserver
```

## Roles ⚙️

Sign up for Descope and set admin roles.

Create two roles in Descope, that will be mapped to Django permissions.
- is_staff
- is_superuser

Map these roles to any user you would like to make a staff or superuser in your Django app.

<br />

Happy Coding ☕