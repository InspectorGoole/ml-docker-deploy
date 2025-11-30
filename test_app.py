from app import app 

def test_home():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.data == b"Hello world" # this should be like this bcuz we get an error in github actions, cuz flask expects the output in bytes