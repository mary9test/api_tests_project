METRO_SCHEMA = {
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
                "city_kladr_id": {
                  "type": "string"
                },
                "city_fias_id": {
                  "type": "string"
                },
                "city": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "line_id": {
                  "type": "string"
                },
                "line_name": {
                  "type": "string"
                },
                "geo_lat": {
                  "type": "number"
                },
                "geo_lon": {
                  "type": "number"
                },
                "color": {
                  "type": "string"
                },
                "is_closed": {
                  "type": "boolean"
                }
              },
              "required": [
                "city_kladr_id",
                "city_fias_id",
                "city",
                "name",
                "line_id",
                "line_name",
                "geo_lat",
                "geo_lon",
                "color"
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