from app import app
from database import db
from models.enemy import Enemy
from models.level import Level
from models.enemy_instance import EnemyInstance
from common.generic_response import GenericResponse as gr

from flask import request

def valid_body(body):
    if body is not None:
        locacation_fields = 'x_location' in body and 'y_location' in body and 'z_location' in body
        id_fields = 'enemy_id' in body and 'level_id' in body
        if locacation_fields and id_fields and 'current_health' in body:
            return True
        else:
            return False
    else:
        return False


@app.route("/enemy-instances/", methods=['GET', 'POST'])
def all_enemies_instances():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if valid_body(body):
            enemy = Enemy.query.filter_by(id = int(body['enemy_id'])).first()
            level = Level.query.filter_by(id = int(body['level_id'])).first()
            if(enemy is not None and level is not None):
                enemy_instance = EnemyInstance(x_location = body['x_location'], 
                    y_location = body['y_location'], 
                    z_location = body['z_location'], 
                    current_health = body['current_health'],
                    enemy = enemy,
                    level = level
                )
                db.session.add(enemy_instance)
                db.session.commit()
                return gr.single_item(item = enemy_instance, created = True)
            else:
                return gr.bad_request()
        else:
            return gr.bad_request()
    
    elif request.method == 'GET':
        results = EnemyInstance.query.all()
        return gr.many_items(results)


@app.route("/enemy-instances/<id>", methods=['GET', 'PUT', 'DELETE'])
def one_enemy_instance(id):
    n_id = int(id)
    enemy_instance = EnemyInstance.query.filter_by(id = n_id).first()
    if enemy_instance is not None:
        if request.method == 'GET':
            return gr.single_item(item = enemy_instance)

        elif request.method == 'PUT':
            body = request.get_json(silent=True)
            
            if valid_body(body):
                enemy = Enemy.query.filter_by(id = int(body['enemy_id'])).first()
                level = Level.query.filter_by(id = int(body['level_id'])).first()
                if(enemy is not None and level is not None):
                    enemy_instance.x_location = body['x_location']
                    enemy_instance.y_location = body['y_location']
                    enemy_instance.z_location = body['z_location'] 
                    enemy_instance.current_health = body['current_health']
                    enemy_instance.enemy = enemy
                    enemy_instance.level = level
                    db.session.commit()
                    return gr.single_item(item = enemy_instance)
                else:
                    return gr.bad_request()
            else:
                return gr.bad_request()
        
        elif request.method == 'DELETE':
            db.session.delete(enemy_instance)
            db.session.commit()
            return gr.no_content()
    else:
        return gr.not_found()
