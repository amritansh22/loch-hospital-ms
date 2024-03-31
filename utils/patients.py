from db.db_schemas import patients,patient_history,upcoming_appointments
from sqlalchemy.sql import select, update, insert
from db.db_utils import execute_query, paginate_query



def get_patients_info(patient_id=None, payload={}, paginate=False):

    patient_name = payload.get("patient_name")
    patient_email = payload.get("patient_email")
    patient_phone = payload.get("patient_phone")
    page_no = payload.get("page_no")
    page_size = payload.get("page_size")

    query = select([patients]).select_from(patients)

    if patient_id:
        query = query.where(patients.c.id==patient_id)
    
    if patient_name:
        query = query.where(patients.c.name.ilike(f"%{patient_name}%"))
    if patient_email:
        query = query.where(patients.c.email.ilike(f"%{patient_email}%"))
    if patient_phone:
        query = query.where(patients.c.phone.ilike(f"%{patient_phone}%"))

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

def add_new_patient(payload):
    
    query = insert(patients).values(**payload)
    execute_query(query)

def update_patient_info(patient_id, payload):
    query = update(patients).values(**payload).where(patients.c.id==patient_id)
    execute_query(query)



def get_patient_history(patient_id):
    query = select([patient_history]).select_from(patient_history)
    query = query.where(patient_history.c.patient_id==patient_id)
    return execute_query(query)

def add_patient_history(payload):
    query = insert(patient_history).values(**payload)
    execute_query(query)

def update_patient_history(history_id, payload):
    query = update(patient_history).values(**payload).where(patient_history.c.patient_id == history_id)
    execute_query(query)



def get_patient_appointment(patient_id):
    query = select([upcoming_appointments]).select_from(upcoming_appointments)
    query = query.where(upcoming_appointments.c.patient_id==patient_id)

    return execute_query(query)

def add_patient_appointment(payload):
    query = insert(upcoming_appointments).values(**payload)
    execute_query(query)

def update_patient_appointment(appointment_id, payload):
    query = update(upcoming_appointments).values(**payload).where(upcoming_appointments.c.id == appointment_id)
    execute_query(query)
