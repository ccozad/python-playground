from flask import Response
import json

class GenericResponse():
    def bad_request():
        return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')

    def not_found():
        return Response(json.dumps({'status': 'not found'}, indent=4), status=404, mimetype='application/json')

    def no_content():
        return Response(None, status=204, mimetype='application/json')
    
    def single_item(item, created=False):
        if created:
            return Response(json.dumps(item.to_dictionary(), indent=4), status=201, mimetype='application/json')
        else:
            return Response(json.dumps(item.to_dictionary(), indent=4), status=200, mimetype='application/json')

    def many_items(items):
        all_items = []
        for item in items:
            all_items.append(item.to_dictionary())
        
        return Response(json.dumps(all_items, indent=4), status=200, mimetype='application/json')

