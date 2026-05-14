from fastapi import FastAPI, Query, HTTPException, Path
import pyjokes
from pydantic import BaseModel, Field

app = FastAPI()

class Joke(BaseModel):
    friend: str
    joke: str

class JokeInput(BaseModel):
    friend: str = Field(..., min_length=2)

@app.get("/multi/{friend}", status_code=200)
def multi_friends_joke(friend: str = Path(..., min_length=2), jokes_number: int = Query(1)):
    if jokes_number < 1 or jokes_number > 15:
        raise HTTPException(status_code=400, detail="Invalid jokes number")

    if not friend.isalpha():
        raise HTTPException(status_code=400, detail="Invalid jokes number")

    result = ""
    for i in range(jokes_number):
        result += friend + f" tells joke №{i + 1}: " + pyjokes.get_joke()
    return result

@app.post("/", response_model=Joke, status_code=201)
def create_joke(joke_input: JokeInput):
    if not joke_input.friend.isalpha():
        raise HTTPException(status_code=400, detail="Invalid jokes number")
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())

@app.get("/path-joke/{friend}")
def path_joke(friend: str = Path(..., min_length=2)):
    if not friend.isalpha():
        raise HTTPException(status_code=400, detail="Invalid friend")
    return {"friend": friend, "joke": pyjokes.get_joke()}

@app.get("/query-joke")
def query_joke(friend: str = Query(..., min_length=2)):
    if not friend.isalpha():
        raise HTTPException(status_code=400, detail="Invalid friend")
    return {"friend": friend, "joke": pyjokes.get_joke()}