from flask import make_response, jsonify

def response_generation(response_data, status):
    response = make_response(jsonify(response_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status_code = status
    return response