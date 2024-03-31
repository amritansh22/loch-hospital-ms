
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


from app import db

class Patients(Base):
   __tablename__ = "patients"
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String())
   gender = db.Column(db.String())
   age = db.Column(db.Integer)
   email = db.Column(db.String(100))
   phone = db.Column(db.String(15))
patients = Patients.__table__

class Doctors(Base):

   __tablename__ = "doctors"
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String())
   specialization = db.Column(db.String())
   email = db.Column(db.String(100))
   phone = db.Column(db.String(15))
   department_id = db.Column(db.Integer)

doctors = Doctors.__table__

class DoctorAvailabilty(Base):
   __tablename__ = "doctor_availabilty"
   doctor_id = db.Column(db.Integer, primary_key=True)
   available_times = db.Column(JSONB)
   unavailabile_times = db.Column(JSONB)
   
doctor_availabilty = DoctorAvailabilty.__table__


class Departments(Base):
   __tablename__ = "departments"
   id = db.Column(db.Integer, primary_key = True)
   department_name = db.Column(db.String())
   services = db.Column(JSONB)
departments = Departments.__table__

class PatientHistory(Base):
   __tablename__ = "patient_history"
   id = db.Column(db.Integer, primary_key = True)
   patient_id = db.Column(db.Integer)
   doctor_id = db.Column(db.Integer)
   appointment_time = db.Column(db.Float)
   diagnosis = db.Column(db.String())
   allergies = db.Column(db.ARRAY(db.String))
   medications = db.Column(db.ARRAY(db.String))
patient_history = PatientHistory.__table__

class UpcomingAppointments(Base):
   __tablename__ = "upcoming_appointments"
   id = db.Column(db.Integer, primary_key = True)
   patient_id = db.Column(db.Integer)
   doctor_id = db.Column(db.Integer)
   appointment_time = db.Column(db.Float)
upcoming_appointments = UpcomingAppointments.__table__