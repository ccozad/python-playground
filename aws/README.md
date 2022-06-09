# Introduction

All of the interactions with AWS services require an AWS account.

# Credentials Setup

AWS credentials must be configured before cals to the AWS APIs will work. You should create a user and assign that user to a group with the appropriate access permissions in AWS. Then local credentials need to be setup as described in https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

# Services

 - [Dynamodb](/aws/dynamodb/) fully managed NoSQL database service
   - [Create tables](/aws/dynamodb/create_tables.py) 
   - [List tables](/aws/dynamodb/list_tables.py) 
   - [Put items](/aws/dynamodb/put_items.py)
   - [Scan items](/aws/dynamodb/scan_items.py)

**[Back to start](https://github.com/ccozad/python-playground)**