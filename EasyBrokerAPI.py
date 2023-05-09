import requests
import json

class EasyBrokerAPI:
    def __init__(self, auth_token):
        self.url = "https://api.stagingeb.com/v1/contact_requests"
        self.auth_token = auth_token
        
    def get_properties(self):
        headers = {"X-Authorization": self.auth_token, "accept": "application/json"}
        url = self.url + "?page=1&limit=20"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            for property in data["content"]:
                print(property["name"])
                print(property["email"])
                print(property["property_id"])
                print(property["message"])
                print(property["source"])
                print(property["happened_at"])
                print()
        else:
            print("Error: ", response.status_code)

# Test unitario para verificar la conexión con la API de EasyBroker y la recuperación de propiedades
def test_get_properties():
    # credenciales de autenticación.
    api = EasyBrokerAPI("l7u502p8v46ba3ppgvj5y2aad50lb9")
    api.get_properties()

# Ejecución del test
test_get_properties()
