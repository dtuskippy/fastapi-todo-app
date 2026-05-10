from .utils import *
from project_3.routers.users import get_db, get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    # assert response.json() is None
    assert response.json()['email'] =='izzy@yahoo.com'
    assert response.json()['username'] =='izzy'
    assert response.json()['first_name'] =='izzy'
    assert response.json()['last_name'] =='bizzy'
    assert response.json()['role'] =='admin'
    assert response.json()['phone_number'] =='4122248096'
   
    
def test_change_password_success(test_user):
    response = client.put("/user/password", json={"password": "testpassword",
                                                   "new_password": "newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put("/user/password", json={"password": "wrong_password",
                                                   "new_password": "newpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change'}

def test_change_phone_number_success(test_user):
    response = client.put("/user/phonenumber/1112223333")
    assert response.status_code == status.HTTP_204_NO_CONTENT
