import typing as tp

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware

from .configs import app as APP
from .exception_handlers import register_exception_handlers
from .resources import register_resources
from .responses._all import MyGlobalResponse


def my_openapi(app):
    def f():
        if app.openapi_schema:
            return app.openapi_schema
        # Info
        contact = {
            "name": 'aponder',
            "url": 'http://aponder.top',
            "email": 'it@aponder.top',
        }
        openapi_schema = get_openapi(
            title=APP.PROJECT_NAME,
            version='0.0.1',
            # openapi_version="2.5.0",
            description='1112222333',
            routes=app.routes,
            tags=None,
            servers=None,
            terms_of_service="不知道的ToS",
            contact=contact,
            license_info={
                "name": '未授权',
                "url": 'http://aponder.top',
            }
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return f


def create_app(app_env='production') -> FastAPI:
    app = FastAPI(
        title=APP.PROJECT_NAME,
        description='',
        version='0.1.0',
        # openapi_url='/static/server1.json',
        default_response_class=MyGlobalResponse,
        docs_url="/",
        # redoc_url="/",
        # root_path='/api',
    )

    # app.openapi = my_openapi(app)

    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=APP.ALLOW_ORIGINS,
        allow_credentials=APP.ALLOW_CREDENTIALS,
        allow_methods=APP.ALLOW_METHODS,
        allow_headers=APP.ALLOW_HEADERS,
    )

    # register all resources
    register_resources(app)

    # register_api_doc(app)
    register_exception_handlers(app)

    return app


def register_api_doc(app: FastAPI):
    @app.get("/", include_in_schema=False)
    async def redirect_typer():
        return RedirectResponse("/index.html")

    from fastapi.staticfiles import StaticFiles
    app.mount('/', StaticFiles(directory=str(APP.PROJECT_PATH / 'api_doc')), name='api_doc')
