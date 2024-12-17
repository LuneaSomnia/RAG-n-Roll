from sqlalchemy import Column, Integer, String, Date, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    medical_history = Column(JSON)
    lifestyle_data = Column(JSON)
    emergency_contacts = Column(JSON)
    
    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "date_of_birth": str(self.date_of_birth),
            "gender": self.gender,
            "medical_history": self.medical_history,
            "lifestyle_data": self.lifestyle_data,
            "emergency_contacts": self.emergency_contacts
        }
