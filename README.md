![django](https://github.com/descope-sample-apps/django-sample-app/assets/59460685/866222d2-437e-4f46-8d92-243ff9bd2d1c)

# Descope Django Sample App

Learn how to integrate Descope authentication in Django by building a Quillbot clone. 

## ⚙️ Setup 

1. Clone the repository:

```
git clone https://github.com/descope-sample-apps/django-sample-app.git
```

2. Install dependencies:

```
make setup
```

3. Environment variables

```
DESCOPE_PROJECT_ID=YOUR_DESCOPE_PROJECT_ID
```

- ```DESCOPE_PROJECT_ID```: can be found in your Descope's account under the [Project page](https://app.descope.com/settings/project)

## 🔮 Running the Application 

To start the application, run:

```
python3 manage.py runserver
```

## 🥷 Roles  

Sign up for Descope and create admin roles [here](https://app.descope.com/authorization).

Create two roles in Descope, that will be mapped to Django permissions.
- is_staff
- is_superuser

Map these roles to any user you would like to make a staff or superuser in your Django app.

## ⚠️ Issue Reporting

For any issues or suggestions, feel free to open an issue in the GitHub repository.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
