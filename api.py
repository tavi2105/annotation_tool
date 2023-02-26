import flask
from flask import Flask, request, json
from flask_cors import CORS
from logic import create_list, add_annotation

app = Flask(__name__)
CORS(app)


@app.route('/contexts', methods=['GET'])
def get():
    args = request.args
    data = create_list(args["word"])

    response = flask.jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/annotation', methods=['POST'])
def post():
    data = json.loads(request.data)
    print(data)
    add_annotation(data["id"], data["context"], data["context_id"])

    response = flask.jsonify({"Status": "Success"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()
