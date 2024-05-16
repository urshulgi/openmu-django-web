# openmu-django-web

Django website for [OpenMU](https://github.com/MUnique/OpenMU)

Other website solutions for OpenMU:

- Laravel/PHP: [openmu-website](https://github.com/antonioanerao/openmu-website)
- NodeJS/React: [open-mu-web](https://github.com/mamfloo/open-mu-web)


# Setup
Install psycopg2 for postgresql according to [Django Project - Database Installation](https://docs.djangoproject.com/en/5.0/topics/install/#database-installation):
```bash
pip install psycopg2-binary
```

## Database connection

We use two separate databases. One of them is the OpenMU database and the second one is our internal database.

In the future, the internal database should be used for a bug tracker and news.

*file: ~/.pg_service.conf*
```
[openmu_service]
host=localhost
user=postgres
dbname=openmu
port=5432

[openmu_web_service]
host=localhost
user=USER
dbname=NAME
port=5432
```

This is the information for the OpenMU database:

*file: openmu-django-web/openmu_web/.openmu_pgpass*
```
localhost:5432:openmu:postgres:admin
```

This would be for our web database:

*file: openmu-django-web/openmu_web/.openmu_web_pgpass*
``` 
localhost:5432:NAME:USER:PASSWORD
```

# Run
```bash
$ cd openmu_web
$ python manage.py migrate
$ python manage.py runserver
```