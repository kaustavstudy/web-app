# "Database code" for the DB Forum.

import datetime
import psycopg2
DBNAME= "forum"


#POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("Select content,time from posts order by time desc")
  return c.fetchall()
  db.close()

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("Insert into posts values(%s)",(content,))
  db.commit()
  db.close()
  ##POSTS.append((content, datetime.datetime.now()))
