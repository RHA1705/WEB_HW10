import os
import django
from pymongo import MongoClient


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite_quotes.settings')
django.setup()

from quotes.models import Author, Tag, Quotes
# from mongoengine import connect

# connect to cluster on AtlasDB with connection string

client = MongoClient(host=f"""mongodb+srv://romanharbazh:SofiaOlenka24@cluster0.dvat4.mongodb.net""", ssl=True)
db = client.web_hw9
authors = db.author.find()
quotes = db.quote.find()
# for author in authors:
#     Author.objects.get_or_create(fullname=author['fullname'],
#                                  born_date=author['born_date'],
#                                  born_location=author['born_location'],
#                                  description=author['description'])

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quotes.objects.filter(quote=quote['quote'])))

    if not exist_quote:
        author = db.author.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quotes.objects.create(quote=quote['quote'],
                                  author=a)

    for tag in tags:
        q.tags.add(tag)
