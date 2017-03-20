source_schema = {
    "type": "object",
    "properties": {
        "AWS_ACCESS_KEY": {
            "type": "string"
        },
        "AWS_SECRET_KEY": {
            "type": "string"
        }
    },
    "required": [
        "AWS_ACCESS_KEY",
        "AWS_SECRET_KEY"
    ]
}

version_schema = {
    "oneOf": [{
        "type": "object",
        "properties": {
            "schema": {
                "type": "string"
            }
        }
    }, {
        "type": "null"
    }]
}

check_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "source": source_schema,
        "version": version_schema
    },
    "required": [
        "source"
    ]
}

out_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "source": source_schema,
        "params": {
            "type": "object",
                "properties": {
                    "version": {
                        "type": "string"
                    },
                    "bucket": {
                        "type": "string"
                    },
                    "directory": {
                        "type": "string"
                    },
                    "step": {
                        "type": "string"
                    },
                },
                "required": [
                  "version",
                  "bucket",
                  "directory"
                ]
        }
    },
    "required": [
        "source",
        "params"
    ]
}

in_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "source": source_schema,
        "version": version_schema
    },
    "required": [
        "source",
        "version"
    ]
}