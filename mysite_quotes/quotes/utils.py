from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(host=f"""mongodb+srv://romanharbazh:SofiaOlenka24@cluster0.dvat4.mongodb.net""", ssl=True)
    db = client.web_hw9
    return db
