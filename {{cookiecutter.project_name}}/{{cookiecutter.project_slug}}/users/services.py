from django.db import transaction 
from .models import User


def create_user(*, email:str,username:str, password:str) -> User:
    return User.objects.create_user(email=email,username=username, password=password)


@transaction.atomic
def register(*, bio:str|None, email:str, username:str, password:str) -> User:

    user = create_user(email=email, username=username, password=password)

    return user
