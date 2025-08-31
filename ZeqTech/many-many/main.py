from sqlalchemy import DateTime, ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os
from datetime import datetime


# ----- Database Config -----
engine = create_engine(
    'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"),
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# ----- Models -----

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)

class Appointment(BaseModel):
    __tablename__ = "appointments"
    
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))
    appointment_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)
    
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")
    
    def __repr__(self):
        return f"<Appointment(doctor={self.doctor.name}, patient={self.patient.name}, date={self.appointment_date})>"
    


class Doctor(BaseModel):
    __tablename__ = "doctors"
    
    name = Column(String)
    specialization = Column(String)
    appointments = relationship("Appointment", back_populates="doctor")
    
    
class Patient(BaseModel):
    __tablename__ = "patients"
    
    name = Column(String)
    age = Column(Integer)
    dob = Column(DateTime)
    appointments = relationship("Appointment", back_populates="patient")
    




Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)



Dr_Ahmed = Doctor(name="Dr. Ahmed", specialization="Cardiology")
Dr_Ali = Doctor(name="Dr. Ali", specialization="Orthopedics")

Mohammed_Ali = Patient(name="Mohammed Ali", age=35)
Gad_Abdallah = Patient(name="Gad Abdallah", age=28)

Appointment1 = Appointment(doctor=Dr_Ahmed, patient=Mohammed_Ali, appointment_date=datetime.now(), notes="Check-up")
Appointment2 = Appointment(doctor=Dr_Ali, patient=Gad_Abdallah, appointment_date=datetime.now(), notes="Surgery")

session.add_all([Dr_Ahmed, Dr_Ali, Mohammed_Ali, Gad_Abdallah, Appointment1, Appointment2])
session.commit()

print(Dr_Ahmed.appointments[0])