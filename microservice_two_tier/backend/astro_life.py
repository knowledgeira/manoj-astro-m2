from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

def get_life_path_number(birthdate):
    birthdate_obj = datetime.datetime.strptime(birthdate, "%d-%m-%Y")
    birthdate_str = birthdate_obj.strftime("%d%m%Y")
    life_path_number = 0
    for digit in birthdate_str:
        life_path_number += int(digit)
    while life_path_number > 9:
        life_path_number = sum(int(digit) for digit in str(life_path_number))
    return life_path_number

def get_lucky_number(birthdate):
    birthdate_obj = datetime.datetime.strptime(birthdate, "%d-%m-%Y")
    day = birthdate_obj.day
    lucky_number = 0
    for digit in str(day):
        lucky_number += int(digit)
    while lucky_number > 9:
        lucky_number = sum(int(digit) for digit in str(lucky_number))
    return lucky_number

def get_lucky_planet(lucky_number):
    planets = {
        1: "Sun",
        2: "Moon",
        3: "Jupiter",
        4: "Rahu",
        5: "Mercury",
        6: "Venus",
        7: "Ketu",
        8: "Saturn",
        9: "Mars"
    }
    return planets.get(lucky_number)

@app.route('/api/astrology', methods=['POST'])
def astrology():
    data = request.get_json()
    name = data.get('name')
    birthdate = data.get('birthdate')

    if not name or not birthdate:
        return jsonify(error="Name and birthdate are required."), 400

    try:
        life_path_number = get_life_path_number(birthdate)
        lucky_number = get_lucky_number(birthdate)
        lucky_planet = get_lucky_planet(lucky_number)

        astrology_details = {
            'name': name,
            'life_path_number': life_path_number,
            'lucky_number': lucky_number,
            'lucky_planet': lucky_planet
        }

        return jsonify(astrology_details)
    except Exception as e:
        return jsonify(error="An error occurred while processing the request."), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

