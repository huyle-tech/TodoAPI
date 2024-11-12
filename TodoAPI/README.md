# TodoAPI

This is a Django Rest API application for managing a basic Todo list wih CRUD functionality and token authentication.

## Features

•  Create, list, retrieve, update and delete todo items.

•  Token-based authentication for API access.

## Requirements

•  Python 3.8+

•  Django 3.2+

•  Django Rest Framework (DRF) 3.12+

•  Django Rest Framework Token Authentication


## Installation

1. **Clone the repository**
```bash
git clone https://github.com/huyle-tech/TodoAPI.git
cd TodoAPI
```

2. **Create and activate a virtual environment**

* On Window:
```bash
python - m venv venv
venv\Scripts\activate
```

* On macOS/Linux:
```bash
python - m venv venv
source venv/bin/activate
```

3. **Install the required packages**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

## Running Tests
```bash
python manage.py test
```

## How to get Token

To authenticate with API, user need to obtain a token. User can get the token by following these steps:

### Using cURL

```bash
curl -X POST -d "username=<your-username>&password=<your-password>" http://127.0.0.1.8000/api/token/
```

### Using Postman

• Send a `POST` request to URL `/api/token/` with the `username` and `password` data to get the token.


## API Endpoints

| Method | Endpoint | Description |
|--------|------------------------|---------------------------------|
| GET    | `/api/todos/`          | List all todo items             |
| POST   | `/api/todos/`          | Create a new todo item          | 
| GET    | `/api/todos/<id>/`     | Retrieve a specific todo item   | 
| PUT    | `/api/todos/<id>/`     | Update a specific todo item     | 
| PATCH  | `/api/todos/<id>/`     | Partially update a todo item    | 
| DELETE | `/api/todos/<id>/`     | Delete a specific todo item     |

## Project Structure

```markdown

TodoAPI/
    |── TodoAPI/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py 
    ├── todos/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    ├── .gitignore
    ├── db.sqlite3
    ├── manage.py
    ├── README.md
    └── requirements.txt
```