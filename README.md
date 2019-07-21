This is an attempt of mine to create a Flask API with JWT

Production ready API on Heroku.

The API includes all the methods GET, POST, DELETE, PUT
It is about creating Stores, Itesm in Stores, Creating a User to register and retrieve the JWT token in order to access other methods related to Stores and respective items.

The methods are mentioned below:
* **{{url}}/register** - Register the user with body - name and password
* **{{url}}/auth** - Retrieve the Access token body - name and password
* **{{url}}/store/name** - POST / GET  / PUT / DELETE store name 
* **{{url}}/stores** - GET list of stores
* **{{url}}/item/name** - GET / POST / PUT / DELETE items, body for POST / PUT - price ( float) and store_id (int)
* **{{url}}/items** - GET a list of items.

It is deployed at the below URI for a limited time
* https://flask-stores-api-trial.herokuapp.com 


