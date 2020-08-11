import flask
from flask import Response

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/pass', methods=['GET'])
def passstatus():
    f = open('teststatus.json')
    x = f.read()
    f.close()
    return Response(x, mimetype='application/json')

@app.route('/fail', methods=['GET'])
def failstatus():
    f = open('teststatus_fail.json')
    x = f.read()
    f.close()
    return Response(x, mimetype='application/json')

if __name__ == '__main__':
    app.run()