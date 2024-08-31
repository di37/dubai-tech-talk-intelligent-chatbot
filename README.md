# Memory Persistent Chatbot using OpenAI, Langchain, and Firebase

This project demonstrates how to build an intelligent chatbot with persistent memory using OpenAI, Langchain, and Firebase.

## Prerequisites

1. [Anaconda](https://www.anaconda.com/products/distribution) installed on your PC
2. [OpenAI API Key](https://platform.openai.com/api-keys)
3. Firebase credentials (Project ID and Private Key JSON file)

## Setup Firebase - Firestore Database

1. Sign in to your Google account and go to the [Firebase Console](https://console.firebase.google.com/).
2. Create a new project or select an existing one.
3. In Project Settings > Service Accounts, click "Generate new private key" to download a JSON file.
4. Place the private key JSON file in the project's root directory.
5. Create a Firestore database in your Firebase project.
6. Copy the project ID from Project Settings.

## Environment Setup

1. Create a conda environment:
   ```bash
   conda create -n chatbot-firebase python=3.12
   ```

2. Activate the conda environment:
   ```bash
   conda activate chatbot-firebase
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on `.env.example` and fill in the following variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `GOOGLE_APPLICATION_CREDENTIALS`: Path to your Firebase private key JSON file
   - `PROJECT_ID`: Your Firebase project ID

## Running the Chatbot

### Non-persistent CLI Chatbot
```bash
python workflow/non-persistent/cli/chatbot_stream.py
```

### Non-persistent UI Chatbot
```bash
python workflow/non-persistent/ui/chatbot_stream.py
```

### Memory Persistent UI Chatbot
```bash
python workflow/persistent/ui/chatbot_stream.py
```

## Features

- Intelligent conversation using OpenAI's language models
- Integration with Langchain for enhanced language processing
- Firebase Firestore for persistent memory storage
- Both CLI and UI versions available
- Stream responses for a more interactive experience

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.