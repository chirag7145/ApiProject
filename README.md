# PizzaApi
Created a Django application that should be able to store information about different types of Pizza.
Used Postgresql Database for storing the data.
An API interface that lists the information about all the different stored pizzas, and also be able to interact with that information (such as edit or delete).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. So first of all clone this project into your local machine. And using terminal enter into the pizzaApi directory. 
(I'm Ubuntu User)
### Prerequisites

What things you need to install the software and how to install them

```
Code Editor (VS Code)
Django
Django RestFramework
Postgresql
Pgadmin4 (Visulaisation of the database)
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

#### Create a virtual environment and activate it
```
Desktop/ApiProject/pizzaApi$ mkvirtualenv PizzaApi
Desktop/ApiProject/pizzaApi$ workon PizzaApi
(PizzaApi)Desktop/ApiProject/pizzaApi$
```

#### Installing the requirements from requirements.txt
* asgiref==3.3.1
* Django==3.1.4
* django-filter==2.4.0
* djangorestframework==3.12.2
* psycopg2==2.8.6
* pytz==2020.4
* sqlparse==0.4.1

```
(PizzaApi)$ pip3 install -r requirements.txt
```

Dependencies are get installed

#### For setting up the postgres database you can refer...
* https://youtu.be/-LwI4HMR_Eg (For Ubuntu)
* https://youtu.be/e1MwsT5FJRQ (For Windows)
* https://www.pgadmin.org/download/ (Pgadmin Download)

I hope postgresql and Pgadmin are all set in your system.

## Setting up the files and running the server
Postgresql database is used and you need to enter your postgres database credentials to access the database and run this project.  

And after this, run the commands,
```
(PizzaApi)Desktop/ApiProject/pizzaApi$ python3 manage.py makemigrations
(PizzaApi)Desktop/ApiProject/pizzaApi$ python3 manage.py migrate
(PizzaApi)Desktop/ApiProject/pizzaApi$ python3 manage.py runserver
```
Now, the server will be running at http://127.0.0.1:8000/
(ALLOWED_HOSTS = ['127.0.0.1','localhost']  you can add any other host if you want so :-))
A superuser can also be created to visualise the admin panel and the data
For creating superuser,
```
(PizzaApi)Desktop/ApiProject/pizzaApi$ python3 manage.py createsuperuser
```
* Fill in the name and password and get the user created
* Now, logging with the created user at http://127.0.0.1:8000/admin/ and now you can see the admin panel 
(All the models/tables are registred on admin)
* Now we can also create the model object using this admin panel.

## Brief about database schema
This project has three models
* Pizza
* Size
* Topping

#### Pizza Model
* ID : AutoField (Integer that increments itself on adding up new Pizza object), Primary Key
* Type: CharField (Take characters of max length 2. Choices are given to this (RG : Regular,SQ : Square))
* Size: ForeignField (Size model is also present, it allows the values from that model only. If we add or remove any particular value from the size all the related objects to it will also get removed)
* Topping: ForeignField (Topping model is also present, it allows the values from that model only. If we add or remove any particular value from the size all the related objects to it will also get removed)

#### Size Model
* Size : Charfield (Size upto 50 characters, unique value must be there), Primary Key
* Inserting (Small,Medium,Large)

#### Size Model
* Topping : Charfield (Size upto 50 characters, unique value must be there), Primary Key
* Inserting (Onion,Tomato,Corn,Capsicum,Cheese,Jalapeno)

## API endpoints

#### http://127.0.0.1:8000/api/pizza/create/ (This is for creating new pizza whether Regular or Square)

* Example1
```
JSON data we are passing 
{
    "type": "SQ",
    "size": "Small",
    "topping": "Onion"
}
```
Response that we get... We have successfully created the object
```
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "type": "SQ",
    "size": "Small",
    "topping": "Onion"
}
```
* Example2
```
JSON data we are passing 
{
    "type": "RG",
    "size": "Extra Large",
    "topping": "Cheese"
}
```
Response that we get... We passed the wrong size "Extra Large" that is not there in the database
```
HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "size": [
        "Invalid pk \"Extra Large\" - object does not exist."
    ]
}
````
* Example3
```
JSON data we are passing 
{
    "type": "AS",
    "size": "Extra Large",
    "topping": "Cheesy Paneer"
}
```
Response that we get... We passed the wrong size, wrong type and the wrong topping
```
HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "type": [
        "\"AS\" is not a valid choice."
    ],
    "size": [
        "Invalid pk \"Extra Large\" - object does not exist."
    ],
    "topping": [
        "Invalid pk \"Cheesy Paneer\" - object does not exist."
    ]
}
````
* Example4
```
{
    "type": "SQ",
    "size": null,
    "topping": "Capsicum"
}
```
Response that we get... Size is not present
```
HTTP 400 Bad Request
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "size": [
        "This field may not be null."
    ]
}
```
* Example5
```
{
    "type": "RG",
    "size": "Large",
    "topping": "Corn"
}
```
New object is created
```
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "type": "RG",
    "size": "Large",
    "topping": "Corn"
}
```

#### http://127.0.0.1:8000/api/pizzas/ (This is for getting the list of all the stored pizzas you can also filter out the data based on the type & size of pizza)

* Example1
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "type": "SQ",
        "size": "Small",
        "topping": "Onion"
    },
    {
        "id": 2,
        "type": "RG",
        "size": "Large",
        "topping": "Corn"
    }
]
```
We created two pizzas and that are visible in this list

* Example2
* http://127.0.0.1:8000/api/pizzas/?type=SQ&size=Small (Filtering the data on the basis of given type and size)
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "type": "SQ",
        "size": "Small",
        "topping": "Onion"
    }
]
```
* Example3
* http://127.0.0.1:8000/api/pizzas/?type=&size=Large (Filtering the data on the basis of size)
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "type": "RG",
        "size": "Large",
        "topping": "Corn"
    }
]
```
#### http://127.0.0.1:8000/api/pizza/<int:id>/ (This is for retrieving the current pizza with the given id you can edit or delete it as well)
* Example1
* Passing the JSON (We are editing the type of topping earlier it was corn, now it is Capsicum)
```
{
    "id": 2,
    "type": "RG",
    "size": "Large",
    "topping": "Capsicum"
}
```
Updated Response
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "type": "RG",
    "size": "Large",
    "topping": "Capsicum"
}
```
* Example2
* Deleting the first pizza 
```
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
* Example3
* If we try to run any url for which the pizza is not there 
Like, http://127.0.0.1:8000/api/pizza/3/
```
HTTP 404 Not Found
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "Not found."
}
```
#### Finally what is there in the database,
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "type": "RG",
        "size": "Large",
        "topping": "Capsicum"
    }
]
```

## Refer the documentation for more knowledge...
* https://www.django-rest-framework.org/
* https://docs.djangoproject.com/en/3.1/

#### Want to contact me ?? (Feel free to ask if there is any confusion or issue, it is working fine)
* chirag7145@gmail.com
* +919354048650
