# pylint: disable=unused-argument
from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.presentation.dependencies.api_gateway_router import api_gateway_router
from src.presentation.routers import gateway_routers

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=["Authorization"],
    # allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    # allow_headers=[
    #     "Accept",
    #     "Content-Type",
    #     "Origin",
    #     "Authorization",
    #     "X-CSRF-Token",
    #     "X-Requested-With",
    #     "X-Company-CNPJ",
    #     "Cache-Control",
    #     "If-None-Match",
    #     "Access-Control-Allow-Origin",
    #     "Access-Control-Allow-Methods",
    #     "Access-Control-Allow-Headers",
    #     "Authorization",
    #     "X-Company-CNPJ",
    # ],
)

app.include_router(gateway_routers.router, dependencies=[Depends(api_gateway_router)])


@app.exception_handler(gateway_routers.RedirectToAuthException)
def exception_handler_auth(
    request: Request, exc: gateway_routers.RedirectToAuthException
) -> Response:
    destination_url = f"http://0.0.0.0:8001{exc.path}"
    return RedirectResponse(url=destination_url)


@app.exception_handler(gateway_routers.RedirectToCommerceException)
def exception_handler_commerce(
    request: Request, exc: gateway_routers.RedirectToCommerceException
) -> Response:
    destination_url = f"http://0.0.0.0:8002{exc.path}"
    return RedirectResponse(url=destination_url)
