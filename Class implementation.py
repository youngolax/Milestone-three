# Encapsulation: Base class Staff with private attributes and public methods
class Staff:
    def __init__(self, staff_id, name, age, gender, role):
        # private attributes
        self.staff_id = staff_id
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role
# Public Method
    def display_info(self):
        print(f"Staff ID: {self.staff_id}")
        print(f"Name: {self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")
        print(f"Role: {self.role}")

# Inheritance: Doctor class inherit from Staff
class Doctor(Staff):
    def __init__(self, staff_id, name, age, gender, speciality):
        super().__init__(staff_id, name, age, gender,role="Doctor")
        self.speciality = speciality
        self.assigned_nurses = {}  # Dictionary to hold nurses assigned to patients

# Abstraction: Assigning a nurse to a patient and ward, simplified for user
    def assign_nurse(self, nurse, patient, ward):
        self.assigned_nurses[patient.patient_id] = (nurse, ward)
        print(f"Nurse {nurse.name} assigned to Patient {patient.name} in Ward {ward}.")

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
        print(f"Diagnosis '{diagnosis}' added to appointment for Patient {appointment.patient.name}.")

# Inheritance: Nurse class inherits from staff class
class Nurse(Staff):
    def __init__(self, staff_id, name,age, gender):
        super().__init__(staff_id, name, age, gender, role="Nurse")

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
        print(f"Amount Due: UGX{self.amount:.2f}")


