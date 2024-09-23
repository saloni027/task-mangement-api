from pydantic import BaseModel


class TokenData(BaseModel):
    """
    Pydantic model representing the data returned after successful authentication.

    Attributes:
        access_token (str): The JWT access token issued to the user.
        token_type (str): The type of the token, typically "bearer".
    """
    access_token: str
    token_type: str
