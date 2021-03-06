## IF YOU WANT TO RUN A FULL STACK APPLICATION:

![contact_list_full_stack_app](https://user-images.githubusercontent.com/42359973/102006672-cd5a5900-3cf0-11eb-92e9-7c1eb8d04272.gif)

## IF YOU ONLY WANT THE API:

![contact_list_API](https://user-images.githubusercontent.com/42359973/102007218-0d233f80-3cf5-11eb-871e-4cd20448a951.gif)


# Flask Boilerplate for profesional development

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io#https://github.com/4GeeksAcademy/flask-rest-hello.git)

## Features

- Extensive documentation [here](https://github.com/4GeeksAcademy/flask-rest-hello/tree/master/docs).
- Integrated with Pipenv for package managing.
- Fast deloyment to heroku with `$ pipenv run deploy`.
- Use of `.env` file.
- SQLAlchemy integration for database abstraction.

## How to stat the project?

There is an example API working with an example database. All your application code should be written inside the `./src/` folder.

- src/main.py (it's were your endpoints should be coded)
- src/models.py (your database tables and serialization logic)
- src/utils.py (some reusable classes and functions)

For a more detailed explanation look for the tutorial inside the `docs` folder.

## Remember migrate every time you change your models

You have to migreate and upgrade the migrations for every update your make to your models:
```
$ pipenv run migrate (to make the migrations)
$ pipenv run upgrade  (to update your databse with the migrations)
```


# Manual Instalation for Ubuntu & Mac

⚠️ Make sure you have `python 3.6+` and `MySQL` installed on your computer and MySQL is running, then run the following commands:
```sh
$ pipenv install (to install pip packages)
$ pipenv run migrate (to create the database)
$ pipenv run start (to start the flask webserver)
```


## Deploy your website to heroku

This template is 100% compatible with heroku, just make sure to understand and execute the following steps

```sh
// Install heroku
$ npm i heroku -g
// Login to heroku on the command line
$ heroku login -i
// Create an application (if you don't have it already)
$ heroku create <your_application_name>
// Commit and push to heroku (commited your changes)
$ git push heroku master
```
⚠️ For a more detailed explanation on working with .env variables or the MySQL database [read the full guide](https://github.com/4GeeksAcademy/flask-rest-hello/blob/master/docs/DEPLOY_YOUR_APP.md).


## 'HOW TO' GUIDE

### Welcome to CONTACT LIST API

This is a simple API that will let you ***GET***, ***UPDATE***, ***POST*** and ***DELETE*** contacts to/from our API

Here is the body to ***POST*** a contact in JSON format using /contact endpoint:

{

"address": "",

"full_name": "",

"phone": "",

"email": ""

}

To ***GET*** information about posted contacts use the same endpoint.

To ***UPDATE***  a posted contact use the same JSON body as shown above and use ***PUT*** method in POSTMAN using **/update/#**  endpoint, where you put your contact's id instead of the #

To ***DELETE*** a posted contact use ***DELETE*** method in POSTMAN using the same **/update/#**  endpoint, where you put your contact's or songs's id instead of the #
