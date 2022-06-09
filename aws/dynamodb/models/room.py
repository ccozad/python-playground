from abstract_entity import AbstractEntity

class Room(AbstractEntity):
    def __init__(self, id, floor, room_number, hotel_id):
        self.id = id
        self.floor = floor
        self.room_number = room_number
        self.hotel_id = hotel_id

    def __repr__(self):
        return "Room(id='{}', floor={}, room_number={}, hotel_id={})".format(self.id, self.floor, self.room_number, self.hotel_id)
    
    def to_dictionary(self):
        return {
            "id": str(self.id),
            "floor": self.floor,
            "room_number": self.room_number,
            "hotel_id": self.hotel_id
        }
    
    @staticmethod
    def table_name():
        return 'aws_lab.Rooms'
    
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