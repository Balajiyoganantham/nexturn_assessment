#Description creating a flask , for the server side to recieve the client request 

from flask import Flask, jsonify, request, abort

# Flask Initialization
app = Flask(__name__)

# In-Memory Data
teachers = [
    {
        "id": 1,
        "name": "John Smith",
        "subject": "Mathematics"
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "subject": "Physics"
    }
]

# Home Route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Teacher API"

# GET /teachers - Get all teachers
@app.route("/teachers", methods=["GET"])
def get_teachers():
    return jsonify(teachers)

# GET /teachers/<int:id> - Get teacher by id
@app.route("/teachers/<int:id>", methods=["GET"])
def get_teacher(id):
    teacher = next((teacher for teacher in teachers if teacher["id"] == id), None)
    if teacher:
        return jsonify(teacher)
    else:
        abort(404, description="Teacher not found")

# PUT /teachers/<int:id> - Update teacher by id
@app.route("/teachers/<int:id>", methods=["PUT"])
def update_teacher(id):
    teacher = next((teacher for teacher in teachers if teacher["id"] == id), None)
    if not teacher:
        abort(404, description="Teacher not found")
    
    if not request.json:
        abort(400, description="Request body is missing")
    
    data = request.json
    teacher.update(data)
    return jsonify(teacher)

# POST /teachers - Add new teacher
@app.route("/teachers", methods=["POST"])
def add_teacher():
    if not request.json or not 'name' in request.json or not 'subject' in request.json or not 'id' in request.json:
        abort(400, description="Invalid request body")
    
    # Check if the ID already exists
    new_id = request.json['id']
    if any(teacher['id'] == new_id for teacher in teachers):
        abort(400, description=f"Teacher with ID {new_id} already exists")
    
    new_teacher = {
        "id": new_id,
        "name": request.json['name'],
        "subject": request.json['subject']
    }
    
    teachers.append(new_teacher)
    return jsonify(new_teacher), 201

# DELETE /teachers/<int:id> - Delete teacher by id
@app.route("/teachers/<int:id>", methods=["DELETE"])
def delete_teacher(id):
    teacher = next((teacher for teacher in teachers if teacher["id"] == id), None)
    if not teacher:
        abort(404, description="Teacher not found")
    
    teachers.remove(teacher)
    return jsonify(teacher)

# Run the Flask Application
if __name__ == "__main__":
    app.run(debug=True)
