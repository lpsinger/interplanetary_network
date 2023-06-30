# About
This service listens to GCN kafka messages, processes and normalizes those messages, and outputs relevant kafka messages.

# Development
## Running locally
* install docker [docker download](https://www.docker.com/products/docker-desktop/)
* install docker-compose `brew install docker-compose` if you have homebrew
* open a terminal window and run the following:
    * `docker-compose up -d --build`
    * `docker-compose up`
* in your browser, navigate to http://localhost:8000/messages/

## Running the listener locally
To listen for GCN messages, you must start the listening process. To do so:

* in your terminal navigate to the project directory
* run `docker exec -it interplanetary_network-web-1 bash`
* you should be at the `/code` directory on the docker machine
* run `python manage.py listen`
* it will look like the process has hung but it is just listening.
* leave this window open while you want to listen for kafka messages.

## Connecting to the Local DB
We are running a postgres server. This runs alongside the server in docker in its own container. To access the database, you must execute the psql command using docker.

* run `docker exec -it interplanetary_network-db-1 psql -U postgres`
* you should be in postres and see your cursor change to `postgres=#`
* run `\l` to see a list of databases
* run `\c ipn` to connect to the ipn database

## Logging Locally
There are a few different places to watch for log messages currently.

* to watch your docker logs run `docker logs --follow interplanetary_network-web-1` in the project directory.
* to see server and database logs, look at the terminal session where you ran `docker-compose up`
* to see listener logs, look in the terminal session where you ran `python manage.py listen`

## Project Organization
This project is created with a type of domain driven design.

* Models - here you will find the definition of the classes/tables/models. Logic doesn't live here.
* Repo - there is a repo for each model. This is where logic and database queries can be found. Functions will be found in the repo for the model that is most applicable. If it is something that is used widely across models, then there is a shared_utils file.
* Listeners - this is where code that defines how to connect to another data source may be found.
* Jobs - these are bits of code that may be run at intervals to accomplish a task
* Management - this is where custom commands are stored. a custom command can be called from within the docker machine by shelling in. These are processes that must be started by calling the particular command.
* Templates - These are the HTML that is rendered for the front end
* Views - this is where data is loaded to populate the template.

when adding models or views, you must remember to import the addition in the __init__.py file within that directory so the project understand that it's part of the models or the views.
