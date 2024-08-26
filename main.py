'''
- This program is written in Python.
- The main function is to generate a password defined by the users requirements e.g. length, inclusion of uppercase letters, lowercase letters, digits, and special characters.
- The output will be a string containing the randomly generated password.
- This program will use FASTAPI to generate the password.
'''

from fastapi import FastAPI 

app = FastAPI()

@app.get('/')

async def root():
    return {"message": "Welcome to the password generator API!"}

