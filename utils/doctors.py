from db.db_schemas import doctors,departments,doctor_availabilty,upcoming_appointments,patients
from sqlalchemy.sql import select, update, insert

from db.db_utils import execute_query, paginate_query


def get_doctors_info(doctor_id=None, payload={}, paginate=False):
    
    select_list =  [doctors]+[departments.c.department_name, departments.c.services]    
    query = select(select_list).select_from(doctors)
    
    doctor_name = payload.get("doctor_name")
    doctor_specialization = payload.get("doctor_specialization")
    doctor_email = payload.get("doctor_email")
    doctor_phone = payload.get("doctor_phone")
    page_no = payload.get("page_no")
    page_size = payload.get("page_size")

    if doctor_id:
        query = query.where(doctors.c.id==doctor_id)
    if doctor_name:
        query = query.where(doctors.c.name.ilike(f"%{doctor_name}%"))
    if doctor_specialization:
        query = query.where(doctors.c.email.ilike(f"%{doctor_specialization}%"))
    if doctor_email:
        query = query.where(doctors.c.email.ilike(f"%{doctor_email}%"))
    if doctor_phone:
        query = query.where(doctors.c.phone.ilike(f"%{doctor_phone}%"))
    
    query = query.outerjoin(departments, doctors.c.department_id == departments.c.id)
    
    if paginate:
        query, count_query = paginate_query(query,page_no,page_size)
        total_rows = execute_query(count_query)
        total = total_rows[0]["count_1"] if total_rows else 0


        return {
            "data": execute_query(query),
            "total_rows": total,
            "page_size": page_size
        }
    return execute_query(query)

def add_new_doctor(payload):
    query = insert(doctors).values(**payload)
    execute_query(query)

def update_doctor_info(doctor_id, payload):
    query = update(doctors).values(**payload).where(doctors.c.id==doctor_id)
    execute_query(query)

def get_doctors_availability(doctor_id):
    select_list =  [doctor_availabilty]
    query = select(select_list).select_from(doctor_availabilty).where(doctor_availabilty.c.doctor_id==doctor_id)
    return execute_query(query)

def add_doctors_availability(payload):

    # Check if availability record is already there
    query = select([doctor_availabilty]).select_from(doctor_availabilty).where(doctor_availabilty.c.doctor_id==payload.get("doctor_id"))
    result = execute_query(query)
    if result !=[]:
        return
        
    query = insert(doctor_availabilty).values(**payload)
    execute_query(query)
def update_doctors_availability(doctor_id, payload):
    query = update(doctor_availabilty).values(**payload).where(doctor_availabilty.c.doctor_id==doctor_id)
    execute_query(query)

def get_assigned_patients(doctor_id):
    select_list = [upcoming_appointments.c.appointment_time, patients.c.name, patients.c.gender, patients.c.age, patients.c.email, patients.c.phone]
    query = select(select_list).select_from(upcoming_appointments)
    query = query.join(patients, patients.c.id == upcoming_appointments.c.patient_id)
    query = query.where(upcoming_appointments.c.doctor_id==doctor_id)
    return execute_query(query)

