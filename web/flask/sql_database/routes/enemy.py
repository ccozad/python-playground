from app import app
from database import db
from models.enemy import Enemy
import json

from flask import request, Response

@app.route("/enemies/", methods=['GET', 'POST'])
def all_enemies():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is not None:
            if 'name' in body and 'max_health' in body:
                enemy = Enemy(name = body['name'], max_health = body['max_health'])
                db.session.add(enemy)
                db.session.commit()
                return Response(json.dumps(enemy.to_dictionary(), indent=4), status=201, mimetype='application/json')
            else:
                return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
    
    elif request.method == 'GET':
        all_enemies = []
        results = Enemy.query.all()
        for item in results:
            all_enemies.append(item.to_dictionary())
        return Response(json.dumps(all_enemies, indent=4), status=200, mimetype='application/json')
