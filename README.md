# TSL NIGERIA Streamit API
## Welcome to TSL Nigeria API. 


The API has a couple of endpoints that gives you access to the database. The base URL allows you to make requests along side sub-endpoints.

### Base URL

```
https://web-production-6c93.up.railway.app/api/
```

Note that every endpoint must have an ending slash. This shows that it is an absolute URL. With the base URL above, requests can be made to various endpoints.

## Requests and Responses

This API gives you access to create and authenticate users, add and remove videos, categories, like videos, add videos to favourites, list and display videos and categories, user profiles and details, et cetera. 

# POST /user/auth-token/
The above is used to authenticate existing users. Please note that this endpoint does not accept a GET request. 

```
{Base_Url}/auth-token/
```

Inorder to make a request, the user must send in a json object. He should ensure that these json objects are properly stringified in the following format, having the following keys: 

```json
{
    "username": "validemail@gmail.com", 
    "password":"validpassword"
}
```
Keys: `username` and `password`.
The `username` key requires the email of an existing user.
The `password` key requires a valid password.

If the json objects come in a different format than the required, an exception of invalid json format will be raised.

## Expected Response
A JWT Token will be generated as a result of your request in this format: 

```json
{
    "token": "afbf91b454b50cc56637d34b77133fef3c6604da", 
    "user_id": 1, 
    "email": "peter@gmail.com"
}
```
Keys: token, user_id, email.

The above token example should be included in the `Authorization` header in order to make subsequent requests. Without the token given, an exception of `UnAuthorized user` will be raised.

If either the password or username (email) entered is inaccurate, a non_field_error is raised.

``
{'non_field_errors': ['Unable to log in with provided credentials.']}
``

You can customize the error however way you would wish in any client side application like React, Angular or Vue.

# POST, GET - /user/
Here, you can retrieve, create, and delete users from the database. Although you should note that each user is conected to a profile object. When a user is deleted, the profile will be deleted automatically.

The required fields necessary to create a user are `email`, `password` and `password2`.
The password2 field is used to compare the user password to see if they match. 
```
{Base_Url}/user/
```
For detail view:
```
{Base_Url}/user/{id}/
```

```json
{
  "email": "validemail@gmail.com",
  "password": "string",
  "password2": "string"
}
```

If `password` and `password2` does not match, an exception is raised: 

```json
{
  "password": "Password must match"
}
```

Creating a user that already exist, will give you the following error:

```json
{"email": ["user with this email already exists."]}
```
You will get this success message when a user is created:

```json
{"email": "sarah@gmail.com", "is_superuser": false, "is_active": false, "date_joined": "2023-01-20T13:12:00.268410Z", "last_login": null}
```

# PUT - /user/change-password/

Here, the password can be changed via the above endpoint.
This change must be made via http headers - i.e. the `Authorization` header.
The parameters that should be provided are as follows:
####

```json
{"old_password":"password","new_password":"password2"}
```
#### old_password: string; new_password: string


# GET, DELETE - /user/:id/
This endpoint retrieves or deletes a single user with a declared id.
Here, you must ensure you send a request with the user id from the client side.

Although deleting a user might come in handy to a site admin or to a client user who wishes to delete his user account, but this should be used with caution.
This is because, when a user instance is deleted, the profile associated with it is also deleted automatically. This means that the user cannot log into his or her account until he creates another user instance.

```
{Base_Url}/user/
```
For detail view:
```
{Base_Url}/user/{id}/
```

The response returned when a user is successfully deleted is as folllows:

```json
{
  "details": "user {id} was successfully deleted"
}
```

A GET request on the other hand fetches you that single user as follows:

```json
{
  "email": "user@gmail.com",
  "is_superuser": false,
  "is_active": true,
  "date_joined": "2023-01-21T05:45:39.075086Z"
}
```


# GET - /profile/
The fields existing for uploading a profile are `username`, `first_name`, `last_name`, `profile_photo`, `bio`, `country`, `gender` and `phone_number`. Non of these fields are required. It is advisable to only make queries with `user_id`, not modify it. You can query the user profile via the `user_id` if your intention is to get the user's prrofile details. `user_details` is automatically generated from the user object. This is because a Profile object is created alongside a User object by default. Hence, the user_id and profile_id are the same. 
Do not send a POST request to the profile object. POST request is not permitted. You can only send a POST request to the user, i.e. WHEN YOUR INTENTION IS TO CREATE A USER. Use a PUT request instead.
A PUT request is ideal for updating the user profile.

This means that you can use the user_id or profile_id interchangeably. We do this to ensure that every user instance is connected to a Profile object. You can make your queries with the endpoints below:
For list view:
```
{Base_Url}/profile/
```
The above request will fetch you all the users profiles in the database.
# PUT, GET, DELETE - /profile/:id/

For detail view:
```
{Base_Url}/profile/{id}/
```

## Request via PUT

You can choose to modify any of the following via a PUT request.

```json
{
  "username": "",
  "first_name": "",
  "last_name": "",
  "profile_photo": "/path/to/media/file",
  "bio": "",
  "country": "",
  "gender": "",
  "phone_number": ""
}
```

Note that every PUT request made gives you back the same object.
If you wish to give back a custom reponse to your user. You can make use of your status_code attribute.
Every successfully request has a status code of 200.

## Response via GET

```json

{
  "user_details": {
    "id": 1,
    "email": "peter@gmail.com",
    "is_superuser": true,
    "is_active": true,
    "date_joined": "2023-01-22T02:53:33.065144Z"
  },
  "username": "",
  "first_name": "",
  "last_name": "",
  "profile_photo": null,
  "bio": "",
  "videos_uploaded": [],
  "country": "",
  "gender": "",
  "phone_number": ""
}

```

# GET, POST - /video/

The video object can be queried via a GET request using the endpoints below the endpoint below:

```
{Base_Url}/video/
```
The above gives you the array (or list) of videos and their respected a respective `id`, `title`, `thumbnail`, `author`, `category`, `author`,`likes`, `date_uploaded` and `last_modified`. A typical response from a GET request is as follows: 

```json
[
  {
    "id": 1,
    "title": "My Video",
    "thumbnail": "/media/media/video/Mr-Solomon-Adodo.jpg",
    "author_": {
      "id": 1,
      "first_name": "Paul",
      "last_name": "Daniel"
    },
    "video_file": "/media/print_7_BIJOU_MUDCLOTH_9f2dafc6-8f73-4ac5-99f9-a81c0c3109a4_800x.png",
    "_category": {
      "id": 1,
      "name": "comedy"
    },
    "likes": 0,
    "date_uploaded": "2020-01-01T12:48:48.793169Z",
    "last_modified": "2020-01-01T12:48:55.924193Z"
  }
]
```









