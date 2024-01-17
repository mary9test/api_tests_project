ERROR_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "family": {
            "type": "string"
        },
        "reason": {
            "type": "string"
        },
        "message": {
            "type": "string"
        }
    },
    "required": [
        "family",
        "reason",
        "message"
    ]
}
