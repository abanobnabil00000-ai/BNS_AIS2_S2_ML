
def view_department(hospital):
    print("\nAvailable Departments:")
    for department in hospital.departments:
        print(department.name)