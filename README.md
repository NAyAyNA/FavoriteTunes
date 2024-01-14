## Installation and Walkthrough 

1. Clone the repository:
git clone https://github.com/NAyAyNA/FavoriteTunes.git
2. Change into the project directory:
cd FavoriteTunes
3. Install dependencies:
pip install -r requirements.txt
5. Apply database migrations:
python manage.py migrate
7. Create a superuser for the Django admin. Follow the prompts to create an admin:
   python manage.py createsuperuser
9. Run the development server:
   python manage.py runserver


Django Admin
Access the Django admin interface: http://localhost:8000/admin/
Log in using the superuser credentials created during installation.
Manage artists and songs through the admin interface.
