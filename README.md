# Recipe API

This is a simple RESTful API for managing recipes, built with Python and Flask. It was created for a frontend/backend assessment.

## Features

- **POST /recipes**: Create a new recipe
- **GET /recipes**: List all recipes
- **GET /recipes/{id}**: Get a recipe by ID
- **PATCH /recipes/{id}**: Update a recipe by ID
- **DELETE /recipes/{id}**: Delete a recipe by ID
- All responses are in JSON format
- Returns `404` for undefined endpoints
