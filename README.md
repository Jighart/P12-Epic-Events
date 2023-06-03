# About the project

**OpenClassrooms Project #12: Develop a Secure Back-End Architecture Using Django ORM**

_Developed on Windows 10 - Python 3.10 - Django 4.2.1 - DRF 3.14_

##

**API-EpicEvents** is a Customer Relationship Management (*CRM*) API designed for _Epic Events_, an events management company.

Epic Events users can:

- Create and update a client database
- Create and manage contracts and organise related events

The RESTful API is implemented with a secured database built with Django ORM and PostgreSQL.


# Installation

## Repository and dependencies

### Windows

```
git clone https://github.com/Jighart/P12-Epic-Events.git

cd P12-Epic-Events 
python -m venv venv 
venv\Scripts\activate

pip install -r requirements.txt
```

### MacOS and Linux

```
git clone https://github.com/Jighart/P12-Epic-Events.git

cd P12-Epic-Events 
python3 -m venv venv 
source venv/bin/activate

pip install -r requirements.txt
```

## Create Postgres database

Install [Postgres](https://www.postgresql.org/download/).
Follow the [documentation](https://www.postgresql.org) to run the server.

Create a new Postgres database with SQL shell (psql) : ```CREATE DATABASE your_db_name;```

## Environment variables: .env file

The Django ```settings.py``` file pulls the database settings from the ```.env``` file, located in the same folder.

The .env file holds the following information required to complete the database setup:

```
SECRET_KEY=<your django secret key>
DB_NAME=<your db name>
DB_USER=<your db username>
DB_PASSWORD=<your db password>
DB_HOST=<your configured db IP/host>
DB_PORT=<your configured db port>
```

## Migrate the database

To migrate, run ```python manage.py migrate```. The Status table is automatically populated during migrations.

## Create a superuser

Run ```python manage.py create superuser```

## Create data with custom management commands

Run the following commands prefixed with ```python manage.py``` to populate the database with some dummy data:

| Command                | Description                                                                      |
|------------------------|----------------------------------------------------------------------------------|
| ```create_data```      | **Create a set of all objects** (20 users, 40 clients, 20 contracts, 10 events)  |
| ```create_status```    | **Verify status have been created during migration**                             |
| ```create_users```     | **Create a set of users.** Args: ```-n``` *or* ```--number``` (default: 20).     |
| ```create_clients```   | **Create a set of clients.** Args: ```-n``` *or* ```--number``` (default: 40).   |
| ```create_contracts``` | **Create a set of contracts.** Args: ```-n``` *or* ```--number``` (default: 20). |
| ```create_events```    | **Create a set of clients.** Args: ```-n``` *or* ```--number``` (default: 10).   |

***Note:*** *Events are exclusively related to one signed contract; the command will create as many events as possible if the amount provided is higher than available contracts.*

# Usage

Run the server with ```python manage.py runserver```. The CRM is browsable via the API or via the admin site.

User management is only available via the admin site and does not appear in the API.

You can find details of the endpoints on the [Postman documentation](https://documenter.getpostman.com/view/26832348/2s93sW8agM).

## Admin site

Tha admin site is available at http://127.0.0.1:8000/admin/. Admin site access is granted to all users.

All users are flagged as staff and all members of the management team are flagged as superusers.