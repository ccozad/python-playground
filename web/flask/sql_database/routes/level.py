from tkinter import N
from app import app
from database import db
from models.level import Level
from common.generic_response import GenericResponse as gr

from flask import request

def valid_body(body):
    if body is not None:
        if 'name' in body:
            return True
        else:
            return False
    else:
        return False

@app.route("/levels/", methods=['GET', 'POST'])
def all_levels():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if valid_body(body):
            level = Level(name = body['name'])
            db.session.add(level)
            db.session.commit()
            return gr.single_item(item = level, created = True)
        else:
            return gr.bad_request()
    
    elif request.method == 'GET':
        results = Level.query.all()
        return gr.many_items(results)

@app.route("/levels/<id>/enemies/", methods=['GET'])
def all_enemies_for_level(id):
    n_id = int(id)
    level = Level.query.filter_by(id = n_id).first()
    if level is not None:
        if request.method == 'GET':
            return gr.many_items(level.enemies)
    else:
        return gr.not_found()

@app.route("/levels/<id>", methods=['GET', 'PUT', 'DELETE'])
def one_level(id):
    n_id = int(id)
    level = Level.query.filter_by(id = n_id).first()
    if level is not None:
        if request.method == 'GET':
            return gr.single_item(item = level)
        
        elif request.method == 'PUT':
            body = request.get_json(silent=True)
            if valid_body(body):
                level.name = body['name']
                db.session.commit()
                return gr.single_item(item = level)
            else:
                return gr.bad_request()
        
        elif request.method == 'DELETE':
            db.session.delete(level)
            db.session.commit()
            return gr.no_content()
    else:
        return gr.not_found()
    

    
