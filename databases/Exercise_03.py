'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''

import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')

connection = engine.connect()

metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table("film", metadata, autoload=True, autoload_with=engine)

rental_150 = sqlalchemy.update(film).values(rental_duration = 10).where(film.columns.length > 150)

update_rental = connection.execute(rental_150)