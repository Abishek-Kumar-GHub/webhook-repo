# 🔔 GitHub Webhook Listener & UI

This project demonstrates a complete GitHub Webhook integration using Flask and MongoDB. It listens for GitHub repository events (Push, Pull Request, Merge, and Branch Creation), stores them in MongoDB, and displays them in real time via a simple frontend that polls the server every 15 seconds.

---

## 🚀 Features

- Receives GitHub webhook events:  
  ✅ Push  
  ✅ Pull Request (opened)  
  ✅ Merge (closed & merged)  
  ✅ Branch Created

- Stores event data in MongoDB
- Frontend updates automatically (every 15 seconds)
- Simple and clean UI

---

## 🛠️ Tech Stack

- **Backend**: Python + Flask  
- **Database**: MongoDB  
- **Frontend**: HTML + JavaScript (vanilla)  
- **Polling Mechanism**: JavaScript `setInterval`

---

## 📦 Project Structure
```bash
webhook-repo/
│
├── templates/
│ └── index.html # Web interface
│
├── static/
│ └── script.js # Frontend polling & rendering
│
├── app.py # Flask backend
├── requirements.txt # Python dependencies (Flask, pymongo)
└── README.md # You're reading it!
```

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/webhook-repo.git
cd webhook-repo
```

### 2. Install dependencies
Make sure Python and MongoDB are installed and running locally.

```bash
pip install -r requirements.txt
```

requirements.txt should include:
```nginx
Flask
pymongo
```

### 3. Run Flask app
```bash
python app.py
```

It will start on http://127.0.0.1:5000

## 🔗 Set Up GitHub Webhook
- Go to your GitHub repo → Settings → Webhooks

- Click "Add webhook"

- Payload URL: http://<your-ip>:5000/webhook (use ngrok if needed)

- Content type: application/json

- Events to trigger:
✅ Push
✅ Pull Request
✅ Create

- Click Add webhook

If you're working locally and want to receive webhooks from GitHub, expose your Flask server using ngrok:

```bash
ngrok http 5000
```

## 📊 UI Preview
### Visit http://localhost:5000

The events will appear as a list:

``` html
Abishek pushed to "main" on Sun, 06 Jul 2025 06:32:12 GMT
Abishek submitted a pull request from "feature" to "main" on ...
```

##  📚 Event Schema (stored in MongoDB)
```json
{
  "request_id": "commit_or_pr_id",
  "author": "username",
  "action": "PUSH | PULL REQUEST | MERGE | BRANCH CREATED",
  "from_branch": "feature-branch (optional)",
  "to_branch": "main",
  "timestamp": "ISO string"
}
```

## ✅ To Do
 - **Add authentication**

 - **Show event icons or types visually**

 - **Add timestamps in local timezone**

 - **Deploy with Docker / Gunicorn for production**

## 🧠 Credits

Created by Abishek Kumar as a GitHub integration showcase.
Pull requests welcome!

## Screenshots

![Screenshot_2025-07-06_12_11_27](https://github.com/user-attachments/assets/6abac03f-f0f0-4597-8090-e2f695a7230c)
