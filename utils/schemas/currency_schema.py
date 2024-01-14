CURRENCY_SCHEMA={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "suggestions": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "value": {
              "type": "string"
            },
            "unrestricted_value": {
              "type": "string"
            },
            "data": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "string"
                },
                "strcode": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "country": {
                  "type": "string"
                }
              },
              "required": [
                "code",
                "strcode",
                "name",
                "country"
              ]
            }
          },
          "required": [
            "value",
            "unrestricted_value",
            "data"
          ]
        }
      ]
    }
  },
  "required": [
    "suggestions"
  ]
}