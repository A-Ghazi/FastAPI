from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get('/blog')                                                               # slash is for local host - Path operation decorator
def index(limit=10, published:bool = True, sort: Optional[str] = None):                                     # path operation function 
    # only get 10 published blogs
    if published:
        return {'data':f'{limit} blogs from the list'}
    else:
        return {'data':f'{limit} published blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished blogs'}

@app.get('/blog/{id}') # path operation function
def show(id: int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

@app.post('/blog')
def create_blog():
    return {'data':"Blog is created"}