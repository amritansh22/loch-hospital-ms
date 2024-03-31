from marshmallow import fields
from marshmallow import Schema

class DoctorsInfoSchema(Schema):
    name = fields.String(allow_none=True)
    specialization = fields.String(allow_none=True)
    email = fields.String(allow_none=True)
    phone = fields.String(allow_none=True)
    department_id = fields.Int(allow_none=True)

class DoctorSearchSchema(Schema):
    doctor_name = fields.String()
    doctor_email = fields.String()
    doctor_phone = fields.String()
    doctor_specialization = fields.String()
    page_no = fields.Int()
    page_size = fields.Int()
