from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException

from core.exception_handlers import _all


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(RequestValidationError, _all.handle_validation_exception)
    app.add_exception_handler(StarletteHTTPException, _all.handle_http_exception)
    app.add_exception_handler(Exception, _all.handle_exception)
