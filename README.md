# Backend Project - Request Type Management API

This project is a RESTful API built with FastAPI that manages request types, allowing users to create, update, and delete various types of requests. The project is designed to support a frontend application that interacts with the API to manage request types dynamically.

## Requirements

-   Python 3.8+
-   FastAPI
-   Uvicorn (ASGI server)
-   Pydantic
-   JSON file storage

## Installation

1.  Clone the repository:

    ```bash
    https://github.com/Rithik1010/intake-backend.git
    cd intake-backend

    ```

2.  Create a virtual environment and activate it:

    ```bash
    python3 -m venv env
    source env/bin/activate # On Windows, use `env\Scripts\activate`
    ```

3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the FastAPI Application

    ```bash
    uvicorn main:app --reload
    ```

The API will be accessible at [http://localhost:8000](http://localhost:8000).

## Access the Swagger Documentation

After running the FastAPI application, you can access the Swagger UI at:

-   **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
-   **ReDoc UI**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These interfaces allow you to interact with your API, view the available endpoints, and see the expected request and response formats.

## Endpoints

-   **GET** `/request-types/`  
    Fetch all request types.

-   **POST** `/request-types/`  
    Create a new request type.

-   **PUT** `/request-types/{index}`  
    Update an existing request type.

-   **DELETE** `/request-types/{index}`  
    Delete a request type.
