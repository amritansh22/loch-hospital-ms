from db.db_schemas import departments
from sqlalchemy.sql import select, update, insert
from db.db_utils import execute_query, paginate_query

def get_department_info(department_id=None, payload = {}, paginate=False):

    page_no = payload.get("page_no")
    page_size = payload.get("page_size")

    query = select([departments]).select_from(departments)

    if department_id:
        query = query.where(departments.c.id==department_id)
    
    department_name = payload.get("department_name")
    department_services = payload.get("department_services")

    if department_name:
        query = query.where(departments.c.department_name.ilike(f"%{department_name}%"))
    if department_services:
        query = query.where(departments.c.services.ilike(f"%{department_services}%"))
    
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

def add_new_department(payload):
    query = insert(departments).values(**payload)
    execute_query(query)

def update_department_info(department_id, payload):
    query = update(departments).values(**payload).where(departments.c.id==department_id)
    execute_query(query)

