# Thought Process - Backend Project

## Objective

The goal of this backend project was to create a RESTful API to manage request types, allowing users to create, update, and delete request types.

## Initial Approach

1. **Framework Selection**: FastAPI was chosen for its ease of use, speed, and automatic generation of interactive API documentation.
2. **Data Storage**: A JSON file was used to store request types. This decision was made for simplicity, but it has limitations (e.g., concurrency issues). For production, a proper database like PostgreSQL or MongoDB should be used.
3. **Schema Definition**: Pydantic was used for data validation and serialization. This ensured that the data received from the frontend adheres to the expected structure.

## API Design

-   **Endpoints**: I followed RESTful principles to design the API endpoints, ensuring that they are intuitive and follow best practices.
-   **Error Handling**: Basic error handling was implemented using FastAPI's `HTTPException`. For instance, trying to update or delete a non-existent request type returns a `404` error.
-   **Data Validation**: Pydantic models are used to validate incoming data to ensure that required fields are provided and are in the correct format.

## Tradeoffs and Considerations

1. **JSON File Storage**: While easy to implement, JSON file storage is not ideal for concurrent access and large datasets. Moving to a relational or NoSQL database would be more appropriate for scalability.
2. **Simplicity vs. Robustness**: The current implementation is simple but lacks features like user authentication, logging, and comprehensive error handling, which would be necessary for a production system.

The focus of this project was on demonstrating the ability to quickly prototype an API while following best practices in design and implementation.
