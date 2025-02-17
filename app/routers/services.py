from fastapi import APIRouter
from app.database import services
from app.database.models import serviceModel

router = APIRouter()

@router.get("/")
async def list_services():
    result = await services.list_services()
    return {"status":"true", "message": "List of services", 'data': result}

@router.get("/{service_id}")
async def list_services(
    service_id: int
):
    result = await services.get_service(service_id)
    return {"status":"true", "message": "Detail of service", 'data': result}

@router.post("/")
async def create_service(
    input_service: serviceModel.ServiceCreate
):
    result = await services.create_service(input_service)
    return {"status":"true", "message": "Service created successfull", 'data': result}