import requests

url = "http://localhost:9200"
try:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print("Resposta JSON:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Erro de Conexão: {e}")
