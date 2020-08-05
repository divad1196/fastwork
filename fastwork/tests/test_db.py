from modular_app import Framework
from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String

f = Framework()

@f.db.register("test")
class A:
    a = Column(Integer)

@f.db.register("test")
class A:
    b = Column(Integer)

@f.db.register("test")
class B:
    c = Column(Integer)

@f.db.register("test2")
class B:
    c = Column(Integer)

f.init()

test = f.db["test"](a=4, b=7, c=9)
print(test.a, test.b, test.c)