#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, HTTPException

from alcolotest_const import People, PEOPLE_EXAMPLE

# Initialization of the api
app = FastAPI()

# Default response
@app.get("/")
def welcome_user():
    return {"message": "This is the Alcolotest API"}

# Add a new user.
@app.post("/add_user", status_code=200)
def add_user(new_user: People = PEOPLE_EXAMPLE):
    add_user_to_database(new_user)
    return {"%s has been added to the database" % new_user.first_name }


def add_user_to_database(new_user):
    #TO DO
    return


if __name__ == "__main__":
    uvicorn.run(app, port=8000, log_level="info")
