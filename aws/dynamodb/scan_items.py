import os
from uuid import uuid4
import boto3

from models.hotel import Hotel
from models.room import Room

if __name__ == "__main__":
    #session = boto3.session.Session()
    #dynamoDBClient = session.client('dynamodb')

    dynamodb = boto3.resource('dynamodb')
    hotel_table = dynamodb.Table(Hotel.table_name())
    room_table = dynamodb.Table(Room.table_name())

    print('{} table contents:'.format(Hotel.table_name()))

    response = hotel_table.scan()
    for item in response['Items']:
        print(' - {}'.format(item))
    
    print('{} table contents:'.format(Room.table_name()))

    response = room_table.scan()
    for item in response['Items']:
        print(' - {}'.format(item))