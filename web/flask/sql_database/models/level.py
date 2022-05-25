from database import db

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Level {}>'.format(repr(self.name))
    
    def to_dictionary(self):
        return {
            "_id": str(self.id),
            "name": self.name
        }