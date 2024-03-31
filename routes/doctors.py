from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Blueprint, jsonify, request
import logging
from errors import INTERNAL_ERROR_GET_DOCTOR_INFO, INTERNAL_ERROR_ADD_DOCTOR_INFO, INTERNAL_ERROR_UPDATE_DOCTOR_INFO, INTERNAL_ERROR_GET_DOCTOR_AVAILABILITY, INTERNAL_ERROR_GET_PATIENTS_ASSIGNED, INTERNAL_ERROR_GET_DOCTOR_AVAILABILITY, INTERNAL_ERROR_ADD_DOCTOR_AVAILABILITY, INTERNAL_ERROR_UPDATE_DOCTOR_AVAILABILITY
from utils.doctors import get_doctors_info, add_new_doctor, update_doctor_info, get_doctors_availability, add_doctors_availability, update_doctors_availability, get_assigned_patients
from api_scehams.doctor_api_schema import DoctorsInfoSchema, DoctorSearchSchema


doctors_blueprint = Blueprint("doctors_blueprint", __name__)
CORS(doctors_blueprint)
api = Api(doctors_blueprint)

log = logging.getLogger(__name__)



class FetchAllDoctorsInfo(Resource):
    def get(self, auth_payload=None):
        try:
            payload = DoctorSearchSchema().load(request.args)
            result = get_doctors_info(payload=payload, paginate=True)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while fetching doctors data {}", error)
            return INTERNAL_ERROR_GET_DOCTOR_INFO,500

class AddDocotrInfo(Resource):
    def post(self, auth_payload=None):
    
        try:
            payload = DoctorsInfoSchema().load(request.get_json())
            add_new_doctor(payload)
            return ("", 201)

        except Exception as error:
            log.error("Error occured while saving a new doctors record {}", error)
            return INTERNAL_ERROR_ADD_DOCTOR_INFO,500

class FetchDoctorInfo(Resource):
    def get(self, doctor_id, auth_payload=None):

        try:
            result = get_doctors_info(doctor_id)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while searching a doctors record with id {} : {}", doctor_id, error)
            return INTERNAL_ERROR_GET_DOCTOR_INFO,500

class ModifyDoctorInfo(Resource):
    def put(self, doctor_id, auth_payload=None):
        
        try:
            payload = DoctorsInfoSchema().load(request.get_json())
            update_doctor_info(doctor_id, payload)
            return ('',204)
        except Exception as error:
            log.error("Error occured while updating a doctors record with id {} : {}", doctor_id, error)
            return INTERNAL_ERROR_UPDATE_DOCTOR_INFO,500
        

class FetchDoctorAvailability(Resource):
    def get(self, doctor_id, auth_payload=None):

        try:
            result = get_doctors_availability(doctor_id)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while fetching doctors availability record with id {} : {}", doctor_id, error)
            return INTERNAL_ERROR_GET_DOCTOR_AVAILABILITY,500  

class AddDoctorAvailability(Resource):
    def post(self, auth_payload=None):
    
        try:
            payload = request.get_json()
            add_doctors_availability(payload)
            return ('',201)

        except Exception as error:
            log.error("Error occured while saving a new doctors availability record {}", error)
            return INTERNAL_ERROR_GET_DOCTOR_AVAILABILITY,500
class ModifyDoctorAvailability(Resource):
    def put(self, doctor_id, auth_payload=None):
        
        try:
            payload = request.get_json()
            update_doctors_availability(doctor_id, payload)
            return ('',204)
        except Exception as error:
            log.error("Error occured while updating doctors availability record with id {} : {}", doctor_id, error)
            return INTERNAL_ERROR_UPDATE_DOCTOR_AVAILABILITY,500
    
class FetchAssignedPatients(Resource):
    def get(self, doctor_id, auth_payload=None):

        try:
            result = get_assigned_patients(doctor_id)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while fetching patients assigned to doctors with id {} : {}", doctor_id, error)
            return INTERNAL_ERROR_GET_PATIENTS_ASSIGNED,500  

api.add_resource(FetchAllDoctorsInfo, "/fetch-doctor-info/")
api.add_resource(AddDocotrInfo, "/add-doctor-info/")
api.add_resource(FetchDoctorInfo, "/fetch-doctor-info/<int:doctor_id>")
api.add_resource(ModifyDoctorInfo, "/modify-doctor-info/<int:doctor_id>")

api.add_resource(AddDoctorAvailability, "/add-doctor-availability/")
api.add_resource(FetchDoctorAvailability, "/fetch-doctor-availability/<int:doctor_id>")
api.add_resource(ModifyDoctorAvailability, "/modify-doctor-availability/<int:doctor_id>")

api.add_resource(FetchAssignedPatients, "/fetch-assigned-patients/<int:doctor_id>")