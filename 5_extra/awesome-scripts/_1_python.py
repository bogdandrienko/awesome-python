def setup_lang_and_ide():
    """
    # TODO update system repositories and dependencies
    sudo apt-get update -y && sudo apt update -y
    sudo apt-get upgrade -y && sudo apt upgrade -y

    # TODO install lang
    sudo apt-get install -y python3-dev python3-pip python3-venv

    # TODO install ide
    sudo snap install pycharm-professional --classic
    sudo snap install code --classic
    """

def project():
    """
    # TODO create new project
    cd ~/Downloads
    mkdir python_app && python_app
    cd python_app
    touch main.py
    """
    pass

def web():
    """
    pip3 install --upgrade pip --user
    python3 -m pip3 install --upgrade pip

    cd ~/Downloads
    mkdir django-rest-api && cd django-rest-api
    python3 -m venv env
    source env/bin/activate

    pip install --upgrade pip --user
    python -m pip install --upgrade pip

    pip install wheel
    pip install django django-environ django-grappelli gunicorn psycopg2-binary pillow
    pip install djangorestframework djangorestframework-simplejwt django-cors-headers celery redis
    pip install -r requirements.txt
    pip freeze > requirements.txt

    django-admin startproject django_settings .
    django-admin startapp django_app

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser --username admin --email bogdandrienko@gmail.com

    python manage.py collectstatic --noinput
    python manage.py createcachetable
    python manage.py check --database default

    python manage.py runserver 0.0.0.0:8000
    gunicorn --bind 0.0.0.0:8000 django_settings.wsgi
    """
    pass

def pip_ubuntu_windows():
    """
    # todo linux
    cd ~/Downloads
    pip3 install --upgrade pip --user

    python3 -m venv env
    call env/scripts/activate
    source env/bin/activate
    pip install --upgrade pip --user

    pip install lxml
    # todo linux

    # todo windows
    cd ~/Downloads
    mkdir web && cd web
    python.exe -m pip install --upgrade pip
    pip install env

    python -m venv env
    call .\env\Scripts\activate.bat
    python.exe -m pip install --upgrade pip

    pip install lxml
    # todo windows
    """
    pass

# TODO WEB #############################################################################################################

def gunicorn_ubuntu_python_django():
    """
    sudo nano /etc/systemd/system/gunicorn.socket
    <file>
    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/run/gunicorn.sock

    [Install]
    WantedBy=sockets.target
    </file>


    sudo nano /etc/systemd/system/gunicorn.service
    <file>
    [Unit]
    Description=Gunicorn for the Django example project
    Requires=gunicorn.socket
    After=network.target

    [Service]
    Type=notify

    User=bogdan
    Group=www-data

    RuntimeDirectory=gunicorn
    WorkingDirectory=/home/bogdan/web
    ExecStart=/home/bogdan/web/env/bin/gunicorn --workers 5 --bind unix:/run/gunicorn.sock backend.wsgi:application
    ExecReload=/bin/kill -s HUP $MAINPID
    KillMode=mixed
    TimeoutStopSec=5
    PrivateTmp=true

    [Install]
    WantedBy=multi-user.target
    </file>
    sudo systemctl daemon-reload
    sudo systemctl start gunicorn
    sudo systemctl enable --now gunicorn.service
    sudo systemctl daemon-reload
    sudo systemctl restart gunicorn
    sudo systemctl status gunicorn.service
    #sudo systemctl disable gunicorn
    #sudo systemctl stop gunicorn
    """
    pass

