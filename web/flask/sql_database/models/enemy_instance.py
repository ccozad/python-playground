from database import db

class EnemyInstance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x_location = db.Column(db.Float)
    y_location = db.Column(db.Float)
    z_location = db.Column(db.Float)
    current_health = db.Column(db.Integer)

    enemy_id = db.Column(db.Integer, db.ForeignKey('enemy.id'),
        nullable=False)
    enemy = db.relationship('Enemy',
        backref=db.backref('instances', lazy=True))
    
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'),
        nullable=False)
    level = db.relationship('Level',
        backref=db.backref('enemies', lazy=True))

    def __repr__(self):
        return '<EnemyInstance {},{}>'.format(repr(self.enemy), repr(self.level))