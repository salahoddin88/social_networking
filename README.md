
# Social Network API

## Overview:
This Django Rest Framework project serves as the backend for a social networking application, offering a set of API endpoints to facilitate user registration, authentication, and friend management. The installation steps cater to both Docker and non-Docker environments.

- Backend: Django, Django Rest Framework
- Database: SQLite3
- Authentication: Token Authentication
- [Download Postman Collection](https://raw.githubusercontent.com/salahoddin88/social_networking/main/postman_collection.json)

## Installation Steps
1. Clone the repository:
```sh
git clone https://github.com/salahoddin88/social_networking.git
```
2. Navigate to the project directory
```sh
cd social_networking
```
3. Visit the server URL in the browser with port 8000
```sh
127.0.0.1:8000
```
### With Docker
1. Build container
```sh
docker-compose -f docker-compose.yml build
```
2. Run container
```sh
docker-compose -f docker-compose.yml up -d
```
3. Run app, visit server url in browser with port 8000
```sh
127.0.0.1:8000
```
### Without Docker
1. Create a virtual environment:
```sh
python -m venv venv
```
2. Activate the virtual environment:
- On Windows:
```sh
venv\Scripts\activate
```
- On Unix or MacOS:
```sh
source venv/bin/activate
```
3. Install dependencies:
```sh
pip install -r requirements.txt
```
4. Navigate to project directory /app
```sh
cd app
```
5. Apply migrations:
```sh
python manage.py migrate
```
6. Run the development server:
```sh
python manage.py runserver
```
7. Visit the server URL in the browser with port 8000
```sh
127.0.0.1:8000
```

## API Endpoints:
- Registration
    - URL: SERVERURL + /api/user/registration/
    - Method : POST
    - Payload:
        | Fields | Type | Required | Description |
        | ---------|----------|----------|----------|
        | first_name | string | False | optional field can make required |
        | last_name | string | False | optional field can make required |
        | email | string | `True` | Unique valid email address |
        | password | string | `True` | Strong password |
        | confirm_password | string | `True` | Confirm password |
--
- Login
    - URL: SERVERURL + /api/auth/token/
    - Method: POST
    - Payload:
        | Fields | Type | Required | Description |
        | ---------|----------|----------|----------|
        | username | string | `True` | Email Id of user |
        | password | string | `True` | Password of user |
--
- Logout
    - URL: SERVERURL + /api/auth/delete-token/
    - Method: POST
    - Header:
    ```sh
        Authorization: Token <token>
    ```
--
- List of users
    - URL: SERVERURL + /api/user/list/
    - Method : GET
    - Header:
    ```sh
        Authorization: Token <token>
    ```
    - Param:
        | Fields | Type | Required | Description |
        | ---------|----------|----------|----------|
        | search | string | False | search in email and first_name |
        | page | integer | True | default is `1` |
--
- List of all pending friend request
    - URL: SERVERURL + /api/friends/request/
    - Method: GET
    - Header:
    ```sh
        Authorization: Token <token>
    ```
    - Param:
--
- Send friend requests

    - URL: SERVERURL + /api/friends/request/
    - Method: POST
    - Header:
    ```sh
        Authorization: Token <token>
    ```
    - Payload:
        | Fields | Type | Required | Description |
        | ---------|----------|----------|----------|
        | receiver | integer (pk) | `True` | User's primary key (`id`) |

--
- Accept friend request
    `request_id`: Primary key that is the id of the `List of all pending friend request` API
    -URL: SERVERURL + /api/friends/request/`request_id`/accept/
    - Method: PUT
    - Header:
    ```sh
        Authorization: Token <token>
    ```
--
- Reject friend request
    `request_id`: Primary key that is the id of the `List of all pending friend request` API
    - URL: SERVERURL + /api/friends/request/`request_id`/reject/
    - Method: PUT
    - Header:
    ```sh
        Authorization: Token <token>
    ```
--
- List of all the friends

    - URL: SERVERURL + /api/friends/
    - Method: GET
    - Header:
    ```sh
        Authorization: Token <token>
    ```
