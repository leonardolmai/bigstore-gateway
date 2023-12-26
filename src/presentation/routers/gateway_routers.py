from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/gateway", tags=["gateway"])


class RedirectToAuthException(HTTPException):
    def __init__(self, service_id: str, path: str):
        detail = f"Redirecting to Service {service_id}"
        super().__init__(status_code=status.HTTP_307_TEMPORARY_REDIRECT, detail=detail)
        self.service_id = service_id
        self.path = path


class RedirectToCommerceException(HTTPException):
    def __init__(self, service_id: str, path: str):
        detail = f"Redirecting to Service {service_id}"
        super().__init__(status_code=status.HTTP_307_TEMPORARY_REDIRECT, detail=detail)
        self.service_id = service_id
        self.path = path


# @router.route(
#     "/{service_id}/{path:path}",
#     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
# )
# def gateway(service_id: int):
#     return {"message": f"API Gateway Microservice {service_id}"}


@router.get("/{service_id}/{path:path}")
def gateway_get(service_id: int):
    return {"message": f"API Gateway Microservice {service_id}"}


@router.post("/{service_id}/{path:path}")
def gateway_post(service_id: int):
    return {"message": f"API Gateway Microservice {service_id}"}


@router.patch("/{service_id}/{path:path}")
def gateway_patch(service_id: int):
    return {"message": f"API Gateway Microservice {service_id}"}


@router.delete("/{service_id}/{path:path}")
def gateway_delete(service_id: int):
    return {"message": f"API Gateway Microservice {service_id}"}
