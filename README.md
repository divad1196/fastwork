# Fastframework

Framework based on fastapi and Sqlalchemy, handling configuration and app modules.

<WORK in PROGRESS>

This framework is currently in dev.

## Installation

```bash
pip3 install fastframework
```



## Basic Run

```bash
python3 -m fastframework
```

Based on the found configuration, this will load all modules and run your app.
You can pre-configure the framework before running it for specific use (Documentation to Do)

## Configuration

Currently, the default configuration is

```json
{
    "database": "sqlite:///fastwork.db",
    "web": {
        "cors": []
    },
    "server": {
        "host": "127.0.0.1",
        "port": 5000,
        "log_level": "info"
    },
    "modules": [],
    "base_path": null
}

```

You just have to write what you want to override, for example

```bash
{
    "modules": [
        "modules_test/module_test",
        "modules_test/module.py"
    ]
}
```

Fastframework will look in the call path for fastwork.json, if it is not found, it will look for "FASTWORK_CONFIG" env variable for a valid config path.
Otherwise, the above default config is used.

Configuration will normally be extendable for modules' needs.



## Writing module

module's path is defined relatively to the configuration file, or the configuration "base_path" value.
They are mere python module.



## Model inheritance

```python
# file 1

from fastframework import register
from sqlalchemy import Boolean, Column, Integer, String

@register("contact")
class Contact:
    name = Column(String)
    forname = Column(String)

# file 2
from fastframework import register
from sqlalchemy import Boolean, Column, Integer, String

@register("contact")
class Contact:
    age = Column(Integer)
```

the resulting class is

```python
class Contact:
	__tablename__ = "contact"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    forname = Column(String)
    age = Column(Integer)
```



Example of use:

```python
import fastframework
framework = fastframework.framework
framework.init()  # for manual use only, no running server, implicitly done in run methode

Contact = framework.db["contact"]
session = framework.db.session()
c = Contact(name="paul", forname="henri", age=22)
session.add(c)
session.commit()
session.close()

# Later, somewhere else
Contact = framework.db["contact"]
session = framework.db.session()

contacts = session.query(Contact).all()
```





## To Do

1. Database migration automation, see [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment)

