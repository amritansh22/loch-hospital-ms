import pytest
from flask import Flask
from unittest.mock import Mock

def test_get_all_patient_info(monkeypatch):
    from routes.patients import FetchAllPatientsInfo
    import routes.patients as Patients
    FetchAllPatientsInfo  = FetchAllPatientsInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_patients_info(*args, **kwargs):
            return [{ "data": [ { "age": None, "email": "user@example.com", "gender": "string", "id": 3, "name": None, "phone": None }, { "age": 40, "email": "user@example.com", "gender": "Male", "id": 4, "name": "John Doe", "phone": None }, { "age": 40, "email": "user@example.com", "gender": "Male", "id": 5, "name": "John Doe", "phone": "+91 12345678" }, { "age": 40, "email": "user@example.com", "gender": "Male", "id": 6, "name": "John Doe", "phone": "+91 12345678" }, { "age": 40, "email": "user@example.com", "gender": "Male", "id": 1, "name": "John Doe", "phone": "+91 12345678" }, { "age": 30, "email": "user@example.com", "gender": "Female", "id": 2, "name": "Doe John", "phone": "+91 8765432" }, { "age": 40, "email": "user@example.com", "gender": "Male", "id": 7, "name": "John Doe", "phone": "+91 12345678" } ], "page_size": 20, "total_rows": 7 }]

        monkeypatch.setattr(Patients, "get_patients_info", mock_get_patients_info)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Patients, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return {"page_no":0, "page_size":20}
        monkeypatch.setattr(Patients.PatientSearchSchema, "load", mock_load_valid)

        response  = FetchAllPatientsInfo.get()
        assert response.json == [{'data': [{'age': None, 'email': 'user@example.com', 'gender': 'string', 'id': 3, 'name': None, 'phone': None}, {'age': 40, 'email': 'user@example.com', 'gender': 'Male', 'id': 4, 'name': 'John Doe', 'phone': None}, {'age': 40, 'email': 'user@example.com', 'gender': 'Male', 'id': 5, 'name': 'John Doe', 'phone': '+91 12345678'}, {'age': 40, 'email': 'user@example.com', 'gender': 'Male', 'id': 6, 'name': 'John Doe', 'phone': '+91 12345678'}, {'age': 40, 'email': 'user@example.com', 'gender': 'Male', 'id': 1, 'name': 'John Doe', 'phone': '+91 12345678'}, {'age': 30, 'email': 'user@example.com', 'gender': 'Female', 'id': 2, 'name': 'Doe John', 'phone': '+91 8765432'}, {'age': 40, 'email': 'user@example.com', 'gender': 'Male', 'id': 7, 'name': 'John Doe', 'phone': '+91 12345678'}], 'page_size': 20, 'total_rows': 7}]

def test_get_patient_info_by_id(monkeypatch):
    from routes.patients import FetchPatientsInfo
    import routes.patients as Patients
    FetchPatientsInfo  = FetchPatientsInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_patients_info(*args, **kwargs):
            return [ { "age": 40, "email": "user@example.com", "gender": "Male", "id": 1, "name": "John Doe", "phone": "+91 12345678" } ]

        monkeypatch.setattr(Patients, "get_patients_info", mock_get_patients_info)
        
        response  = FetchPatientsInfo.get(patient_id=1)
        assert response.json == [ { "age": 40, "email": "user@example.com", "gender": "Male", "id": 1, "name": "John Doe", "phone": "+91 12345678" } ]

def test_post_patient_info(monkeypatch):
    from routes.patients import AddPatientInfo
    import routes.patients as Patients
    AddPatientInfo  = AddPatientInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_add_new_patient(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Patients, "add_new_patient", mock_add_new_patient)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Patients, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return  { "age": 12, "email": "asdwds", "gender": "Male", "name": "ABC", "phone": "+91 2378537853" }
        monkeypatch.setattr(Patients.PatientsInfoSchema, "load", mock_load_valid)

        response  = AddPatientInfo.post()
        assert response == ('',201)

def test_put_patient_info(monkeypatch):
    from routes.patients import ModifyPatientInfo
    import routes.patients as Patients
    ModifyPatientInfo  = ModifyPatientInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_update_patient_info(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Patients, "update_patient_info", mock_update_patient_info)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Patients, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return   { "age": 12, "email": "csasc", "dscdc":231 }
        monkeypatch.setattr(Patients.PatientsInfoSchema, "load", mock_load_valid)

        response  = ModifyPatientInfo.put(patient_id=1)
        assert response == ('',204)


