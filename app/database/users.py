from app.database.db import get_session
from sqlmodel import Session, select
from app.database.models.userModel import User, UserCreate

async def list_users(
    session: Session = next(get_session())
):
    statement = select(User)
    results = session.exec(statement)
    return results.all()

async def create_user(
    input_user: UserCreate,
    session: Session = next(get_session())
):
    user = User(
        email = input_user.email,
        name = input_user.name,
        password = input_user.password
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    return user