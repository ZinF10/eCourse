# Back-End 🌶️

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Author](#author)

## About

The `Flask` 🌶️ project follows a RESTful API architectural style, emphasizing the principles of statelessness, resource identification, and uniform interface. By adhering to RESTful principles, the project aims to provide a clear and consistent approach to designing web services, promoting scalability, flexibility, and ease of maintenance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Create the environment (creates a folder in your current directory)

```bash
virtualenv .venv
```

In Linux or Mac, activate the new python environment

```bash
source .venv/bin/activate
```

Or in Windows

```bash
source .venv/Scripts/activate
```

### Installing

With the above application you can create a migration repository with the following command

```bash
flask db init
```

You can then generate an initial migration

```bash
flask db migrate -m "Initial migration"
```

Then you can apply the changes described by the migration script to your database

```bash
flask db upgrade
```

File `.env`

```bash
SECRET_KEY=<secret_key>
CLOUD_NAME=<cloud_name>
API_KEY=<api_key>
API_SECRET=<api_secret>
DB_USERNAME=<username>
DB_PASSWORD=<password>
DB_HOST=<host>
MAIL_USERNAME=<your_email>
MAIL_PASSWORD=<your_password>
```

Run all testcase

```bash
python -m unittest discover
```

CLI create `Admin` user

```bash
python manage.py create_admin
```

## Author

Copyright &copy; 2024 by [ZIN](http://www.github.com/zinitdev)
