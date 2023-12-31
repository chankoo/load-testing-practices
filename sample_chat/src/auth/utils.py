from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_pwd(pwd: str):
    return pwd_context.hash(pwd)


def verify(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)
