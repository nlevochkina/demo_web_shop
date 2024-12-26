add_product = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "updatetopcartsectionhtml": {"type": "string"},
        "updateflyoutcartsectionhtml": {"type": "string"},
    },
    "required": ["success", "message", "updatetopcartsectionhtml", "updateflyoutcartsectionhtml"]
}

add_to_wish_list = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "updatetopwishlistsectionhtml": {"type": "string"},
    },
    "required": ["success", "message"]
}

subscribe = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "Success": {"type": "boolean"},
        "Result": {"type": "string"},
    },
    "required": ["Success", "Result"]
}
