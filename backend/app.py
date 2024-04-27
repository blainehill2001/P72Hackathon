from datetime import datetime

from flask import Flask, make_response, request  # type: ignore
from flask_cors import CORS  # type: ignore
from temp import test

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/algo")
def get_time():
    test(request.headers)
    current_time = datetime.now().strftime("%H:%M:%S")
    return make_response(current_time)


if __name__ == "__main__":
    app.run(debug=False)