def test_get_patient_history_by_id(monkeypatch):
    from routes.patients import FetchPatientHistoy
    import routes.patients as Patients
    FetchPatientHistoy  = FetchPatientHistoy()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_patient_history(*args, **kwargs):
            return [ { "allergies": None, "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 1, "medications": None }, { "allergies": [ "None I could find", "you may" ], "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 2, "medications": None }, { "allergies": [], "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 3, "medications": None }, { "allergies": None, "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 4, "medications": None }, { "allergies": [ "None I could find", "you may" ], "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 5, "medications": [ " find", "you " ] } ]

        monkeypatch.setattr(Patients, "get_patient_history", mock_get_patient_history)
        
        response  = FetchPatientHistoy.get(patient_id=1)
        assert response.json == [ { "allergies": None, "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 1, "medications": None }, { "allergies": [ "None I could find", "you may" ], "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 2, "medications": None }, { "allergies": [], "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 3, "medications": None }, { "allergies": None, "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 4, "medications": None }, { "allergies": [ "None I could find", "you may" ], "appointment_time": 1292838392.0, "diagnosis": "Dudes rocking", "doctor_id": 1, "id": 5, "medications": [ " find", "you " ] } ]

def test_post_patient_history(monkeypatch):
    from routes.patients import AddPatientHistoy
    import routes.patients as Patients
    AddPatientHistoy  = AddPatientHistoy()
    app = Flask(__name__)

    with app.app_context():

        def mock_add_patient_history(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Patients, "add_patient_history", mock_add_patient_history)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Patients, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return   { "doctor_id": 1, "patient_id": 1, "appointment_time": 1292838392, "diagnosis": "Dudes rocking", "allergies": ["None I could find", "you may"], "medications": [" find", "you "] }
        monkeypatch.setattr(Patients.PatientsHistroyDetailsSchema, "load", mock_load_valid)

        response  = AddPatientHistoy.post()
        assert response == ('',201)

def test_put_patient_history(monkeypatch):
    from routes.patients import ModifyPatientHistoy
    import routes.patients as Patients
    ModifyPatientHistoy  = ModifyPatientHistoy()
    app = Flask(__name__)

    with app.app_context():

        def mock_update_patient_history(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Patients, "update_patient_history", mock_update_patient_history)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Patients, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return    { "doctor_id": 1, "patient_id": 1000, "appointment_time": 1292838392, "diagnosis": "Dudes rocking", "allergies": ["None I could find", "you may"], "medications": [" find", "you "] }
        monkeypatch.setattr(Patients.PatientsHistroyDetailsSchema, "load", mock_load_valid)

        response  = ModifyPatientHistoy.put(history_id=1)
        assert response == ('',204)




def test_get_patient_appointment(monkeypatch):
    from routes.patients import FetchPatientAppointment
    import routes.patients as Patients
    FetchPatientAppointment  = FetchPatientAppointment()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_patient_appointment(*args, **kwargs):
            return [ { "appointment_time": 1292838392, "doctor_id": 1, "id": 1 } ]

        monkeypatch.setattr(Patients, "get_patient_appointment", mock_get_patient_appointment)
        
        response  = FetchPatientAppointment.get(patient_id=1)
        assert response.json == [ { "appointment_time": 1292838392, "doctor_id": 1, "id": 1 } ]

def test_post_patient_appointment(monkeypatch):
    from routes.patients import AddPatientAppointment
    import routes.patients as Patients
    AddPatientAppointment  = AddPatientAppointment()
    app = Flask(__name__)

    with app.app_context():

        def mock_add_patient_appointment(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Patients, "add_patient_appointment", mock_add_patient_appointment)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Patients, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return    { "doctor_id": 1, "patient_id": 1, "appointment_time": 1292838392 }
        monkeypatch.setattr(Patients.PatientsHistroyDetailsSchema, "load", mock_load_valid)

        response  = AddPatientAppointment.post()
        assert response == ('',201)

def test_put_patient_appointment(monkeypatch):
    from routes.patients import ModifyPatientAppointment
    import routes.patients as Patients
    ModifyPatientAppointment  = ModifyPatientAppointment()
    app = Flask(__name__)

    with app.app_context():

        def mock_update_patient_appointment(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Patients, "update_patient_appointment", mock_update_patient_appointment)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Patients, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return     { "doctor_id": 1, "patient_id": 1, "appointment_time": 1292838392 }
        monkeypatch.setattr(Patients.PatientsHistroyDetailsSchema, "load", mock_load_valid)

        response  = ModifyPatientAppointment.put(appointment_id=1)
        assert response == ('',204)
