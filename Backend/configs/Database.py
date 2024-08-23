from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://myuser:mypassword@localhost:3306/mydatabase'

"Author @Arun"

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:admin@localhost:3306/virtualqueue'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)


def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
