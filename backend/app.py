import datetime

from flask import Flask, request  # type: ignore

app = Flask(__name__)


@app.route("/get_time", methods=["GET"])
def get_time():
    # Print the request parameters
    print(f"Request Parameters: {request.args}")

    # Get the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return current_time


if __name__ == "__main__":
    app.run(debug=False)
