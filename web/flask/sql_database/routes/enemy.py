from app import app
from database import db
from models.enemy import Enemy
from common.generic_response import GenericResponse as gr

from flask import request

def valid_body(body):
    if body is not None:
        if 'name' in body and 'max_health' in body:
            return True
        else:
            return False
    else:
        return False


@app.route("/enemies/", methods=['GET', 'POST'])
def all_enemies():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if valid_body(body):
            enemy = Enemy(name = body['name'], max_health = body['max_health'])
            db.session.add(enemy)
            db.session.commit()
            return gr.single_item(item = enemy, created = True)
        else:
            return gr.bad_request()
    
    elif request.method == 'GET':
        results = Enemy.query.all()
        return gr.many_items(results)

@app.route("/enemies/<id>/instances/", methods=['GET'])
def all_instances_for_enemy(id):
    n_id = int(id)
    enemy = Enemy.query.filter_by(id = n_id).first()
    if enemy is not None:
        if request.method == 'GET':
            return gr.many_items(enemy.instances)
    else:
        return gr.not_found()


@app.route("/enemies/<id>", methods=['GET', 'PUT', 'DELETE'])
def one_enemy(id):
    n_id = int(id)
    enemy = Enemy.query.filter_by(id = n_id).first()
    if enemy is not None:
        if request.method == 'GET':
            return gr.single_item(item = enemy)
        
        elif request.method == 'PUT':
            body = request.get_json(silent=True)
            if valid_body(body):
                enemy.name = body['name']
                db.session.commit()
                return gr.single_item(item = enemy)
            else:
                return gr.bad_request()
        
        elif request.method == 'DELETE':
            db.session.delete(enemy)
            db.session.commit()
            return gr.no_content()
    else:
        return gr.not_found()
