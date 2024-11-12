from fastapi import APIRouter, Depends
from schemas import RequestCreateUser, ResponseUser, RequestUpdateUser
from sqlalchemy.orm import Session
from database import get_db
from crud import create_user, get_users, update_user

router = APIRouter(
    prefix="/auth"
)



@router.post(
    "/",
    response_model=ResponseUser
)
def session_create_user(
    request: RequestCreateUser,
    db: Session = Depends(get_db)
):  
    user = create_user(request, db)
    return ResponseUser(id=user.id, email=user.email, username=user.user_name)



@router.get(
    "/users",
    response_model = list[ResponseUser]
)
def session_get_users(
    db: Session = Depends(get_db)
):
    users = get_users(db)
    return [ResponseUser(id=user.id, email=user.email, username=user.user_name) for user in users]



@router.put(
    "/",
    response_model = ResponseUser
)
def session_update_user(
    id: int,
    request: RequestUpdateUser,
    db: Session = Depends(get_db)
):
    user = update_user(id, request, db)
    return ResponseUser(id=user.id, email=user.email, username=user.user_name)
    