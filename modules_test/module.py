from fastframework import register, app
from sqlalchemy import Boolean, Column, Integer, String

@register("contact")
class Contact:
    age = Column(Integer)

@app.get("/")
def test():
    return "hello world"