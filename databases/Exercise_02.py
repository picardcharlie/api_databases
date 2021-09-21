'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''

import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# Find all the actors named "Morgan"

actor = sqlalchemy.Table("actor", metadata, autoload = True, autoload_with = engine)
actor_query = sqlalchemy.select([actor]).where(actor.columns.first_name == "Morgan")
actor_query_results = connection.execute(actor_query)
result_actor = actor_query_results.fetchall()
print("Lists all actors named 'Morgan':")
pprint(result_actor)

# Print out all the movies the actors named "Morgan" have been in.

film_actor = sqlalchemy.Table("film_actor", metadata, autoload = True, autoload_with = engine)
film = sqlalchemy.Table("film", metadata, autoload = True, autoload_with = engine)
#actor is already loaded

# Joines the actor and film_actor table together if the IDs match.  Then joins the film and film_actor together if the ID mactches.
join_actor_film = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)

# searches for the name "Morgan" and the movie title and their full name for each found.
film_actor = sqlalchemy.select([film.columns.title, actor.columns.first_name, actor.columns.last_name]).select_from(join_actor_film).where(actor.columns.first_name == "Morgan")

query_film_actor = connection.execute(film_actor)
results_film_actor = query_film_actor.fetchall()
print("List the names of all movies with an actor named 'Morgan':")
pprint(results_film_actor)

# Select all the actors in a comedy category of my choice.
film_category = sqlalchemy.Table("film_category", metadata, autoload = True, autoload_with = engine)

film_cat = join_actor_film.join(film_category, film.columns.film_id == film_category.columns.film_id)

comedy_film = sqlalchemy.select([film.columns.title, actor.columns.first_name, actor.columns.last_name]).select_from(film_cat).where(film_category.columns.category_id == 5)

query_comedy_film = connection.execute(comedy_film)
results_comedy_film = query_comedy_film.fetchall()
print("List all movies and their actors in the comedy category:")
pprint(results_comedy_film)

# Select all the comedic films and sort them by rental rate
# rental_rate = sqlalchemy.select([film.columns.title, film.columns.rental_rate]).select_from(film_cat).where(film_category.columns.category_id == 5)
# ^^^ this caused it to print out the finding from it 4 times each.  I think it's just from the extra tables or how I connected them.  I'm tired.

comedy_rate = film.join(film_category, film.columns.film_id == film_category.columns.film_id)
rental_rate = sqlalchemy.select([film.columns.title, film.columns.rental_rate]).select_from(comedy_rate).where(film_category.columns.category_id == 5)

query_rental_rate = connection.execute(rental_rate)
results_rental_rate = query_rental_rate.fetchall()
print("List the rental cost of all comedy movies:")
pprint(results_rental_rate)

# Using one of the statements above, add a GROUP BY statement of your choice
# group_film = sqlalchemy.select([film.columns.title, film.columns.rental_rate]).group_by(film.columns.rental_rate)
# query_group = connection.execute(group_film)
# group_results = query_group.fetchall()
# pprint(group_results)
'''
GROUP was not covered in the course and the internet isn't being helpful at all.  What is this?
'''



# Using one of the statements above, add a ORDER BY statement of your choice
from sqlalchemy import asc

#order_rental = sqlalchemy.select([film.columns.title, film.columns.lenth]).order_by(asc(film.columns.lenth))
# This line gave non-stop problems.  I copy and pasted the one from the course and dedited it, no problem.

order_rental = sqlalchemy.select([film.columns.title, film.columns.length]).order_by(sqlalchemy.asc(film.columns.length))
query_order = connection.execute(order_rental)
results_order = query_order.fetchall()
pprint(results_order)