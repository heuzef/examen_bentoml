import requests

# The URL of the login and prediction endpoints
login_url = "http://127.0.0.1:3000/login"
predict_url = "http://127.0.0.1:3000/predict"

# Données de connexion
credentials = {
    "username": "bentoml",
    "password": "bentoml"
}

# Send a POST request to the login endpoint
login_response = requests.post(
    login_url,
    headers={"Content-Type": "application/json"},
    json=credentials
)

# Check if the login was successful
if login_response.status_code == 200:
    print("Authentification :", login_response)

    # Data to be sent to the prediction endpoint
    data = {
        "GRE_Score": 334,
        "TOEFL_Score": 116,
        "University_Rating": 4,
        "SOP": 4.0,
        "LOR": 3.5,
        "CGPA": 9.54,
        "Research": 1
    }

    # Send a POST request to the prediction
    response = requests.post(
        predict_url,
        headers={
            "Content-Type": "application/json"
        },
        json=data
    )

    print("Réponse de l'API de prédiction :", response.text)
else:
    print("Erreur lors de la connexion :", login_response.text)