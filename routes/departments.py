from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Blueprint, jsonify, request
import logging
from errors import INTERNAL_ERROR_GET_DEPARTMENT_INFO, INTERNAL_ERROR_ADD_DEPARTMENT_INFO, INTERNAL_ERROR_UPDATE_DEPARTMENT_INFO
from utils.department import get_department_info, add_new_department, update_department_info
from api_scehams.department_api_schema import DepartmentInfoSchema,  DepartmentSearchSchema

department_blueprint = Blueprint("department_blueprint", __name__)
CORS(department_blueprint)
api = Api(department_blueprint)

log = logging.getLogger(__name__)


class FetchAllDepartmentInfo(Resource):
    def get(self, auth_payload=None):
        
        try:
            payload = DepartmentSearchSchema().load(request.args)
            result = get_department_info(payload=payload, paginate=True)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while fetching department data {}", error)
            return INTERNAL_ERROR_GET_DEPARTMENT_INFO,500
class AddDepartmentInfo(Resource):
    def post(self, auth_payload=None):
    
        try:
            payload = DepartmentInfoSchema().load(request.get_json())
            add_new_department(payload)
            return ('',201)

        except Exception as error:
            log.error("Error occured while saving a new department record {}", error)
            return INTERNAL_ERROR_ADD_DEPARTMENT_INFO,500

class FetchDepartmentInfo(Resource):
    def get(self, department_id, auth_payload=None):

        try:
            result = get_department_info(department_id)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while searching a department record with id {} : {}", department_id, error)
            return INTERNAL_ERROR_GET_DEPARTMENT_INFO,500
class ModifyDepartmentInfo(Resource):
    def put(self, department_id, auth_payload=None):
        
        try:
            payload = DepartmentInfoSchema().load(request.get_json())
            update_department_info(department_id, payload)
            return ('', 204)
        except Exception as error:
            log.error("Error occured while updating a department record with id {} : {}", department_id, error)
            return INTERNAL_ERROR_UPDATE_DEPARTMENT_INFO,500
        
    
    
api.add_resource(FetchAllDepartmentInfo, "/fetch-department-info/")
api.add_resource(AddDepartmentInfo, "/add-department-info/")
api.add_resource(FetchDepartmentInfo, "/fetch-department-info/<int:department_id>")
api.add_resource(ModifyDepartmentInfo, "/modify-department-info/<int:department_id>")