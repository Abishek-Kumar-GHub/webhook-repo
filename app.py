from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["github_hooks"]
collection = db["events"]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event = request.headers.get("X-GitHub-Event")

    print(f"\n--- Event Received ---")
    print(f"Event Type: {event}")
    print(f"Payload: {data}")

    if event == "push":
        commit = data.get("head_commit", {})
        collection.insert_one({
            "request_id": commit.get("id", ""),
            "author": data.get("pusher", {}).get("name", "Unknown"),
            "action": "PUSH",
            "from_branch": None,
            "to_branch": data.get("ref", "").split("/")[-1],
            "timestamp": commit.get("timestamp", datetime.utcnow().isoformat())
        })

    elif event == "pull_request":
        pr = data.get("pull_request", {})
        if data.get("action") == "opened":
            collection.insert_one({
                "request_id": str(pr.get("id")),
                "author": pr.get("user", {}).get("login", "Unknown"),
                "action": "PULL REQUEST",
                "from_branch": pr.get("head", {}).get("ref"),
                "to_branch": pr.get("base", {}).get("ref"),
                "timestamp": pr.get("created_at")
            })
        elif data.get("action") == "closed" and pr.get("merged"):
            collection.insert_one({
                "request_id": str(pr.get("id")),
                "author": pr.get("merged_by", {}).get("login", "Unknown"),
                "action": "MERGE",
                "from_branch": pr.get("head", {}).get("ref"),
                "to_branch": pr.get("base", {}).get("ref"),
                "timestamp": pr.get("merged_at")
            })

    elif event == "create" and data.get("ref_type") == "branch":
        collection.insert_one({
            "request_id": data.get("ref"),
            "author": data.get("sender", {}).get("login", "Unknown"),
            "action": "BRANCH CREATED",
            "from_branch": None,
            "to_branch": data.get("ref"),
            "timestamp": datetime.utcnow().isoformat()
        })

    return "", 204

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def get_events():
    return jsonify(list(collection.find({}, {"_id": 0})))

if __name__ == "__main__":
    app.run(debug=True)
