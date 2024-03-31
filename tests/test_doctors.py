import pytest
from flask import Flask
from unittest.mock import Mock

def test_get_all_doctors_info(monkeypatch):
    from routes.doctors import FetchAllDoctorsInfo
    import routes.doctors as Doctors
    FetchAllDoctorsInfo  = FetchAllDoctorsInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_doctors_info(*args, **kwargs):
            return { "data": [ { "department_id": 1, "department_name": "Radiology", "email": "dwa@lds.com", "id": 1, "name": "Shaymu", "phone": "1292838392", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "I may not know" }, { "department_id": 2, "department_name": None, "email": "swa@lds.com", "id": 3, "name": "PULLU", "phone": "3292838392", "services": None, "specialization": "U may not know" }, { "department_id": 1, "department_name": "Radiology", "email": "dwa@lds.com", "id": 4, "name": "Gullu", "phone": "1292838392", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "I may not know" }, { "department_id": 1, "department_name": "Radiology", "email": "user@example.com", "id": 5, "name": "John Doe", "phone": "+91 12345678", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "Cardiologist" }, { "department_id": 1, "department_name": "Radiology", "email": "user@example.com", "id": 6, "name": "John Doe", "phone": "+91 12345678", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "Cardiologist" }, { "department_id": 1, "department_name": "Radiology", "email": "user@example.com", "id": 2, "name": "John Doe", "phone": "+91 12345678", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "Pulmonologist" } ], "page_size": 20, "total_rows": 6 }

        monkeypatch.setattr(Doctors, "get_doctors_info", mock_get_doctors_info)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Doctors, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return {"page_no":0, "page_size":20}
        monkeypatch.setattr(Doctors.DoctorSearchSchema, "load", mock_load_valid)

        response  = FetchAllDoctorsInfo.get()
        assert response.json == { "data": [ { "department_id": 1, "department_name": "Radiology", "email": "dwa@lds.com", "id": 1, "name": "Shaymu", "phone": "1292838392", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "I may not know" }, { "department_id": 2, "department_name": None, "email": "swa@lds.com", "id": 3, "name": "PULLU", "phone": "3292838392", "services": None, "specialization": "U may not know" }, { "department_id": 1, "department_name": "Radiology", "email": "dwa@lds.com", "id": 4, "name": "Gullu", "phone": "1292838392", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "I may not know" }, { "department_id": 1, "department_name": "Radiology", "email": "user@example.com", "id": 5, "name": "John Doe", "phone": "+91 12345678", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "Cardiologist" }, { "department_id": 1, "department_name": "Radiology", "email": "user@example.com", "id": 6, "name": "John Doe", "phone": "+91 12345678", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "Cardiologist" }, { "department_id": 1, "department_name": "Radiology", "email": "user@example.com", "id": 2, "name": "John Doe", "phone": "+91 12345678", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "Pulmonologist" } ], "page_size": 20, "total_rows": 6 }

def test_get_doctor_info_by_id(monkeypatch):
    from routes.doctors import FetchDoctorInfo
    import routes.doctors as Doctors
    FetchDoctorInfo  = FetchDoctorInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_doctors_info(*args, **kwargs):
            return [ { "department_id": 1, "department_name": "Radiology", "email": "dwa@lds.com", "id": 1, "name": "Shaymu", "phone": "1292838392", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "I may not know" } ]

        monkeypatch.setattr(Doctors, "get_doctors_info", mock_get_doctors_info)
        
        response  = FetchDoctorInfo.get(doctor_id=1)
        assert response.json == [ { "department_id": 1, "department_name": "Radiology", "email": "dwa@lds.com", "id": 1, "name": "Shaymu", "phone": "1292838392", "services": [ "MRI", "CT SCAN", "UltraSound" ], "specialization": "I may not know" } ]

def test_post_doctor_info(monkeypatch):
    from routes.doctors import AddDocotrInfo
    import routes.doctors as Doctors
    AddDocotrInfo  = AddDocotrInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_add_new_doctor(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Doctors, "add_new_doctor", mock_add_new_doctor)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Doctors, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return   { "name": "John Doe", "department_id": 1, "phone": "1292838392", "email": "dwa@lds.com", "specialization": "Ortho" }
        monkeypatch.setattr(Doctors.DoctorsInfoSchema, "load", mock_load_valid)

        response  = AddDocotrInfo.post()
        assert response == ('',201)

