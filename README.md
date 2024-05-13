# openmu-django-web

# Setup
Create database:
```bash
sudo -u postgres psql -c "CREATE ROLE openmuweb WITH PASSWORD 'openmuweb'"
sudo -u postgres psql -c "ALTER ROLE openmuweb WITH LOGIN"
sudo -u postgres psql -c "CREATE DATABASE openmuweb WITH OWNER openmuweb"
```

Install psycopg2 for postgresql according to [Django Project - Database Installation](https://docs.djangoproject.com/en/5.0/topics/install/#database-installation):
```bash
pip install psycopg2-binary
```

## Database connection


~/.pg_service.conf
```
[openmu_service]
host=localhost
user=USER
dbname=NAME
port=5432
```

openmu-django-web/openmu_web/.openmu_pgpass
```
localhost:5432:NAME:USER:PASSWORD
```

# Run
```bash
$ cd openmu_web
$ python manage.py migrate
$ python manage.py runserver
```