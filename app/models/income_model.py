from sqlalchemy import Column, Integer, String, Float

from app.core.database import Base


class Income(Base):

    __tablename__ = "income"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(String)

    amount = Column(Float)