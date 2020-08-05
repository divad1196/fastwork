from .app import framework

def register(*args, **kwargs):
    return framework.db.register(*args, **kwargs)