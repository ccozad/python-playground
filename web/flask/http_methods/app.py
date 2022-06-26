from flask import Flask, request, Response
from uuid import uuid4
import json

app = Flask(__name__)

# Our storage for this example will simply be an in memory dictionary
storage = {
    'students': {}
}

@app.route("/")
def index():
    results = []
    results.append('<html><head></head><body>')
    results.append('<p>HTTP Methods demo</p>')
    results.append('<ul>')
    results.append('<li>Get all students GET /students/</li>')
    results.append('<li>Create a student POST /students/</li>')
    results.append('<li>Show a single student GET /students/<id></li>')
    results.append('<li>Update a single student PATCH /students/<id></li>')
    results.append('<li>Delete a single student DELETE /students/<id></li>')
    results.append('</body></html>')
    return ''.join(results)

@app.route("/students/", methods=['GET', 'POST'])
def all_students():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is not None:
            # A simple way to have unique ids is to generate a v4 uuid
            id = uuid4()
            body['id'] = str(id)
            storage['students'][str(id)] = body
            # Return the resource that was just created
            return Response(json.dumps(body, indent=4), status=201, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
    elif request.method == 'GET':
        all_students = []
        # Add all the items in the students dictionary to a list
        for k,v in storage['students'].items():
            all_students.append(v)
        return Response(json.dumps(all_students, indent=4), status=200, mimetype='application/json')


@app.route("/students/<id>", methods=['GET', 'PUT', 'DELETE'])
def one_student(id):
    if request.method == 'GET':
        if id in storage['students']:
            return Response(json.dumps(storage['students'][id], indent=4), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'not found'}, indent=4), status=404, mimetype='application/json')
    elif request.method == 'PATCH':
        if id in storage['students']:
            body = request.get_json(silent=True)
            if body is not None:
                # Since this is just an an example we don't really care what is
                # in the request body. A real application might evaluate the
                # body against a series of business rules to make sure the
                # resource has a valid state before saving it
                body['id'] = id
                storage['students'][id] = body
                return Response(json.dumps(body, indent=4), status=200, mimetype='application/json')
            else:
                return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'not found'}, indent=4), status=404, mimetype='application/json')
    elif request.method == 'DELETE':
        if id in storage['students']:
            del storage['students'][id]
            # The typical response for a delete is a 204 (Ro content) with
            # an empty response body
            return Response(None, status=204, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'not found'}, indent=4), status=404, mimetype='application/json')
