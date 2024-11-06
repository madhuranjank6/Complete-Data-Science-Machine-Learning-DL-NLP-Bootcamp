## Put and Delete
## Working With API's --JSON

from flask import Flask, jsonify, request

app = Flask(__name__)


## Initial Data in the to do list
items = [
    {"id":1,"name":"Item 1", "description":"This is Item 1"},
    {"id":2,"name":"Item 2", "description":"This is Item 2"}
]

@app.route("/")
def home():
    return "Welcome to the Sample To DO List App"

## GET: Retrieve all the items
@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

## GET: Retrieve specific items by ID
@app.route("/items/<int:item_id>",methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({"error":"Item Not Found"})
    return jsonify(item)

## POST: Create a new task
@app.route("/items",methods = ['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Invalid Json Payload Body"})
    new_item = {
        "id":items[-1]["id"]+1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)


## PUT: Update an existing Item
@app.route("/items/<int:item_id>",methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item Not Found"})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

## DELETE: delete an item
@app.route("/items/<int:item_id>",methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result":"Item Deleted"})

if __name__ == '__main__':
    app.run(debug=True)