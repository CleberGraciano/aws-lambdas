from chalice.test import Client
from app import app

event = {
    "nome":"Cleber",
    "idade":"31"
}

def test_index():
    with Client(app) as client:
        response = client.lambda_.invoke('Invoke', event)
        assert response.payload == True
