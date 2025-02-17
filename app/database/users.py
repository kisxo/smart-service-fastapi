from app.database.db import get_session
from sqlmodel import Session, select
from app.database.models.userModel import User

async def list_users(
    session: Session = next(get_session())
):
    statement = select(User)
    results = session.exec(statement)

    return results