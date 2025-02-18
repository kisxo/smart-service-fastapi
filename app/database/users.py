from fastapi import HTTPException
from app.database.db import get_session, engine
from sqlmodel import Session, select
from app.database.models.userModel import User, UserCreate
from app.security.security import get_password_hash
from app.security.phone import phone_lookup

async def list_users(
    session: Session = next(get_session())
):
    statement = select(User)
    results = session.exec(statement)
    return results.all()

async def get_user(
    user_id: int = None
):
    with Session(engine) as session:
            return session.get(User, user_id)

async def create_user(
    input_user: UserCreate,
):
    user = User(
        phone = phone_lookup(input_user.phone),
        name = input_user.name,
        password = get_password_hash(input_user.password)
    )

    with Session(engine) as session:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="User already exists!")

    return user