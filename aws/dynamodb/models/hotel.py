from abstract_entity import AbstractEntity

class Hotel(AbstractEntity):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Hotel(id='{}', name='{}')>".format(self.id, self.name)
    
    def to_dictionary(self):
        return {
            "id": str(self.id),
            "name": self.name
        }
    
    @staticmethod
    def table_name():
        return 'aws_lab.Hotels'
    
    @staticmethod
    def key_schema():
        return [
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ]
    
    @staticmethod
    def key_attributes():
        return [
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ]