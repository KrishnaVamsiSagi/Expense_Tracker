# 💸 Expense Tracker Web App

A simple and clean web-based **Expense Tracker** built using Python Flask, HTML, CSS, and JavaScript. It allows users to:

- Set a monthly **total budget**
- Add categorized **daily expenses**
- View all added expenses in a **table**
- See the **remaining budget** dynamically
- Deploy easily with **Docker**



## 🚀 Features

- 💡 Set your total monthly budget
- 📝 Add expenses with description, category, and amount
- 📊 View all expenses in a responsive table
- 📉 Real-time update of remaining budget
- 📦 Run anywhere using Docker

## 🛠️ Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Storage**: Local JSON file (`data.json`)
- **Containerization**: Docker

## 📁 Project Structure
expense-tracker/
├── app.py               # Flask backend logic
├── Dockerfile           # Docker container instructions
├── requirements.txt     # Python package dependencies
├── data.json            # Local JSON file for storing expenses and budget

├── templates/           # HTML templates for Flask
│   └── index.html       # Main user interface

└── static/              # Static assets (CSS, JS, images)
    └── style.css        # Custom styling for the UI


## ⚙️ How to Run Locally

### 🔧 Prerequisites

- Python 3.8+
- Flask (`pip install flask`)

### ▶️ Run without Docker

```bash
python app.py

```
## How to run with Docker
1. Build Docker Image
  ```bash
docker build -t expense-tracker .
```
2. Run the Container
```bash
docker run -p 80:80 expense-tracker
```
Visit: http://localhost
