import os
import boto3

from models.hotel import Hotel
from models.room import Room

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb')
    entities = [Hotel, Room]

    for entity in entities:
        print('Creating table {}...'.format(entity.table_name()))
        dynamodb.create_table(
            TableName = entity.table_name(),
            KeySchema = entity.key_schema(),
            AttributeDefinitions = entity.key_attributes(),
            ProvisionedThroughput = {
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
    
    print('All tables created')

