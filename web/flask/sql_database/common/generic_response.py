from flask import Response
import json

class GenericResponse():
    def bad_request():
        return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')

    def not_found():
        return Response(json.dumps({'status': 'not found'}, indent=4), status=404, mimetype='application/json')

    def no_content():
        return Response(None, status=204, mimetype='application/json')
