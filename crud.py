from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, user, pw):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = '1qaz2wsx'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30148
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user,pw,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(vars(data))
            return "Animal entry has been created."
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Create method to implement the R in CRUD.
    def read(self, query):
        if not query:            
            return list(self.collection.find())
        else:
            return list(self.collection.find(query))
    
    def update(self, search_key, v1, update_key, v2):
        result = self.database.animals.update_one({search_key:v1}, {"$set":{update_key:v2}})
        return str(result.modified_count) + " document(s) modified."
    
    def delete(self, remove_key, val):
        result = self.database.animals.delete_one({remove_key:val})
        return str(result.deleted_count) + " document(s) deleted."
        
        
    
class Animal:
    """"Animal class includes parameters for instantiating an animal"""
    
    def __init__(self, rec_num, age_upon_outcome, animal_id, animal_type, breed, color, date_of_birth, datetime, monthyear, name, outcome_subtype, outcome_type, sex_upon_outcome, location_lat, location_long, age_upon_outcome_in_weeks):
        
        self.rec_num =rec_num
        self.age_upon_outcome=age_upon_outcome
        self.animal_id=animal_id
        self.animal_type = animal_type
        self.breed=breed
        self.color=color
        self.date_of_birth=date_of_birth
        self.datetime=datetime
        self.monthyear=monthyear
        self.name = name
        self.outcome_subtype=outcome_subtype
        self.outcome_type=outcome_type
        self.sex_upon_outcome=sex_upon_outcome
        self.location_lat=location_lat
        self.location_long=location_long
        self.age_upon_outcome_in_weeks=age_upon_outcome_in_weeks
        
    def to_dict(self):
        return self.__dict__
    
    
    
    
    
    
    
    