from typing import Union

from fastapi import FastAPI

#from uvicorn import run as app_run

myapp = FastAPI()


@myapp.get("/")
def root():
    return "Hello Visnu!. You have created an fastapi app and ran it through docker."


#app_run(myapp)


