from fastapi import Request

from src.presentation.routers.gateway_routers import (
    RedirectToAuthException,
    RedirectToCommerceException,
)


def api_gateway_router(request: Request, service_id: str):
    path = request.url.path.removeprefix(f"/gateway/{service_id}")

    if service_id == str(1):
        raise RedirectToAuthException(service_id, path)
    if service_id == str(2):
        raise RedirectToCommerceException(service_id, path)
