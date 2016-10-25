[//]: <> (This is sample of markdown readme)

# {{cookiecutter.app_name}}

{{cookiecutter.app_name}} provides ...

## Install

1. pip install
    
    pip install {{cookiecutter.app_name}}

2. Add {{cookiecutter.app_name}} to django settings.py

    INSTALLED_APPS = [
        ....,
        {{cookiecutter.app_name}},
        ...
    ]

3. Run python/django essential commands:

    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic -l

4. Start hacking or using app.

## Usage

example:

* `/API/v1/` : root url of API version 1
* `/API/v2/` : root url of API version 2
...

## LICENSE

Please read LICENSE file