def nginx_ubuntu_gunicorn_python_django():
    """
    sudo usermod -aG user www-data

    sudo nano /etc/nginx/sites-available/web-km-kz-http.conf
    <file>
    server {
    listen 80;
    listen [::]:80;

    server_name web.km.kz www.web.km.kz;

    root /home/bogdan/web;

    location /.well-known/acme-challenge/ {}

    location /favicon.ico {
        alias /home/bogdan/web/static/logo.png;

        access_log off; log_not_found off;

        expires max;
    }

    location /robots.txt {
        alias /home/bogdan/web/static/robots.txt;

        access_log off; log_not_found off;

        expires max;
    }

    location /static/ {
        alias /home/bogdan/web/static/;

        expires max;
    }

    location /media/ {
        alias /home/bogdan/web/static/media/;

        expires max;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_buffering off;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
    }
    </file>

    sudo ln -s /etc/nginx/sites-available/web-km-kz-http.conf /etc/nginx/sites-enabled/web-km-kz-http.conf
    sudo service nginx start
    sudo systemctl status nginx.service
    sudo ufw allow 'Nginx Full'
    sudo systemctl reload nginx.service

    sudo mv /etc/nginx/sites-available/web-km-kz-http.conf /etc/nginx/sites-available/web.km.kz-https.conf
    sudo nano /etc/nginx/sites-available/web-km-kz-http.conf
    <file>
    server {
    listen 80;
    listen [::]:80;

    server_name web.km.kz www.web.km.kz;

    root /home/bogdan/web;

    location /.well-known/acme-challenge/ {}

    location / {
        return 301 https://$server_name$request_uri;
    }
    }
    </file>

    sudo certbot certonly --webroot -w /home/bogdan/web -d web.km.kz -m bogdandrienko@gmail.com --agree-tos
    sudo openssl dhparam -out /etc/nginx/dhparam.pem 2048

    sudo nano /etc/nginx/sites-available/web-km-kz-https.conf
    <file>
    server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    ssl_certificate /etc/letsencrypt/live/web.km.kz/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/web.km.kz/privkey.pem;

    ssl_session_timeout 1d;
    ssl_session_cache shared:MozSSL:10m;

    ssl_dhparam /etc/nginx/dhparam.pem;

    ssl_protocols TLSv1.2;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;

    ssl_stapling on;
    ssl_stapling_verify on;

    ssl_trusted_certificate /etc/letsencrypt/live/web.km.kz/chain.pem;

    resolver 1.1.1.1;

    client_max_body_size 30M;

    server_name web.km.kz www.web.km.kz;

    root /home/bogdan/web;

    location /.well-known/acme-challenge/ {}

    location /favicon.ico {
        alias /home/bogdan/web/static/logo.png;

        access_log off; log_not_found off;

        expires max;
    }

    location /robots.txt {
        alias /home/bogdan/web/static/robots.txt;

        access_log off; log_not_found off;

        expires max;
    }

    location /static/ {
        alias /home/bogdan/web/static/;

        expires max;
    }

    location /media/ {
        alias /home/bogdan/web/static/media/;

        expires max;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_buffering off;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
    }
    </file>

    sudo ln -s /etc/nginx/sites-available/web-km-kz-https.conf /etc/nginx/sites-enabled/web-km-kz-https.conf
    sudo service nginx start
    sudo systemctl status nginx.service
    sudo ufw allow 'Nginx Full'
    sudo systemctl reload nginx.service
    """
    pass

def celery_python_django():
    """

    # todo check redis
    redis-server
    redis-cli
    ping # PONG
    exit
    # todo check redis

    source env/bin/activate
    pip install celery redis django
    pip freeze > requirements.txt

    # django_setting/celery.py
    import os
    from celery import Celery

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_settings.settings")
    app = Celery("django_settings")
    app.config_from_object("django.conf:settings", namespace="CELERY")
    app.autodiscover_tasks()
    # django_setting/celery.py

    # django_setting/__init__.py
    from .celery import app as celery_app

    __all__ = ("celery_app",)
    # django_setting/__init__.py

    # django_setting/settings.py
    CELERY_APP_TIMEZONE = 'Asia/Almaty'
    CELERY_APP_TASK_TRACK_STARTED = True
    CELERY_APP_TASK_TIME_LIMIT = 1800

    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    # CELERY_BROKER_URL = "amqp://myuser:mypassword@localhost:5672/myvhost"
    # CELERY_RESULT_BACKEND = "redis://localhost:6379"
    # django_setting/settings.py

    # sh (env)
    python -m celery -A django_settings worker -l info
    # sh (env)

    # django_app/celery.py
    # parsing(get data from another web-sites), analyze, reports, image refactor, send mass mail
    @shared_task
    def add(x, y):
        return x + y

    @shared_task
    def count_users():
        time.sleep(3.0)
        return User.objects.count()

    @shared_task
    def send_mass_email(recipients: list, message: dict, skip_error=True):
        results = []
        for recipient in recipients:
            success = False
            error = ""
            try:
                # send_mail(recipient, message)
                pass
            except Exception as error:
                print(error)
                error = error
                if skip_error is False:
                    break
            else:
                success = True
            finally:
                results.append((success, error))
        # return results  # [(True, ""), (False, "timeout error")]
        return [(True, ""), (False, "timeout error")]
    # django_app/celery.py

    # django_app/view.py
    from django_app import celery as current_celery
    from celery.result import AsyncResult
    from django_settings.celery import app as celery_app

    task_id = current_celery.send_mass_email.apply_async([1, 2, 3], {}, skip_error=True, countdown=20)  #
    old_task_id = "33779111-0f42-4a96-bdec-d5643e57a018"

    result = AsyncResult(old_task_id, app=celery_app)
    # print()

    if result.state != "PENDING":
    result = f"status: {result.state} | result: {result.get()}"
    else:
    result = f"status: {result.state} | result: {None}"
    print(result)
    # django_app/view.py
    """
    pass

