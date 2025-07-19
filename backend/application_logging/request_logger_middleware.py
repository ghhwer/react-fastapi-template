from fastapi import Request
from fastapi.responses import JSONResponse

from starlette.middleware.base import BaseHTTPMiddleware
from . import log_exception, log_message

from asgi_correlation_id.middleware import CorrelationIdMiddleware

class LoggerCorrelationIdMiddleware(CorrelationIdMiddleware):
    async def dispatch(self, request, call_next):
        print(">> CorrelationIdMiddleware RUNNING")
        return await super().dispatch(request, call_next)

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            body = await request.body()
            log_message(
                "RequestLoggerMiddleware._request_received", {
                    "method": request.method, 
                    "path": request.url.path,
                    "headers": request.headers,
                    "body_raw": body.decode('utf-8')
                }
            )
            response = await call_next(request)
            log_message(
                "RequestLoggerMiddleware._respose_status", {
                    "method": request.method, 
                    "path": request.url.path,
                    "status_code": response.status_code
                }
            )
            return response
        except Exception as e:
            log_exception("response_failed", e)
            return JSONResponse(content={"error": str(e)}, status_code=500)
