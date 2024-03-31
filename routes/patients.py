from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Blueprint, jsonify, request
import logging
from errors import (
    INTERNAL_ERROR_GET_PATIENT_INFO, 
    INTERNAL_ERROR_ADD_PATIENT_INFO, 
    INTERNAL_ERROR_UPDATE_PATIENT_INFO,
    INTERNAL_ERROR_GET_PATIENT_HISTORY, 
    INTERNAL_ERROR_ADD_PATIENT_HISTORY, 
    INTERNAL_ERROR_UPDATE_PATIENT_HISTORY,
    INTERNAL_ERROR_GET_PATIENT_APPOINTMENT,
    INTERNAL_ERROR_ADD_PATIENT_APPOINTMENT,
    INTERNAL_ERROR_UPDATE_PATIENT_APPOINTMENT

)
from utils.patients import (
    get_patients_info, 
    add_new_patient, 
    update_patient_info, 
    get_patient_history, 
    add_patient_history, 
    update_patient_history,
    get_patient_appointment,
    add_patient_appointment,
    update_patient_appointment,
)

from api_scehams.patient_api_schema import PatientsInfoSchema, PatientsHistroyDetailsSchema, PatientSearchSchema

patients_blueprint = Blueprint("patients_blueprint", __name__)
CORS(patients_blueprint)
api = Api(patients_blueprint)

log = logging.getLogger(__name__)


class FetchAllPatientsInfo(Resource):
    def get(self, auth_payload=None):
        try:
            payload = PatientSearchSchema().load(request.args)
            result = get_patients_info(payload = payload, paginate=True)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while fetching patient data {}", error)
            return INTERNAL_ERROR_GET_PATIENT_INFO,500

class FetchPatientsInfo(Resource):
    def get(self, patient_id, auth_payload=None):

        try:            
            result = get_patients_info(patient_id = patient_id)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while searching a patient record with id {} : {}", patient_id, error)
            return INTERNAL_ERROR_GET_PATIENT_INFO,500

class AddPatientInfo(Resource):
    def post(self, auth_payload=None):
    
        try:
            payload = PatientsInfoSchema().load(request.get_json())
            add_new_patient(payload)
            return ('', 201)

        except Exception as error:
            log.error("Error occured while saving a new patient record {}", error)
            return INTERNAL_ERROR_ADD_PATIENT_INFO,500

class ModifyPatientInfo(Resource):

    def put(self, patient_id, auth_payload=None):
        
        try:
            payload = PatientsInfoSchema().load(request.get_json())
            update_patient_info(patient_id, payload)
            return '', 204
        except Exception as error:
            log.error("Error occured while updating a patient record with id {} : {}", patient_id, error)
            return INTERNAL_ERROR_UPDATE_PATIENT_INFO,500
        
    
 
class FetchPatientHistoy(Resource):
    def get(self, patient_id, auth_payload=None):

        try:            
            result = get_patient_history(patient_id)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while searching a patient history record with id {} : {}", patient_id, error)
            return INTERNAL_ERROR_GET_PATIENT_HISTORY,500

class AddPatientHistoy(Resource):

    def post(self, auth_payload=None):
        
        try:
            payload = PatientsHistroyDetailsSchema().load(request.get_json())
            add_patient_history(payload)
            return '', 201
        except Exception as error:
            log.error("Error occured while adding a new patient history record {}", error)
            return INTERNAL_ERROR_ADD_PATIENT_HISTORY,500

class ModifyPatientHistoy(Resource):

    def put(self, history_id, auth_payload=None):
        
        try:
            payload = PatientsHistroyDetailsSchema().load(request.get_json())
            update_patient_history(history_id, payload)
            return '', 204
        except Exception as error:
            log.error("Error occured while updating a patient history record with id {} : {}", history_id, error)
            return INTERNAL_ERROR_UPDATE_PATIENT_HISTORY,500    
    

class FetchPatientAppointment(Resource):
    def get(self, patient_id, auth_payload=None):

        try:            
            result = get_patient_appointment(patient_id)
            return jsonify(result)
        except Exception as error:
            log.error("Error occured while searching a patient appointment record with id {} : {}", patient_id, error)
            return INTERNAL_ERROR_GET_PATIENT_APPOINTMENT,500

class AddPatientAppointment(Resource):

    def post(self, auth_payload=None):
        
        try:
            payload = PatientsHistroyDetailsSchema().load(request.get_json())
            add_patient_appointment(payload)
            return '', 201
        except Exception as error:
            log.error("Error occured while adding a new patient appointment record {}", error)
            return INTERNAL_ERROR_ADD_PATIENT_APPOINTMENT,500

class ModifyPatientAppointment(Resource):

    def put(self, appointment_id, auth_payload=None):
        
        try:
            payload = PatientsHistroyDetailsSchema().load(request.get_json())
            update_patient_appointment(appointment_id, payload)
            return '', 204
        except Exception as error:
            log.error("Error occured while updating a patient appointment record with id {} : {}", appointment_id, error)
            return INTERNAL_ERROR_UPDATE_PATIENT_APPOINTMENT,500    
    



api.add_resource(AddPatientInfo, "/add-patient-info/")
api.add_resource(FetchAllPatientsInfo, "/fetch-patient-info/")
api.add_resource(FetchPatientsInfo, "/fetch-patient-info/<int:patient_id>/")
api.add_resource(ModifyPatientInfo, "/modify-patient-info/<int:patient_id>/")

api.add_resource(AddPatientHistoy, "/add-patient-history/")
api.add_resource(ModifyPatientHistoy, "/modify-patient-history/<int:history_id>/")
api.add_resource(FetchPatientHistoy, "/fetch-patient-history/<int:patient_id>/")

api.add_resource(AddPatientAppointment, "/add-patient-appointment/")
api.add_resource(ModifyPatientAppointment, "/modify-patient-appointment/<int:appointment_id>/")
api.add_resource(FetchPatientAppointment, "/fetch-patient-appointment/<int:patient_id>/")

