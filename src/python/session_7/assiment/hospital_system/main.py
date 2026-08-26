
from project import Hospital, Department
from add_department import add_department
from add_patient import add_patient
from add_staff import add_staff
from view_patient_record import view_patient_record
from view_staff_info import view_staff_info
from view_department import view_department

hospital = Hospital()

while True:
    print("\n===== Hospital System =====")
    print("1. Add Department")
    print("2. Add Patient")
    print("3. Add Staff")
    print("4. View Departments")
    print("5. View Patient Record")
    print("6. View Staff Information")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_department(hospital)

    elif choice in ["2", "3", "4", "5","6"]:
        if not hospital.departments:
            print("Please add a department first.")
            continue

        # print("\nAvailable Departments:")
        # for department in hospital.departments:
        #     print(department.name)
        if choice in ['2','3','5','6']:
            department_name = input("Enter department name: ")

            selected_department = None

            for department in hospital.departments:
                if department.name == department_name:
                    selected_department = department
                    break

            if selected_department is None:
                print("Department not found.")
                continue

        if choice == "2":
            add_patient(selected_department)

        elif choice == "3":
            add_staff(selected_department)

        elif choice == "4":
            view_department(hospital)
            
        elif choice == "5":
            view_patient_record(selected_department)

        elif choice == "6":
            view_staff_info(selected_department)

    elif choice == "7":
        print("Thank you for using Hospital System.")
        break

    else:
        print("Invalid choice. Please try again.")