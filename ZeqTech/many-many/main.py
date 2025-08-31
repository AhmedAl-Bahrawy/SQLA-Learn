from sqlalchemy import DateTime, ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os
from datetime import datetime


# ----- Database Config -----
engine = create_engine(
    'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db")
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# All that is just learning but powerful

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
    
    
    # Without it will display the place of the memory
    
    def __repr__(self):
        doctor_name = self.doctor.name if self.doctor else "Unknown"
        patient_name = self.patient.name if self.patient else "Unknown"
        date_str = self.appointment_date.strftime("%Y-%m-%d %H:%M") if self.appointment_date else "No date"
        return f"<Appointment(doctor='{doctor_name}', patient='{patient_name}', date='{date_str}')>"
    


class Doctor(BaseModel):
    __tablename__ = "doctors"
    
    name = Column(String)
    specialization = Column(String)
    appointments = relationship("Appointment", back_populates="doctor")
    
    
    # Without it will display the place of the memory
    def __repr__(self):
        appointments_count = len(self.appointments) if hasattr(self, 'appointments') and self.appointments else 0
        return f"<Doctor(name='{self.name}', specialization='{self.specialization}', appointments_count={appointments_count})>"
    
    
class Patient(BaseModel):
    __tablename__ = "patients"
    
    name = Column(String)
    age = Column(Integer)
    dob = Column(DateTime)
    appointments = relationship("Appointment", back_populates="patient")
    
    
    # Without it will display the place of the memory
    def __repr__(self):
        appointments_count = len(self.appointments) if hasattr(self, 'appointments') and self.appointments else 0
        return f"<Patient(name='{self.name}', age={self.age}, appointments_count={appointments_count})>"
    



# remove and create a new data

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Signing the data to columns to try it 

Dr_Ahmed = Doctor(name="Dr. Ahmed", specialization="Cardiology")
Dr_Ali = Doctor(name="Dr. Ali", specialization="Orthopedics")

Mohammed_Ali = Patient(name="Mohammed Ali", age=35)
Gad_Abdallah = Patient(name="Gad Abdallah", age=28)

Appointment1 = Appointment(doctor=Dr_Ahmed, patient=Mohammed_Ali, appointment_date=datetime.now(), notes="Check-up")
Appointment2 = Appointment(doctor=Dr_Ali, patient=Gad_Abdallah, appointment_date=datetime.now(), notes="Surgery")
Appointment3 = Appointment(doctor=Dr_Ahmed, patient=Gad_Abdallah, appointment_date=datetime.now(), notes="Check-up")

session.add_all([Dr_Ahmed, Dr_Ali, Mohammed_Ali, Gad_Abdallah, Appointment1, Appointment2])
session.commit()


print()
print('='*50)
print()

print(Dr_Ahmed.appointments[0])


# Just getting everything from its columns
print(session.query(Appointment).all())
print(session.query(Doctor).all())
print(session.query(Patient).all())

print('='*50)
print()
print('='*50)

# trying to make a something new
print(*(row for row in session.query(Appointment).filter(Appointment.doctor.has(name='Dr. Ahmed'))), sep="\n")

print('='*50)
print()
print('='*50)

# Just trying the new way to unlink the list just learned now 
print(*([1, 2, 3]), sep="\n")



# Hey I just noticed I have learned to make comments 
# Yabeee !!!!