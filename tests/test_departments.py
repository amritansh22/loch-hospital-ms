import pytest
from flask import Flask
from unittest.mock import Mock

def test_get_all_department_info(monkeypatch):
    from routes.departments import FetchAllDepartmentInfo
    import routes.departments as Department
    FetchAllDepartmentInfo  = FetchAllDepartmentInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_department_info(*args, **kwargs):
            return { "data": [ { "department_name": "Radiology", "id": 1, "services": [ "MRI", "CT SCAN", "UltraSound" ] } ], "page_size": 20, "total_rows": 1 }

        monkeypatch.setattr(Department, "get_department_info", mock_get_department_info)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Department, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return {"page_no":0, "page_size":20}
        monkeypatch.setattr(Department.DepartmentSearchSchema, "load", mock_load_valid)

        response  = FetchAllDepartmentInfo.get()
        assert response.json == { "data": [ { "department_name": "Radiology", "id": 1, "services": [ "MRI", "CT SCAN", "UltraSound" ] } ], "page_size": 20, "total_rows": 1 }

def test_get_department_info(monkeypatch):
    from routes.departments import FetchDepartmentInfo
    import routes.departments as Department
    FetchDepartmentInfo  = FetchDepartmentInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_get_department_info(*args, **kwargs):
            return [ { "department_name": "Radiology", "id": 1, "services": [ "MRI", "CT SCAN", "UltraSound" ] } ]

        monkeypatch.setattr(Department, "get_department_info", mock_get_department_info)
        
        response  = FetchDepartmentInfo.get(department_id=1)
        assert response.json == [ { "department_name": "Radiology", "id": 1, "services": [ "MRI", "CT SCAN", "UltraSound" ] } ]

def test_post_department_info(monkeypatch):
    from routes.departments import AddDepartmentInfo
    import routes.departments as Department
    AddDepartmentInfo  = AddDepartmentInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_add_new_department(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Department, "add_new_department", mock_add_new_department)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Department, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return   { "name": "John Doe", "department_id": 1, "phone": "1292838392", "email": "dwa@lds.com", "specialization": "Ortho" }
        monkeypatch.setattr(Department.DepartmentInfoSchema, "load", mock_load_valid)

        response  = AddDepartmentInfo.post()
        assert response == ('',201)

def test_put_department_info(monkeypatch):
    from routes.departments import ModifyDepartmentInfo
    import routes.departments as Department
    ModifyDepartmentInfo  = ModifyDepartmentInfo()
    app = Flask(__name__)

    with app.app_context():

        def mock_update_department_info(*args, **kwargs):
            return Mock()

        monkeypatch.setattr(Department, "update_department_info", mock_update_department_info)


        mock_request = Mock()
        mock_get_json = Mock()
        mock_request = Mock()
        mock_request.get_json = mock_get_json
        monkeypatch.setattr(Department, "request", mock_request)
        def mock_load_valid(*args, **kwargs):
            return  { "department_name": "Radio" }
        monkeypatch.setattr(Department.DepartmentInfoSchema, "load", mock_load_valid)

        response  = ModifyDepartmentInfo.put(department_id=1)
        assert response == ('',204)