from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.auth.auth_utilities import verify_access_token


class JWTBearer(HTTPBearer):
    """
    Custom security class that extends FastAPI's HTTPBearer class to handle JWT authentication.
    
    It validates the 'Bearer' token from the Authorization header of the request and checks if
    the JWT token is valid using a verification utility.
    """
    def __init__(self, auto_error: bool = True):
        """
        Constructor for JWTBearer class.
        
        Args:
            auto_error (bool): If set to True, FastAPI will automatically raise an error
                               if the token is missing or invalid. Defaults to True.
        """
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        """
        Handles the authentication process by checking the Authorization header in the request.
        
        Args:
            request (Request): Incoming HTTP request that contains the JWT token in the Authorization header.

        Raises:
            HTTPException: If the authentication scheme is invalid (not 'Bearer') or if the token
                           is invalid/expired, a 403 Forbidden error is raised.

        Returns:
            str: The JWT token if it's valid.
        """
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        """
        Verifies the validity of a JWT token by checking its payload.
        
        Args:
            jwtoken (str): The JWT token to be verified.
        
        Returns:
            bool: True if the token is valid, False otherwise.
        """
        isTokenValid: bool = False

        try:
            payload = verify_access_token(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True

        return isTokenValid
