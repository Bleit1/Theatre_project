# Database Setup and Usage

Follow these commands to set up and work with the database:

1. **Create the `.env` file**

    Build and run Docker containers

    Use Docker Compose to build and run the containers in detached mode:
   
    ```sh
    docker-compose up --build -d
    ```

2. Verify that the PostgreSQL container is running

    Check the status of the containers:
    ```sh
   docker-compose ps
    ```

    You should see something like:
```sh 
NAME               IMAGE              COMMAND                  SERVICE   CREATED          STATUS                   PORTS
postgres-theatre   postgres:14.17     "docker-entrypoint.s…"   db        12 minutes ago   Up 7 minutes (healthy)   0.0.0.0:5432->5432/tcp
theatre-backend    theatre_project-web "sh -c 'python manage.…" web       12 minutes ago   Up 7 minutes             0.0.0.0:8000->8000/tcp

```

3. Connect to the PostgreSQL database

    Use a local psql client if it installed
    ```sh
    psql -h localhost -U theatre_user -d theatre_db
    ```


Use Docker to run psql if it not istalled
    ```sh
    docker run -it --rm postgres:14 psql -h localhost -U theatre_user -d theatre_db
    ```


4. Run Django migrations
    To apply migrations inside the running container:
    ```sh
    docker-compose exec web python manage.py migrate
   ```
