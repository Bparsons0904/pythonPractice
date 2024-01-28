# from flask import Flask, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/consume-api')
# def consume_api():
#     try:
#         response = requests.get('https://some-external-api.com/data')
#         if response.status_code == 200:
#             return jsonify(response.json())
#         else:
#             return jsonify({'error': 'Bad response from external service'}), 500
#     except requests.RequestException as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/consume_api')
def consume_api():
    try:
        response = requests.get('http://some_external_api.com')
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Bad response from external service'}), 500
    except requests.RequestException as error:
        return jsonify({'error': str(error)}) 

if __name__ == '__main__':
    app.run(debug=True)
