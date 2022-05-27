from tkinter import N
from app import app
from database import db
from models.level import Level
import json

from flask import request, Response

@app.route("/levels/", methods=['GET', 'POST'])
def all_levels():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is not None:
            if 'name' in body:
                level = Level(name = body['name'])
                db.session.add(level)
                db.session.commit()
                return Response(json.dumps(level.to_dictionary(), indent=4), status=201, mimetype='application/json')
            else:
                return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
    
    elif request.method == 'GET':
        all_levels = []
        results = Level.query.all()
        for item in results:
            all_levels.append(item.to_dictionary())
        return Response(json.dumps(all_levels, indent=4), status=200, mimetype='application/json')


@app.route("/levels/<id>", methods=['GET', 'PUT', 'DELETE'])
def one_level(id):
    n_id = int(id)
    level = Level.query.filter_by(id = n_id).first()
    if request.method == 'GET':
        
        if level is not None:
            return Response(json.dumps(level.to_dictionary(), indent=4), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'not found'}, indent=4), status=404, mimetype='application/json')
    
    elif request.method == 'PUT':
        if level is not None:
            body = request.get_json(silent=True)
            if body is not None:
                if 'name' in body:
                    level.name = body['name']
                    db.session.commit()
                    return Response(json.dumps(level.to_dictionary(), indent=4), status=200, mimetype='application/json')
                else:
                    return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
            else:
                return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'not found'}, indent=4), status=404, mimetype='application/json')
    
    elif request.method == 'DELETE':
        if level is not None:
            db.session.delete(level)
            db.session.commit()
            return Response(None, status=204, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'not found'}, indent=4), status=404, mimetype='application/json')