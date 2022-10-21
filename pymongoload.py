import pymongo

myclient = pymongo.MongoClient("mongodb+srv://kooladmin:rnrMYhiEtPoRzl7X@cluster0.lrohczl.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["dish_app_db"]
mycol = mydb["countries"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)