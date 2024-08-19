# Thought Process - Request Type Management API

## 1. Authentication Using Email Passed in Headers

**Decision**: I implemented an authentication mechanism where the user's email is passed in the headers for every API request. This email is stored in the frontend's local storage and is used to authenticate and authorize the user for backend operations.

**Justification**: This approach simplifies the authentication flow by avoiding the complexity of managing tokens (such as JWT). It is particularly useful for the given scope as the user's credentials are persisted in the local storage. By storing the email in local storage, the user can maintain their session across different interactions with the application.

**Tradeoff**: While this method is simpler and easier to implement, it is not as secure as traditional methods like JWT tokens, which provide better protection against certain types of attacks (e.g., CSRF). The tradeoff was made considering the simplicity and scope of the project, understanding that a more secure method could be implemented in a production environment.

## 2. Chose `db.json` for Simplicity

**Decision**: I opted to use a `db.json` file as the storage mechanism for the request types instead of a full-fledged database like PostgreSQL or MySQL.

**Justification**: The choice of `db.json` was driven by the simplicity it offers in setup and usage.

**Tradeoff**: The main tradeoff here is scalability. While `db.json` is sufficient for demo applications and prototyping, it lacks the robustness, performance, and features (like concurrent access and transactions) provided by traditional relational databases. In a production environment, transitioning to a more robust database would be necessary.

## 3. Validations for Handling Edge Cases in CRUD Operations

**Decision**: I implemented validations in the CRUD operations to handle various edge cases, ensuring data integrity and proper error handling.

**Justification**: Validations are crucial for maintaining the integrity of the data and ensuring that the API handles different scenarios gracefully. By validating input data, checking for the existence of resources before updating or deleting, and providing clear error messages, the API becomes more reliable and user-friendly. These validations prevent common issues like trying to update or delete non-existent resources, or submitting invalid data.

**Tradeoff**: Implementing comprehensive validations adds complexity to the codebase and requires additional time for development and testing. However, this tradeoff is justified as it leads to a more robust and dependable API, which is essential for providing a good user experience and maintaining data integrity.
