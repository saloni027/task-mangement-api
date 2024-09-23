from passlib.context import CryptContext
from jose import JWTError, jwt
from decouple import config

#Secret key and algorithm for JWT encoding/decoding loaded from environment variables
SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM", default="HS256")


#password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    """
    Hashes the provided password using bcrypt.
    
    Args:
        password (str): The plaintext password to be hashed.
    
    Returns:
        str: The hashed version of the password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """
    Verifies a plaintext password against a hashed password.
    
    Args:
        plain_password (str): The plaintext password provided by the user.
        hashed_password (str): The hashed password stored in the database.
    
    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    """
    Creates a JWT (JSON Web Token) for a given set of data.
    
    Args:
        data (dict): A dictionary containing the payload to encode into the JWT.
    
    Returns:
        str: The encoded JWT string.
    """
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    """
    Verifies a JWT and extracts the 'sub' (subject) claim, which typically contains the username.
    
    Args:
        token (str): The JWT to verify.
    
    Returns:
        str: The username ('sub' claim) if the token is valid.
        None: If the token is invalid or the 'sub' claim is missing.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return
        return username
    except JWTError:
        return
