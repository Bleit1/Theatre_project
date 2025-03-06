# Theatre Project
![изображение](https://github.com/user-attachments/assets/f3cf71bb-a021-4d6b-a34d-27fff4c88b62)

Theatre Project is a Django application for managing theatrical productions, including plays, performances, actors, genres, and reservations. It provides a REST API for integration with a frontend and uses Django’s admin panel for content management.

This project is containerized using Docker and Docker Compose, and it uses PostgreSQL as its database.

---

## Features

- **Theatrical Data Management:** Models for actors, genres, plays, performances, and reservations.
- **REST API:** Built with Django REST Framework.
- **API Documentation:** Provided by drf-spectacular.
- **Containerization:** Dockerfile and docker-compose.yml simplify deployment and testing.
- **Custom User Model:** Defined in the `user` app and configured via `AUTH_USER_MODEL`.

---

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Git

---

## Installation and Running

### 1. Clone the Repository

   ```bash
   git clone https://github.com/Bleit1/Theatre_project.git
   cd Theatre_project
   ```

2. Create .env file

3. Start Docker Containers
Build and run the containers in detached mode:
   ```sh 
   docker-compose up --build -d
   ```

4. Apply Database Migrations
   ```sh 
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```
   if You don`t have enough permissions, use this:
   ```sh 
   docker-compose exec --user root web python manage.py makemigrations
   docker-compose exec --user root web python manage.py migrate
   ```

5. Create a superuser
   if you need access to admin panel, use this:
   ```sh
   docker-compose exec web python manage.py createsuperuser
   ```

6. Access to Application

   Admin Panel: http://localhost:8000/admin/
   API Endpoints: http://localhost:8000/api/

Development and Testing

   Run tests:
      ```sh
      docker-compose exec web python manage.py test
      ```
