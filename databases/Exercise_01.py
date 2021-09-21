'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.
Using
'''

import sqlalchemy
from pprint import pprint
# engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/sakila')
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')

connection = engine.connect()

metadata = sqlalchemy.MetaData()

# actor = sqlalchemy.Table("actor", metadata, autoload=True, autoload_with=engine)

film = sqlalchemy.Table("film", metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table("category", metadata, autoload=True, autoload_with=engine)

# print(actor.columns.keys())
# print(repr(metadata.tables["actor"]))

print(film.columns.keys())
pprint(repr(metadata.tables["film"]))

print(category.columns.keys())
pprint(repr(metadata.tables["category"]))