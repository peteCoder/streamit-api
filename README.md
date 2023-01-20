# TSL NIGERIA Streamit API
## Welcome to TSL Nigeria API. 

### Base URL
The API has a couple of endpoints that gives you access to the database. The base URL allows you to make requests along side sub-endpoints.

```
https://web-production-6c93.up.railway.app/api/
```

Note that every endpoint must have an ending slash. This shows that it is an absolute URL. With the base URL above, requests can be made to various endpoints.

## Requests and Responses

This API gives you access to create and authenticate users, add and remove videos, categories, like videos, add videos to favourites, list and display videos and categories, user profiles and details, et cetera. 

# POST user/auth-token/
The above is used to authenticate existing users. Please note that this endpoint does not accept a GET request. Inorder to make a request, the user must send in a json object. He should ensure that these json objects are properly stringified in the following format, having the following keys: 

```json
{
    "username": "validemail@gmail.com", 
    "password":"validpassword"
}
```
Keys: username and password.
The username key requires the email of an existing user.
The password key requires a valid password.

If the json objects come in a different format than the required, an exception of invalid json format will be raised.

## Expected Response
A JWT Token will be generated as a result of your request in this format: 

```json
{
    "token": "afbf91b454b50cc56637d34b77133fef3c6604da", "user_id": 1, 
    "email": "peter@gmail.com"
}
```
The above token example should be included in the Authorization header in order to make subsequent requests. Without the token given, an exception of `UnAuthorized user` will be raised.

If either the password or username (email) entered is inaccurate, a non_field_error is raised.

``
{'non_field_errors': ['Unable to log in with provided credentials.']}
``

You can customize the error however way you would wish in any client side application like React, Angular or Vue.

### 