def docker_python_django():
    """
    mkdir web && cd web
    python3 -m venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install wheel
    pip install Django gunicorn psycopg2 Pillow
    django-admin startproject django_settings .
    django-admin startapp core
    cd core
    mkdir management && cd management
    nano __init__.py       #ctr s ctrl x
    mkdir commands && cd commands
    nano __init__.py  #ctr s ctrl x

    nano wait_for_db.py
    # wait_for_db.py
    import time
    from django.db import connections
    from django.db.utils import OperationalError
    from django.core.management import BaseCommand


    class Command(BaseCommand):
        '''Django command to pause execution until db is available'''

        def handle(self, *args, **options):
            self.stdout.write('Waiting for database...')
            db_conn = None
            while not db_conn:
                try:
                    db_conn = connections['default']
                except OperationalError:
                    self.stdout.write('Database unavailable, waititng 1 second...')
                    time.sleep(1)

            self.stdout.write(self.style.SUCCESS('Database available!'))
    # wait_for_db.py

    nano django_settings/settings.py
    # settings.py
    import os

    DEBUG = os.environ.get("DEBUG", True)
    ALLOWED_HOSTS = ["*"]

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'core',
    ]

    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": os.environ.get("SQL_USER", "user"),
            "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
            "HOST": os.environ.get("SQL_HOST", "localhost"),
            "PORT": os.environ.get("SQL_PORT", "5432"),
        }
    }

    STATIC_ROOT = Path(BASE_DIR/"static")
    # settings.py

    nano .env
    # .env
    # django
    DEBUG=1


    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=django_db
    SQL_USER=django_usr
    SQL_PASSWORD=Qwerty12345!
    SQL_HOST=db
    SQL_PORT=5432

    # postgres
    POSTGRES_DB=django_db
    POSTGRES_USER=django_usr
    POSTGRES_PASSWORD=Qwerty12345!
    # .env

    python3 manage.py runserver 0.0.0.0:8000
    cd ..

    nano docker-compose.yml
    # docker-compose.yml
    version: '3.7'

    services:

      db:
        container_name: db
        image: postgres:latest
        restart: on-failure
        networks:
          - main
        env_file:
          - ./web/.env
        volumes:
          - postgres_data:/var/lib/postgresql/data
      web:
        container_name: web
        restart: on-failure
        depends_on:
          - db
        networks:
          - main
        build:
          context: .
          dockerfile: ./Dockerfile
        env_file:
          - ./web/.env
        image: web
        volumes:
          - .:/web
        ports:
          - 8000:8000
        command: >
          sh -c "python manage.py wait_for_db && python manage.py collectstatic --noinput &&
                 python manage.py makemigrations --noinput && python3 manage.py migrate --noinput &&
                 python manage.py runserver 0.0.0.0:8000"
                 # gunicorn django_settings.wsgi -bind 0.0.0.0:8000
    volumes:
      postgres_data:
    networks:
       main:
         driver: bridge
    # docker-compose.yml

    nano Dockerfile
    # Dockerfile
    FROM python:latest

    ENV PYTHONUNBUFFERED 1
    ENV PYTHONDONTWRITEBYTECODE 1

    RUN apt-get update && apt-get install -y build-essential && apt-get install -y libpq-dev && apt-get install -y gettext \
      && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && rm -rf /var/lib/apt/lists/*

    RUN mkdir /web_build
    COPY ./web /web_build

    COPY ./web/requirements.txt /requirements.txt
    RUN pip install -r /requirements.txt

    WORKDIR /web_build
    # Dockerfile

    nano start.sh
    # start.sh
    #!/bin/bash

    docker-compose run web sh -c "django-admin startproject django_settings app"
    # sudo docker-compose build
    sudo docker-compose up --build
    # sudo docker-compose up -d --build
    # sudo docker compose down
    # start.sh

    source start.sh
    """
    pass

def certbot_ubuntu_python_django():
    """
    sudo systemctl list-timers | grep 'certbot\|ACTIVATES'
    sudo nano /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh
    <file>
    #!/bin/bash
    /usr/bin/systemctl reload nginx.service
    sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh
    sudo certbot renew --dry-run
    </file>
    """
    pass

def curl_ubuntu():
    """
    # curl -v -X GET -H 'x-id:1' 127.0.0.1:8080/todos
    # curl -v -X POST -H 'x-id:1' 127.0.0.1:8080/todos -d '{"userId":2,"id":2,"title":"11111111111111","completed":true}'

    // Create
    // curl -v -X POST 127.0.0.1:8080/books -d '{"id":4,"title":"Amon Ra","author":"V.Pelevin"}'

    // Read
    // curl -v -X GET 127.0.0.1:8080/books/1

    // Read all
    // curl -v -X GET 127.0.0.1:8080/books

    // Update
    // curl -v -X PUT 127.0.0.1:8080/books/1 -d '{"title":"War and peace","author":"N.Tolstoy"}'

    // Delete
    // curl -v -X DELETE 127.0.0.1:8080/books/1
    """
    pass

# TODO WEB #############################################################################################################
