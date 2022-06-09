import os
import boto3

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb')

    for table in dynamodb.tables.all():
        print( ' - {}'.format(table.name))