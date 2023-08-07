from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend-service:5000/api/astrology"  # Replace with the actual backend service URL


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        birthdate = request.form['birthdate']

        astrology_data = {
            "name": name,
            "birthdate": birthdate
        }

        try:
            response = requests.post(BACKEND_URL, json=astrology_data)
            response.raise_for_status()
            astrology_details = response.json()

            return render_template('result.html', astrology_details=astrology_details)
        except requests.exceptions.RequestException as e:
            error_message = f"Error: Unable to fetch astrology details from the backend. {e}"
            return render_template('result.html', error_message=error_message)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

