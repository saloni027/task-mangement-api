from src.auth.auth_router import auth_router
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.auth_utilities import (
    get_password_hash,
    verify_password,
    create_access_token,
)
from fastapi import Depends, HTTPException, status
from src.auth.models import TokenData

mock_users_db = {               #fake users db
    "user1": {
        "username": "user1",
        "hashed_password": get_password_hash("password1"),
    },
}


@auth_router.post("/token", response_model=TokenData)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate user and return an access token if credentials are valid.
    
    This endpoint simulates user authentication by verifying a username and password 
    against a mock user database. If the credentials are valid, an access token is 
    generated and returned.
    
    Args:
        form_data (OAuth2PasswordRequestForm): A dependency that automatically parses
                                               form data containing the username and password.
    
    Raises:
        HTTPException: If the username does not exist in the mock database or if the 
                       password is incorrect, a 401 Unauthorized exception is raised.
    
    Returns:
        dict: A dictionary containing the generated access token and its type (bearer).
    """
    user = mock_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}
