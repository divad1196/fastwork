from pony.orm import *

db = Database()


class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')
    def before_insert(self):
        print(f"Before insert! name={self.name}")

    def before_update(self):
        print(f"Before update! name={self.name}")
        if "bar" not in self.name:
            self.name += "bar"


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)


db.bind(provider='sqlite', filename='test_ponyorm.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
# set_sql_debug(True)  # => activer le debug


# @db_session  => on va devoir mettre ça sur chaque route
# ou utiliser `with db_session:`


# Il y a des hooks: https://docs.ponyorm.org/api_reference.html#entity-hooks
# Est-ce qu'on peut changer les valeurs dans ces hooks => oui et non
# Le plus simple est de faire confiance au dev pour utiliser des fonctions comme create ou write

with db_session:  # L'insert est fait qu'à la fin, il n'y a donc pas d'update 
    p1 = Person(name="A", age=5)
    p2 = Person(name="B", age=9)
    p1.name = "foo"
    show(Person.get(name="A")) 
    show(Person.select(name="B")) 


with db_session:
    foo = Person.select(lambda p: "foo" in p.name.lower())[:1][0]
    print(foo.name)
    foo.name = "foofoo"
    foo = Person.select(lambda p: "foo" in p.name.lower())
    print(dir(foo))
    # help(foo.for_update)


# la notion de recordset est bonne dans Odoo: Il n'y a ici pas de moyen d'appeler une méthode surchargée sur une liste d'entitée
# Il faut un moyen simple de générer une query à partir de json/graphql ?
# https://docs.ponyorm.org/ponyjs.html
# utiliser directement starlette plutot que fastapi: https://www.starlette.io/

# from starlette.applications import Starlette
# from starlette import routing

# class Router:
#     def __init__(self, prefix=None):
#         self._routes = []
#         self._subrouters = {}


# from starlette.applications import Starlette