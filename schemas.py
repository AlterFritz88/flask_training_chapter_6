from marshmallow import Schema, fields


class LocationSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    code = fields.String()


class EventSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    date = fields.String()
    time = fields.String()
    type = fields.String()
    category = fields.String()
    location = fields.Nested("LocationSchema")
    seats = fields.Integer()
    address = fields.String()

