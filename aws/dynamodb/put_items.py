import os
from uuid import uuid4
import boto3

from models.hotel import Hotel
from models.room import Room

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb')
    hotel = Hotel(id = str(uuid4()), name = "Ben's Bed and Breakfast")
    rooms = [
        Room(id = str(uuid4()), floor = 1, room_number = 1, hotel_id = hotel.id),
        Room(id = str(uuid4()), floor = 1, room_number = 2, hotel_id = hotel.id),
        Room(id = str(uuid4()), floor = 1, room_number = 3, hotel_id = hotel.id),
        Room(id = str(uuid4()), floor = 1, room_number = 4, hotel_id = hotel.id)
    ]

    hotel_table = dynamodb.Table(Hotel.table_name())
    room_table = dynamodb.Table(Room.table_name())

    print('Writing Hotel {} to DynamoDB'.format(repr(hotel)))
    hotel_table.put_item(
        Item = hotel.to_dictionary()
    )

    with room_table.batch_writer() as batch:
        for room in rooms:
            print('Add Room {} to batch'.format(room))
            batch.put_item(
                Item = room.to_dictionary()
            )
    print('Batch write of rooms completed')

