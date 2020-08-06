from .app import framework

def init():
    return framework.init()

def run():
    return framework.run()

def register(*args, **kwargs):
    return framework.db.register(*args, **kwargs)