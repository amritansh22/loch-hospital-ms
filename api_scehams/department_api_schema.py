from marshmallow import fields
from marshmallow import Schema

class DepartmentInfoSchema(Schema):
    department_name = fields.String()
    services = fields.List(fields.String())

class DepartmentSearchSchema(Schema):
    department_name = fields.String()
    department_services = fields.String()
    page_no = fields.Int()
    page_size = fields.Int()