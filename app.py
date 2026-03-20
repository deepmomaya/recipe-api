from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

recipes = []
current_id = 1


# POST /recipes
@app.route('/recipes', methods=['POST'])
def create_recipe():
    global current_id

    data = request.get_json()
    required_fields = ["title", "making_time", "serves", "ingredients", "cost"]

    if not data or not all(field in data for field in required_fields):
        return jsonify({
            "message": "Recipe creation failed!",
            "required": "title, making_time, serves, ingredients, cost"
        }), 200

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    recipe = {
        "id": current_id,
        "title": data["title"],
        "making_time": data["making_time"],
        "serves": data["serves"],
        "ingredients": data["ingredients"],
        "cost": data["cost"],
        "created_at": now,
        "updated_at": now
    }

    recipes.append(recipe)
    current_id += 1

    return jsonify({
        "message": "Recipe successfully created!",
        "recipe": [recipe]
    }), 200


# GET /recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify({
        "recipes": recipes
    }), 200


# GET /recipes/<id>
@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    for recipe in recipes:
        if recipe["id"] == id:
            return jsonify({
                "message": "Recipe details by id",
                "recipe": [recipe]
            }), 200

    return jsonify({
        "message": "No recipe found"
    }), 200


# PATCH /recipes/<id>
@app.route('/recipes/<int:id>', methods=['PATCH'])
def update_recipe(id):
    data = request.get_json()

    for recipe in recipes:
        if recipe["id"] == id:
            recipe["title"] = data.get("title", recipe["title"])
            recipe["making_time"] = data.get("making_time", recipe["making_time"])
            recipe["serves"] = data.get("serves", recipe["serves"])
            recipe["ingredients"] = data.get("ingredients", recipe["ingredients"])
            recipe["cost"] = data.get("cost", recipe["cost"])
            recipe["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            return jsonify({
                "message": "Recipe successfully updated!",
                "recipe": [recipe]
            }), 200

    return jsonify({
        "message": "No recipe found"
    }), 200


# DELETE /recipes/<id>
@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    global recipes

    for recipe in recipes:
        if recipe["id"] == id:
            recipes = [r for r in recipes if r["id"] != id]
            return jsonify({
                "message": "Recipe successfully removed!"
            }), 200

    return jsonify({
        "message": "No recipe found"
    }), 200


# 404 for all other routes
@app.errorhandler(404)
def not_found(e):
    return "", 404


# Run server (IMPORTANT for Render)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)