# Notification Api

This template includes samples how to install the application and documentation about the endpoints.

First of all I am using  Python and Serverless Framework to build the application.

## Environment Information
Domain: https://7hbsmqn32h.execute-api.us-east-1.amazonaws.com


## Install

Setup your amazon credential in your credentials file [official documentation](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

```bash
Run the following command in root path
$ npm install
$ serverless deploy

Deploying notification-api to stage dev (us-east-1)

✔ Service deployed to stack notification-api-dev (170s)

```

## Accounts
I created the following accounts to test the application

```bash
{
    "users": [
        {
            "user_id": "U001",
            "name": "one",
            "email": "user_one@test.com",
            "phone_number": "111-11-1111",
            "categories": ["Sports", "Movies"],
            "notification_types": ["SMS", "E-Mail"]
        },
        {
            "user_id": "U002",
            "name": "two",
            "email": "user_two@test.com",
            "phone_number": "222-22-2222",
            "categories": ["Finance"],
            "notification_types": ["Push Notification"]
        }, 
        {
            "user_id": "U003",
            "name": "user_three",
            "email": "user_three@test.com",
            "phone_number": "333-33-3333",
            "categories": ["Finance","Movies"],
            "notification_types": ["SMS", "Push Notification"]
        }
    ]
}
'
```




### Get Categories
```bash
curl --location 'https://7hbsmqn32h.execute-api.us-east-1.amazonaws.com/category/list'

response
{
    "categories": [
        {
            "category_id": "C002",
            "name": "Finance"
        },
        {
            "category_id": "C001",
            "name": "Sports"
        },
        {
            "category_id": "C003",
            "name": "Movies"
        }
    ]
}
```

### Get logs list a notification

```bash
curl --location 'https://7hbsmqn32h.execute-api.us-east-1.amazonaws.com/log/list'

Response
{
    "logs": [
        {
            "id": "b351b655-0e5e-4106-8c9b-6adb5d38f012",
            "user_name": "one",
            "email": "user_one@test.com",
            "category": "Movies",
            "channel": "SMS",
            "message": "Hello World!",
            "create_at": "06/15/2023"
        }
    ]
}
```

### Create notification subscribers

```bash
curl --location 'https://7hbsmqn32h.execute-api.us-east-1.amazonaws.com/notification/subscribers' \
--header 'Content-Type: application/json' \
--data '{
    "category_id": "C003",
    "message": "Hey Hector"
}'

Response
{
    "logs": [
        {
            "id": "b351b655-0e5e-4106-8c9b-6adb5d38f012",
            "user_name": "one",
            "email": "user_one@test.com",
            "category": "Movies",
            "channel": "SMS",
            "message": "Hello World!",
            "create_at": "06/15/2023"
        }
    ]
}
```


## Unit test
```bash
Run the following command in root path
$ pytest tests --cov=src/

```


