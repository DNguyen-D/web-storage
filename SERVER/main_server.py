from flask import Flask, request, jsonify
import utils.user_util as user_util

app = Flask(__name__)


def handle_action(action, data):
    if action == "signup":
        return {
            "success": user_util.sign_up(
                data.get("user"),
                data.get("password")
            )
        }

    elif action == "login":
        return {
            "success": user_util.login(
                data.get("user"),
                data.get("password")
            )
        }

    elif action == "get_user_data":
        return {
            "data": user_util.get_user_data(
                data.get("user")
            )
        }

    return {"error": "Invalid action"}


@app.route("/api", methods=["POST"])
def api_post():
    data = request.get_json()
    action = data.get("action")

    result = handle_action(action, data)
    return jsonify(result)


@app.route("/api", methods=["GET"])
def api_get():
    action = request.args.get("action")
    result = handle_action(action, request.args)
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000)