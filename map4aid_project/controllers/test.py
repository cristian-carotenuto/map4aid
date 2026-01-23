import requests

data = {
    "email": "prova@test.com",
    "password": "123456",
    "ruolo": "beneficiario",
    "nome": "Mario",
    "cognome": "Rossi"
}
try:
    response = requests.post("http://127.0.0.1:5000//register", data=data)
    print("Status:", response.status_code)
    try:
        print("JSON:", response.json())
    except ValueError:  # se non è JSON
        print("Risposta non JSON:", response.text)
except requests.exceptions.RequestException as e:
    print("Errore nella richiesta:", e)