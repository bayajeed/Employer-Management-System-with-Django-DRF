# Employer Management System

A complete Employer Management System with both API and web interface.

## Features

- Custom user authentication with email/password
- JWT token-based authentication for API
- Session-based authentication for web interface
- CRUD operations for employers
- User can only access their own employers

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`

## API Endpoints

### Authentication
- POST `/api/auth/signup/` - Register a new user
- POST `/api/auth/login/` - Login and get JWT tokens
- POST `/api/auth/logout/` - Logout (blacklist refresh token)
- GET `/api/auth/profile/` - Get logged-in user's profile

### Employers
- POST `/api/employers/` - Create a new employer
- GET `/api/employers/` - List all employers for the logged-in user
- GET `/api/employers/<id>/` - Retrieve a specific employer
- PUT `/api/employers/<id>/` - Update a specific employer
- DELETE `/api/employers/<id>/` - Delete a specific employer

## Web Interface

- `/login/` - Login page
- `/signup/` - User registration
- `/profile/` - User profile
- `/employers/` - List of employers
- `/employers/create/` - Create new employer
- `/employers/<id>/` - Employer details
- `/employers/<id>/update/` - Update employer
- `/employers/<id>/delete/` - Delete employer

## Testing

### API Testing
Use tools like Postman or curl to test the API endpoints. Include the JWT token in the Authorization header: