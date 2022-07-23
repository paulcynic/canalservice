## Compose sample application
### Django application in dev mode

Project structure:
```
.
├── docker-compose.yml
├── app
    ├── Dockerfile
    ├── requirements.txt
    └── manage.py

```

[_docker-compose.yml_](docker-compose.yml)
```
services: 
  web: 
    build: app 
    ports: 
      - '8000:8000'
```

## Deploy with docker-compose

```
$ docker-compose up -d
Creating network "django_default" with the default driver
Building web
Step 1/6 : FROM python:3.10
...
...
Status: Downloaded newer image for python:3.10
Creating django_web_1 ... done

```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
3adaea94142d        django_web          "python3 manage.py r…"   About a minute ago   Up About a minute   0.0.0.0:8000->8000/tcp   django_web_1
```

## Make Migrations

```
docker-compose exec backend python3 manage.py makemigrations
```

## Migrate

```
docker-compose exec backend python3 manage.py migrate
```
If everything is "OK", then

## Open app:

After the application starts, navigate to `http://localhost:8000` in your web browser:

## After usage:

Stop and remove the containers
```
$ docker-compose down
```
