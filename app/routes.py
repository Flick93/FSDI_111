from flask import Flask   #python module imported from the Flask #lowercase represents python and "Flask" viewed as object #OOP Object Oriented Paradigm

app = Flask(__name__) #creates an  instance of the Flask class (app is now an object)

@app.get("/")   #Flask decorator ro map routes to view functions. Decorator represented by "@"
def get_home():     #Flask view function
    me = {          #Flask dictionary (Key-value pairs)
        "first_name":"Paul",
        "last_name":"Afflick",
        "hobbies":"Constructive activities",
        "is_online":True
    }
    return me       #Retuning a dcitionary in Flask it is converted to JSON(Javascript Object Notation)