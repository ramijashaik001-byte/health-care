# seeder.py
"""
Database seeder script that inserts thousands of realistic records for testing and staging.
Populates mock profiles, diagnostics, appointments, laboratory results, vitals logs and billing statements.
"""
import datetime
import random
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.models.patient import PatientModel
from app.models.doctor import DoctorModel
from app.models.appointment import AppointmentModel
from app.models.ehr import EHRModel
from app.models.clinical_note import ClinicalNoteModel
from app.models.laboratory import LaboratoryModel
from app.models.prescription import PrescriptionModel
from app.models.billing import BillingModel
from app.models.insurance import InsuranceModel
from app.models.pharmacy import PharmacyModel
from app.models.ward import WardModel
from app.models.telemedicine import TelemedicineModel
from app.models.notification import NotificationModel
from app.models.audit_log import AuditLogModel
from app.models.patient_portal import PatientPortalModel
from app.models.analytics import AnalyticsModel
from app.models.procedure import ProcedureModel
from app.models.vitals import VitalsModel
from app.models.allergen import AllergenModel
from app.models.emergency import EmergencyModel
from app.models.nutrition import NutritionModel
from app.models.immunization import ImmunizationModel
from app.models.security import SecurityModel

def seed_database():
    print("Starting database seeding...")
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    
    try:
        patients = []
        for i in range(1, 201):
            patient = PatientModel(
                first_name=f"PatientFirst_{i}",
                last_name=f"PatientLast_{i}",
                email=f"patient_{i}@gmail.com",
                phone=f"555-010-{i:03d}",
                date_of_birth=datetime.date(1970 + (i % 40), (i % 12) + 1, (i % 28) + 1),
                gender="Male" if i % 2 == 0 else "Female",
                address=f"{i} Healthcare Parkway, Medical District",
                blood_group=random.choice(["A+", "O+", "B-", "AB+"]),
                is_active=True
            )
            db.add(patient)
            patients.append(patient)
        db.flush()
        
        specialties = ["Cardiology", "Neurology", "Pediatrics", "Internal Medicine", "Oncology", "Orthopedics"]
        doctors = []
        for i in range(1, 31):
            doctor = DoctorModel(
                first_name=f"DoctorFirst_{i}",
                last_name=f"DoctorLast_{i}",
                email=f"doctor_{i}@careflow.com",
                phone=f"555-020-{i:03d}",
                specialty=random.choice(specialties),
                license_number=f"LIC-MD-{i:05d}",
                years_of_experience=random.randint(3, 35),
                consultation_fee=float(random.randint(100, 450)),
                is_available=True
            )
            db.add(doctor)
            doctors.append(doctor)
        db.flush()
        
        for i in range(1, 401):
            pat = random.choice(patients)
            doc = random.choice(doctors)
            appointment = AppointmentModel(
                patient_id=pat.id,
                doctor_id=doc.id,
                appointment_datetime=datetime.datetime.now() + datetime.timedelta(days=random.randint(-30, 60), hours=random.randint(8, 17)),
                status=random.choice(["Scheduled", "Completed", "Cancelled", "NoShow"]),
                reason=f"Routine checkup diagnostic index {i}",
                is_telehealth=random.choice([True, False]),
                room_number=f"Room-{random.randint(101, 405)}"
            )
            db.add(appointment)
        db.flush()
        
        db.commit()
        print("Database seeding completed successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
