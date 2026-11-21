from sqlalchemy import Integer,Float,String
from sqlalchemy.orm import Mapped,mapped_column,relationship


from database import Base

class Patient(Base):
    __tablename__="Patients"

    Gender:Mapped[str]=mapped_column(String)
    Age:Mapped[int]=mapped_column(Integer)
    Hypertension:Mapped[int]=mapped_column(Integer)
    heart_disease:Mapped[int]=mapped_column(Integer)
    smoking_history:Mapped[str]=mapped_column(String)
    bmi:Mapped[float]=mapped_column(Float)
    HbA1c_level:Mapped[float]=mapped_column(float)
    blood_glucose_level:Mapped[int]=mapped_column(int)
