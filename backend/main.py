import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from controller.sub_controller_a import route as sub_controller_a_route
from controller.sub_controller_b import route as sub_controller_b_route
from fastapi.middleware.cors import CORSMiddleware
from application_logging.setup import setup_logging
from application_logging.request_logger_middleware import (
    RequestLoggerMiddleware, 
    LoggerCorrelationIdMiddleware
)
import settings
from repository.database import init_models
from app_lifespan import lifespan

# Database things
# For async you may need to wait on this function to return.
init_models()

# Setup FastAPI
config = {
    "title": settings.TITLE,
    "description": settings.DESCRIPTION,
    "summary": settings.SUMMARY,
    "version": settings.VERSION,
    "lifespan": lifespan
}
app = FastAPI(**config)
# Logging
logger = logging.getLogger(__name__)
setup_logging()
app.add_middleware(RequestLoggerMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggerCorrelationIdMiddleware)

# Mout Routes
app.mount(f'{settings.API_ROUTE_PREFIX}/sub_controller_a', sub_controller_a_route)
app.mount(f'{settings.API_ROUTE_PREFIX}/sub_controller_b', sub_controller_b_route)

# Root endpoints
@app.get("/")
async def redirect_docs():
    return RedirectResponse("/docs")

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}