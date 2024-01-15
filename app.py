from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route('/')
def index():
    locations = []
    try:
        locations = util.get_location_names()
    except:
        locations.append("No Data Available")
    return render_template('index.html', locations=locations)


# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


util.load_saved_artifacts()
app.run()
