import rethinkdb as r
from pprint import pprint

r.connect("localhost", 28015, db="pycon").repl()

#iterator for the entire table
c = r.table("tweets").run()
#pprint(next(c))

#Just return a single document
c = r.table("tweets").limit(1).run()
# pprint(next(c))

#Return the document but only return user name / screen name
c = r.table("tweets").pluck({"user":{ "name": True, "screen_name": True}}).limit(10).run()
# pprint([x for x in c])

#Inserting some users into the other table
# for user in c:

#     u = dict(
#         name = user['user']['name'],
#         screen_name = user['user']['screen_name']
#     )
#     print u
#     r.table("users").insert(u)


#Count documents
c = r.table("tweets").count().run()









