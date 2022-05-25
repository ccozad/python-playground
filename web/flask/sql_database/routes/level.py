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
    
    elif request.method == 'GET':
        all_levels = []
        results = Level.query.all()
        for item in results:
            all_levels.append(item.to_dictionary())
        return Response(json.dumps(all_levels, indent=4), status=200, mimetype='application/json')