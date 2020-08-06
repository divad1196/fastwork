from .app import framework

db = framework.db
app = framework.app

def init():
    return framework.init()

def run():
    return framework.run()

def register(*args, **kwargs):
    return framework.db.register(*args, **kwargs)