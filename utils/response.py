def OK(message):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": message
    }


def NOT_FOUND(message):
    return {
        "statusCode": 404,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": message
    }


def BAD_REQUEST(message):
    return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": message
    }