def test_put_doctor_info(monkeypatch):
    from routes.doctors import ModifyDoctorInfo
    import routes.doctors as Doctors
    ModifyDoctorInfo  = ModifyDoctorInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_update_doctor_info(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Doctors, "update_doctor_info", mock_update_doctor_info)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Doctors, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return  { "name": "John Doe", "department_id": 1, "phone": "1292838392", "email": "dwa@lds.com", "specialization": "Ortho" }
        monkeypatch.setattr(Doctors.DoctorsInfoSchema, "load", mock_load_valid)

        response  = ModifyDoctorInfo.put(doctor_id=1)
        assert response == ('',204)


def test_get_doctors_availability(monkeypatch):
    from routes.doctors import FetchDoctorAvailability
    import routes.doctors as Doctors
    FetchDoctorAvailability  = FetchDoctorAvailability()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_doctors_availability(*args, **kwargs):
            return [ { "available_times": [ { "1": [ "1232", "12355" ] }, { "2": [ "23", "35" ] } ], "doctor_id": 2, "unavailabile_times": [ "123", "1234", "12345", "123456" ] } ]

        monkeypatch.setattr(Doctors, "get_doctors_availability", mock_get_doctors_availability)
        
        response  = FetchDoctorAvailability.get(doctor_id=1)
        assert response.json == [ { "available_times": [ { "1": [ "1232", "12355" ] }, { "2": [ "23", "35" ] } ], "doctor_id": 2, "unavailabile_times": [ "123", "1234", "12345", "123456" ] } ]

def test_post_doctors_availability(monkeypatch):
    from routes.doctors import AddDoctorAvailability
    import routes.doctors as Doctors
    AddDoctorAvailability  = AddDoctorAvailability()
    app = Flask(__name__)

    with app.app_context():

        def mock_add_doctors_availability(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Doctors, "add_doctors_availability", mock_add_doctors_availability)


        mock_request = Mock()
        mock_request = Mock()
        def mock_load_valid(*args, **kwargs):
            return   { "name": "John Doe", "department_id": 1, "phone": "1292838392", "email": "dwa@lds.com", "specialization": "Ortho" }
        mock_request.get_json = mock_load_valid
        monkeypatch.setattr(Doctors, "request", mock_request)

        response  = AddDoctorAvailability.post()
        assert response == ('',201)

def test_put_doctors_availability(monkeypatch):
    from routes.doctors import ModifyDoctorAvailability
    import routes.doctors as Doctors
    ModifyDoctorAvailability  = ModifyDoctorAvailability()
    app = Flask(__name__)

    with app.app_context():

        def mock_update_doctors_availability(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Doctors, "update_doctors_availability", mock_update_doctors_availability)


        mock_request = Mock()
        mock_request = Mock()
        def mock_load_valid(*args, **kwargs):
            return  { "name": "John Doe", "department_id": 1, "phone": "1292838392", "email": "dwa@lds.com", "specialization": "Ortho" }
        mock_request.get_json = mock_load_valid
        monkeypatch.setattr(Doctors, "request", mock_request)
        response  = ModifyDoctorAvailability.put(doctor_id=1)
        assert response == ('',204)


def test_get_assigned_patients(monkeypatch):
    from routes.doctors import FetchAssignedPatients
    import routes.doctors as Doctors
    FetchAssignedPatients  = FetchAssignedPatients()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_assigned_patients(*args, **kwargs):
            return [ { "age": 12, "appointment_time": 1000000.0, "email": "asdwds", "gender": "Male", "name": "AA", "phone": "+91 2378537853" } ]

        monkeypatch.setattr(Doctors, "get_assigned_patients", mock_get_assigned_patients)
        
        response  = FetchAssignedPatients.get(doctor_id=1)
        assert response.json == [ { "age": 12, "appointment_time": 1000000.0, "email": "asdwds", "gender": "Male", "name": "AA", "phone": "+91 2378537853" } ]
