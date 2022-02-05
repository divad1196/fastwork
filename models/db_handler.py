from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from .alembic import run_migrations

class DatabaseHandler:
    def __init__(self, dsn: str, **kwargs):
        self._base = declarative_base()
        self._dsn = dsn  # data source name, e.g. "sqlite:///fastwork.db"
        self._engine = create_engine(dsn, connect_args={"check_same_thread": False}, **kwargs)
        self._SessionMaker = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._engine,
        )
        self._model_load_registry = {}
        self._registry = {}

    def _get_base_metaclass(self, name):
        class Base(self._base):
            __tablename__ = name
            __abstract__ = True
            id = Column(Integer, primary_key=True, index=True)

        return Base

    def register(self, name):
        def _register(cls):
            if name not in self._model_load_registry:
                BaseModel = self._get_base_metaclass(name)
                self._model_load_registry[name] = [BaseModel]
            self._model_load_registry[name].append(cls)
        return _register

    def _make_register(self):
        self._registry = {}
        for name, inheritance in self._model_load_registry.items():
            self._registry[name] = type(
                name,
                tuple(reversed(inheritance)),
                {}
            )

    def __iter__(self):
        if self._registry:
            return iter(self._registry)
        return iter({})

    def __getitem__(self, model):
        return self._registry[model]

    def _create_all(self):
        self._base.metadata.create_all(bind=self._engine)

    def session_generator(self):
        try:
            session = self._SessionMaker()
            yield session
        finally:
            session.close()

    def migrate(self):
        run_migrations(self._dsn, )

    def session(self):
        return self._SessionMaker()

    def init(self):
        self._make_register()
        self._create_all()

