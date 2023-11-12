# Social Network API

## Overview:
This Django Rest Framework project serves as the backend for a social networking application, offering a set of API endpoints to facilitate user registration, authentication, and friend management. The installation steps cater to both Docker and non-Docker environments.

- Backend: Django, Django Restframework
- Database: SQLite3
- Authentication: Token Authentication
- [Download Postman Collection](https://raw.githubusercontent.com/salahoddin88/social_networking/main/README.md)

## Installation Steps
1. Clone the repository:
```sh
git clone https://github.com/salahoddin88/social_networking.git
```
2. Navigate to the project directory
```sh
cd social_networking
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



## API Endpoints:
- Registration
    - URL: SERVERURL + /api/user/registration/
    - Method : POST
    - Payload:
        ```sh
            {
                first_name: str (optional)
                last_name: str (optional)
                email: str (required)
                password: str (required)
                confirm_password: str (required)
            }
        ```

- Login
    - URL: SERVERURL + /api/auth/token/
    - Method : POST
    - Payload:
        ```sh
            {
                username: str (email address, required)
                password: str (required)
            }
        ```
- Logout
    - URL: SERVERURL + /api/auth/delete-token/
    - Method : POST
    - Header:
    ```sh
        {
            Authorization: Token <token>
        }
    ```
    - Payload: {}

- List of users
    - URL: SERVERURL + /api/user/list/
    - Method : GET
    - Header:
    ```sh
        {
            Authorization: Token <token>
        }
    ```
    - Param:
    ```sh
        {
            search: str (To search email and first name of user)
            page: int (default is <1>)
        }
    ```

- List of all pending friend request
    - URL: SERVERURL + /api/friends/request/
    - Method : GET
    - Header:
    ```sh
        {
            Authorization: Token <token>
        }
    ```
    - Param:  { }

- Send friend requests

    - URL: SERVERURL + /api/friends/request/
    - Method : POST
    - Header:
    ```sh
        {
            Authorization: Token <token>
        }
    ```
    - Payload:
    ```sh
        {
            receiver: int (pk of user)
        }
    ```

- Accept friend request
`request_id` : primary key that is id of List of all pending friend request API

    -URL: SERVERURL + /api/friends/request/`request_id`/accept/
    - Method : PUT
    - Header:
    ```sh
        {
            Authorization: Token <token>
        }
    ```
    Payload: { }

- Reject friend request
    `request_id` : primary key that is id of List of all pending friend request API
    - URL: SERVERURL + /api/friends/request/`request_id`/reject/
    - Method : PUT
    - Header:
    ```sh
        {
            Authorization: Token <token>
        }
    ```
    - Payload: {}

- List of all the friends

    - URL: SERVERURL + /api/friends/
    - Method : GET
    - Header:
    ```sh
        {
            Authorization: Token <token>
        }
    ```
    Param: { }
