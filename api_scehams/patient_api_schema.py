from marshmallow import fields
from marshmallow import Schema

class PatientsInfoSchema(Schema):
    name = fields.String(allow_none=True)
    gender = fields.String(allow_none=True)
    age = fields.Int(allow_none=True)
    email = fields.String(allow_none=True)
    phone = fields.String(allow_none=True)

class PatientsHistroyDetailsSchema(Schema):
    patient_id = fields.Int(allow_none=True)
    doctor_id = fields.Int(allow_none=True)
    appointment_time = fields.Float(allow_none=True)
    diagnosis = fields.String(allow_none=True)
    allergies = fields.List(fields.String(allow_none=True))
    medications = fields.List(fields.String(allow_none=True))

class PatientsAppointmentSchema(Schema):
    patient_id = fields.Int(allow_none=True)
    doctor_id = fields.Int(allow_none=True)
    appointment_time = fields.Float(allow_none=True)

class PatientSearchSchema(Schema):
    patient_name = fields.String()
    patient_email = fields.String()
    patient_phone = fields.String()
    page_no = fields.Int()
    page_size = fields.Int()
