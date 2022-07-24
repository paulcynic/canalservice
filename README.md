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

Stop and remove the containers
```
$ docker-compose down
```

## Link to googleSheetsAPI
```
https://docs.google.com/spreadsheets/d/1jupyBDOGP8xpNYsdDhtyucU_zm3bh6NMyK_vZRTabYQ/edit?usp=sharing
```
## Automatization with Cron job which make api request every minute 
```
curl http://backend:8000/api/orders/
```
## ISSUE

GoogleAPI doesn't work from docker container.
I can run app on my local PC and it's OK.
But inside container I get eternal loading.
