import fastwork
framework = fastwork.framework
framework.init()

Contact = framework.db["contact"]
session = framework.db.session()
c = Contact(name="paul", forname="henri")
session.add(c)
session.commit()
session.close()



Contact = framework.db["contact"]
session = framework.db.session()

contacts = session.query(Contact).all()