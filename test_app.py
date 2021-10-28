from app import app
client=app.test_client()
def test_devops():
    response=client.get('/')
    assert response.status_code==200

