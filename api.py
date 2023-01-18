from flask import Flask, request, json

from logic import create_list, add_annotation

app = Flask(__name__)


@app.route('/contexts', methods=['GET'])
def get():
    args = request.args
    data = create_list(args["word"])
    return data, 200


@app.route('/annotation', methods=['POST'])
def post():
    data = json.loads(request.data)
    add_annotation(data["id"], data["context"], data["context_id"])
    return {"Status": "Success"}, 200


if __name__ == '__main__':
    app.run()
