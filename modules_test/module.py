from fastwork import register
from sqlalchemy import Boolean, Column, Integer, String

@register("contact")
class Contact:
    age = Column(Integer)