# Django Blog

A fully functional blog web application built with Django and PostgreSQL.

## Features

- User authentication (login, logout, password reset)
- Create, read, update, and delete blog posts
- Comment system
- User profiles
- Pagination
- Responsive design with Bootstrap

## Requirements

- Python 3.8+
- Django 5.1+
- PostgreSQL 12+
- psycopg2-binary

## Installation

1. Clone the repository:
```
git clone https://github.com/Einzigart/TestDjangoBlog.git
cd django-blog
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:
```
pip install -r requirements.txt
```

4. Configure PostgreSQL:
   - Create a database named `blog_db`
   - Update the database settings in `blog_project/settings.py` if needed

5. Apply migrations:
```
python manage.py migrate
```

6. Create a superuser:
```
python manage.py createsuperuser
```

7. Run the development server:
```
python manage.py runserver
```

8. Access the application at http://127.0.0.1:8000/

## Usage

- Visit the admin interface at http://127.0.0.1:8000/admin/ to manage users, posts, and comments
- Create new posts from the web interface after logging in
- View posts by specific users
- Add comments to posts
- Update or delete your own posts and comments

## License

This project is licensed under the MIT License - see the LICENSE file for details. 