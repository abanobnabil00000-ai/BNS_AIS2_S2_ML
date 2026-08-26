from project import Patient

def add_patient(department):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    phone = int(input("Enter patient phone: "))
    ID = input("ID: ")
    ailment = input("ailment: ")
    medical_record = input("Enter medical record: ")
    patient = Patient(name, age, phone ,ID,ailment,medical_record)

    department.add_patient(patient)
    
    

def __init__(self, name, age, phone, ID, ailment, medical_record):
        super().__init__(name, age,phone)
        self.medical_record = medical_record
        self.ID = ID
        self.ailment = ailment
