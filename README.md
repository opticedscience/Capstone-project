# Little Lemon Restaurant

## Description

The Little Lemon Restaurant is a web application built using Django, a popular Python web framework. This project serves as a capstone project for a meta backend developer. The main purpose of the application is to provide customers with an online platform to book a table, view the menu, and access other relevant information about the restaurant.

## Key Features

- User Registration and Authentication: Users can create an account, log in, and manage their profile.
- Table Booking: Users can book a table for a specific date and time.
- Menu: The application displays a list of menu items with their prices and inventory.
- Admin Panel: The admin panel allows administrators to manage bookings, menu items, and other aspects of the application.

## Technologies Used

- Django: The web framework used to build the application.
- Python: The programming language used for development.
- MySQL: The database used to store data.
- REST Framework: The application uses Django REST Framework for building APIs.
- Djoser: The application uses Djoser for user registration and authentication.

## Getting Started

To run the Little Lemon Restaurant application locally, follow these steps:

1. Clone the repository.
2. Install the required dependencies using pip.
3. Set up the database configuration in the `settings.py` file.
4. Run the necessary database migrations.
5. Start the development server.

## Directory Structure

- littlelemon: The root directory of the project.
  - littlelemon: The Django project configuration.
    - settings.py: The project settings.
    - urls.py: The project URLs.
    - wsgi.py: The WSGI configuration.
    - asgi.py: The ASGI configuration.
  - templates: The directory for HTML templates.
  - static: The directory for static files.
  - restaurant: The application directory.
    - models.py: The application models.
    - views.py: The application views.
    - migrations: The directory for database migrations.
    - urls.py: The application URLs.
    - admin.py: The admin configuration.
    - serializers.py: The application serializers.
    - tests.py: The application tests.
    - static/css: The directory for CSS files.
    - static/img: The directory for images.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or further information, please contact us at [info@littlelemon.com](mailto:info@littlelemon.com).