
# Encapsulation: Base class Staff with private attributes and public methods
class Staff:
    def __init__(self, staff_id, name, age, gender, role):
        # private attributes
        self.staff_id = staff_id
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role
# Public Methods
    def display_info(self):
        print(f"Staff ID: {self.staff_id}")
        print(f"Name: {self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")
        print(f"Role: {self.role}")

# Inheritance: Doctor and Nurse classes inherit from Staff
class Doctor(Staff):
    def __init__(self, staff_id, name, age, gender, speciality):
        super().__init__(staff_id, name, age, gender,role="Doctor")
        self.speciality = speciality
        self.assigned_nurses = {}  # Dictionary to hold nurses assigned to patients
        # self.treat_patient = {}

# Abstraction: Assigning a nurse to a patient and ward, simplified for user
    def assign_nurse(self, nurse, patient, ward):
        self.assigned_nurses[patient.patient_id] = (nurse, ward)
        print(f"Nurse {nurse.name} assigned to Patient {patient.name} in Ward {ward}.")

    # def treat_patient(self, doctor, patient):
        # print(f"Doctor {doctor.name} is treating patient {patient.name}.")

    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.speciality}")

# Polymorphism: Method for viewing appointments is unique to doctors
    def view_appointments(self, appointments):
        print("\n--- DOCTOR'S APPOINTMENT ---")
        for appointment in appointments:
            if appointment.doctor == self:
                appointment.display_info()

# Polymorphism: Method for adding a diagnosis is unique to doctors
    def diagnose(self, appointment, diagnosis):
        appointment.diagnosis = diagnosis
        print(f"Diagnosis: '{diagnosis}' added to appointment for Patient {appointment.patient.name}.")



class Nurse(Staff):
    def __init__(self, staff_id, name,age, gender):
        super().__init__(staff_id, name, age, gender, role="Nurse")

    # def treat_patient(self,patient):
       # return f"{self.name} is assisting in the treatment of patient {patient.name}"

    def display_info(self):
        super().display_info()


class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display_info(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")


class Appointment:
    def __init__(self, appointment_id, patient, doctor, date):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.diagnosis = None

    def display_info(self):
        print(f"Appointment ID: {self.appointment_id}")
        print("Patient Info:")
        self.patient.display_info()
        print("Doctor Info:")
        self.doctor.display_info()
        print(f"Date: {self.date}")
        print(f"Diagnosis: {self.diagnosis if self.diagnosis else 'Pending'}")


class Billing:
    def __init__(self, billing_id, patient, amount):
        self.billing_id = billing_id
        self.patient = patient
        self.amount = amount

    def display_info(self):
        print(f"Billing ID: {self.billing_id}")
        print("Patient Info:")
        self.patient.display_info()
        print(f"Amount Due: Ugx{self.amount:.2f}")


# Functions to add user inputs
def add_patient():
    print("ENTER PATIENT DETAILS:")
    patient_id = int(input("Patient ID: "))
    name = str(input("Name: "))
    age = int(input("Age: "))
    disease = str(input("Disease: "))
    return Patient(patient_id, name, age, disease)


def add_doctor():
    print("ENTER DOCTORS DETAILS:")
    staff_id = int(input("Doctor ID: "))
    name = str(input("Name: "))
    age = int(input("Age:"))
    gender = str(input("Gender:"))
    speciality = str(input("Specialization: "))
    return Doctor(staff_id, name, age, gender, speciality)


def add_nurse():
    print("ENTER NURSE DETAILS:")
    staff_id = int(input("Nurse ID: "))
    name = str(input("Name: "))
    age = int(input("Age:"))
    gender = str(input("Gender:"))
    return Nurse(staff_id, name, age, gender)


def book_appointment(patient, doctor):
    appointment_id = int(input("Appointment ID: "))
    date = input("Date (YYYY-MM-DD): ")
    return Appointment(appointment_id, patient, doctor, date)


# Main function to demonstrate the system's functionalities
def main():
    # Instantiate doctor and nurse
    doctor = add_doctor()
    nurse = add_nurse()

    # Add a patient through user input
    patient = add_patient()

    # Doctor assigns nurse to patient in a specified ward
    ward = str(input("Enter ward for the patient: "))
    doctor.assign_nurse(nurse, patient, ward)

    # Book an appointment for the patient with the doctor
    appointment = book_appointment(patient, doctor)
    appointments = [appointment]  # List to store appointments

    # Display appointment details
    print("\n--- APPOINTMENT DETAILS ---")
    appointment.display_info()

    # Doctor views their appointments
    doctor.view_appointments(appointments)

    # Doctor makes a diagnosis for the appointment
    diagnosis = str(input(f"Enter diagnosis for Patient {patient.name}: "))
    doctor.diagnose(appointment, diagnosis)

    # Display updated appointment details with diagnosis
    print("\n--- Updated Appointment Details ---")
    appointment.display_info()

     # Create a billing
    billing = Billing("B001", patient, 35000.00)

    print("\n--- BILLING DETAILS: ---")
    billing.display_info()
    billing.display_info()


if __name__ == "__main__":
    main()
