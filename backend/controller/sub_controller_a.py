from fastapi import FastAPI
from application_logging import log_message, log_exception

route = FastAPI(title="sub-api-a")

@route.get("/")
def get_a():
    log_message("SUB-A", "Hello Called") 
    return {"message": "Hello World from sub A"}