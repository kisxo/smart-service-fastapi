from app.database.db import get_session
from sqlmodel import Session, select
from app.database.models.serviceModel import Service, ServiceCreate

async def list_services(
    session: Session = next(get_session())
):
    statement = select(Service)
    results = session.exec(statement)
    return results.all()

async def get_service(
    service_id: int,
    session: Session = next(get_session())
):

    results = session.get(Service, service_id)
    return results

async def create_service(
    input_service: ServiceCreate,
    session: Session = next(get_session())
):
    service = Service(
        name = input_service.name,
        phone = input_service.phone,
        category = input_service.category,
        area = input_service.area
    )
    session.add(service)
    session.commit()
    session.refresh(service)

    return service