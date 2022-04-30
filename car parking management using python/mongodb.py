from pymongo import MongoClient

client= MongoClient("")


db = client.get_database('Enhancement')
records=db.Enhance

#Count documents
#records.count_documents({})

def new_value_insert(cd,av,loc):
    x = {'Co-ordinates':cd,'Available-Spaces':av,'Location':loc}
    records.insert_one(x)
def update_values(cd, avsp):
    myquery = { 'Co-ordinates':cd }
    newvalues = { "$set": {'Location':'Bhutan','Available-Spaces':avsp} }
    db.Enhance.update_one(myquery, newvalues)




