from ... import register, app
from ...modules import tools
from sqlalchemy import Boolean, Column, Integer, String

@register("module")
class Module:
    name = Column(String)
    name = Column(String)