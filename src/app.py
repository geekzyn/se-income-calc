from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "<p>Hello, World!<p>"

@app.route('/calculate', methods=['POST'])
def calculate():
    req_data = request.get_json()
    daily_rate = req_data['daily_rate']
    days_worked = req_data['days_worked']
    return jsonify({
        'daily_rate': daily_rate,
        'days_worked': days_worked,
        'revenue': daily_rate * days_worked
    })

if __name__ == '__main__':
    app.run(debug=True)