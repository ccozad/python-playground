from database import db

class Enemy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    max_health = db.Column(db.Integer)

    def __repr__(self):
        return '<Enemy {}>'.format(repr(self.name))
    
    def to_dictionary(self):
        return {
            "_id": str(self.id),
            "name": self.name,
            "max_health": self.max_health
        }