#importing the library
from fastapi import FastAPI

#creating an instance
app = FastAPI()

#giving the path for the application to run - decorator
@app.get('/')

#function
def index():
    #return 'hey'
    return {"data": {"item": "biscuits"}}

@app.get('/about')
def about():
    return {"data": "Parle G"}