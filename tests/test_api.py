import requests
import pytest

def test_login_success():
    response = requests.post('http://localhost:3000/login', json={'username': 'bentoml', 'password': 'bentoml'})
    assert response.status_code == 200

def test_login_failure():
    response = requests.post('http://localhost:3000/login', json={'username': 'wrong_user', 'password': 'wrong_psw'})
    assert response.status_code == 401 or 403 or 500

def test_predict():
    url = 'http://localhost:3000/predict'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data = {
        "GRE_Score": 334,
        "TOEFL_Score": 116,
        "University_Rating": 4,
        "SOP": 4.0,
        "LOR": 3.5,
        "CGPA": 9.54,
        "Research": 1
    }

    response = requests.post(url, headers=headers, json=data)

    assert response.status_code == 200, "La requête n'a pas retourné le statut 200 attendu"
    assert 'Chance of Admit' in response.json(), "La réponse ne contient pas le champ 'Chance of Admit'"
    assert isinstance(response.json()['Chance of Admit'], float), "Le champ 'Chance of Admit' n'est pas un float"