

# Hospital Management Solution 

The server is hosted at https://loch-hospital-ms.onrender.com <br />
We can access it by using the appropriate API endpoints (dicussed further in [API Design section](https://github.com/amritansh22/loch-hospital-ms/new/main?filename=README.md#api-design))
<br />
<br />
## DB Design 
<img width="1136" alt="Screenshot 2024-03-31 at 3 05 15 PM" src="https://github.com/amritansh22/loch-hospital-ms/assets/29978031/f1e488e3-0d39-46a2-a0b5-823cb7fd3cd2">

We have created the following tables: 
  1. patients: stores information of the patients
  2. patient_history: stores diagnosis history of the patient
  3. upcoming_appointments: stores future scheduled visits of the paitent
  4. doctors: stores information of the doctors
  5. doctor_availabilty: stores doctor’s availabilty schedule
  6. departments: stores information of the departments in  the hospital. 

## API Design 

We have created API set for all major flows of the application. 
The complete list and their documentation can be found here: 
https://loch-hospital-ms.onrender.com/swagger/

We can also run the API from here. 

<img width="1724" alt="Screenshot 2024-03-31 at 4 05 47 PM" src="https://github.com/amritansh22/loch-hospital-ms/assets/29978031/aa0a41c2-cad2-4846-9242-aff5c617e5fc">



## Unit Test Cases 

We have written the unit test cases using the unittest library of python. 
To run the unit test cases, please give the command `python3 -m pytest` from the root directory of this application. 
<img width="851" alt="Screenshot 2024-03-31 at 4 05 28 PM" src="https://github.com/amritansh22/loch-hospital-ms/assets/29978031/921aa15d-8dd6-4b4c-b1a9-00f7e8d3fe77">


## Techincal Specifications

  1. Python and Flask used for the application
  2. PostgreSQL used for the DB
  3. SQLAlchemy used for the ORM
  4. Alembic used for the db migration
  5. Swagger used for API documentation
  6. Gunicorn used for production deployment
  7. Marshmallow used for serialization of the API payload

## Local usage

To run this application locally: 
  1. Clone this repo
  2. cd into the hospital_ms folder
  3. Give the command `gunicorn run:app` from the root of this repo
  4. Access the app at http://127.0.0.1:8000 (Port might change if 8000 is already in use)
