# 🤖 AI Personal Assistant

An AI-powered personal assistant web application built using **Python, Flask, and Anthropic Claude API**. It allows users to ask questions and summarize lengthy emails through a simple web interface.

## ✨ Features

- 💬 **Ask Anything:** Get AI-generated responses to general questions.
- 📧 **Email Summarization:** Summarize lengthy emails into concise, easy-to-understand summaries.
- ⚡ **Interactive Web Interface:** Simple interface with loading indicators and dynamic responses.
- 🔐 **Environment Variable Support:** Store API credentials securely using a `.env` file.
- 🐍 **Flask Backend:** Handle requests and communicate with the Claude API.
- 🧩 **Modular Structure:** Separate HTML templates and static assets for easier maintenance.

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** Flask
- **AI Model Provider:** Anthropic Claude API
- **Frontend:** HTML, CSS, JavaScript
- **Environment Management:** python-dotenv
- **Version Control:** Git and GitHub

## 📂 Project Structure

```text
AI Assistant/
├── main.py
├── requirements.txt
├── .env                 # Local API credentials; not committed
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-personal-assistant.git
cd ai-personal-assistant
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows using Git Bash:

```bash
source .venv/Scripts/activate
```

Alternatively, in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root directory:

```dotenv
CLAUDE_API_KEY=your_anthropic_api_key
```

Replace the placeholder with your valid Anthropic API key.

**Security:** Never commit your `.env` file or expose your API key in source code.

### 5. Configure the Claude model

In `main.py`, ensure the `MODEL` variable contains a model ID currently available to your Anthropic API account.

For example:

```python
MODEL = "claude-haiku-4-5-20251001"
```

Model availability may depend on your account and API access.

### 6. Run the application

```bash
python main.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🔄 How It Works

### Ask Anything

1. The user enters a question in the web interface.
2. JavaScript sends the question to the Flask `/ask` endpoint.
3. Flask forwards the request to the Anthropic Claude API.
4. The generated answer is returned as JSON.
5. JavaScript displays the answer on the page.

### Email Summarization

1. The user pastes
