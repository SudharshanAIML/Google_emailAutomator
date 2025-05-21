# Google_emailAutomator

## 📧 Google Email Automator

A Python-based tool to automate sending emails through the Gmail API. This script supports multiple recipients and file attachments, streamlining your email dispatch process.

### 🚀 Features

- **Send Emails**: Automate email sending via Gmail API.
- **Multiple Recipients**: Specify multiple email addresses.
- **Attachments**: Include one or more files as attachments.

### 🛠️ Prerequisites

- Python 3.6 or higher
- Google Cloud Project with Gmail API enabled
- OAuth 2.0 Credentials: `credentials.json` file obtained from Google Cloud Console

### 📦 Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/Google_Email_Automator.git
    cd Google_Email_Automator
    ```

2. **Set Up Virtual Environment (Optional but Recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### 🔐 Setting Up Gmail API Credentials

1. **Enable Gmail API**:
    - Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing one.
    - Go to **APIs & Services > Library**.
    - Search for "Gmail API" and enable it.

2. **Create OAuth Client ID**:
    - Go to **APIs & Services > Credentials**.
    - Click **Create Credentials > OAuth client ID**.
    - Choose **Desktop App** as the application type.
    - Download the `credentials.json` file.

3. **Place `credentials.json` in Project Directory**:
    - Move the downloaded `credentials.json` file into the root directory of your project.

### 📄 Usage

1. **Prepare Your Email Content**:
    - Edit the `email_automator.py` script to specify:
        - **Recipients**: Update the `mimeMessage['to']` field with recipient email addresses.
        - **Subject**: Set your desired email subject.
        - **Body**: Modify the `emailMsg` variable with your message content.
        - **Attachments**: Add file paths to the `file_attachments` list.

2. **Run the Script**:
    ```bash
    python email_automator.py
    ```
    - On the first run, a browser window will prompt you to authorize access to your Gmail account.
    - After authorization, a `token.json` file will be created for future access.

### 📁 File Structure

```
Google_Email_Automator/
├── credentials.json
├── email_automator.py
├── requirements.txt
└── README.md
```

### 📝 Notes

- Ensure that `credentials.json` is not exposed publicly. Add it to your `.gitignore` file to prevent accidental commits.
- The `token.json` file stores your access and refresh tokens. Keep it secure.
- And don't forgot to change the local port number before run this program
