from fastapi import FastAPI
from application_logging import log_message, log_exception

route = FastAPI(title="sub-api-b")

@route.get("/")
def get_b():
    log_message("SUB-B", "Hello Called")
    return {"message": "Hello World from sub B"}