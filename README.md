Lyra 1.0

A Python-based AI voice assistant for macOS, powered by an LLM and modular local automation.

Lyra converts natural-language voice commands into structured actions, routes them to Python commands, and executes them on the user's Mac.

✨ Features
🎙️ Voice interaction — speech input and text-to-speech responses
🧠 LLM-powered understanding — uses Gemini to interpret natural-language requests
🧭 Command routing — separates intent recognition from command execution
📂 File & folder management — search for and open files and folders
🚀 Application launching — launch configured macOS applications
📁 Project management — open configured projects
🌐 Web search — perform browser-based searches
▶️ YouTube search — open YouTube searches directly
🕐 Date & time commands
⚙️ Configurable local paths for applications, folders, and projects
🏗️ Architecture
Voice Input
    ↓
Speech Recognition
    ↓
Lyra Assistant
    ↓
Gemini LLM
    ↓
Router
    ↓
Dispatcher
    ↓
Python Command
    ↓
macOS Action
    ↓
Text-to-Speech

The LLM handles natural-language understanding, while Python handles actual system operations.

This keeps AI reasoning separate from executable actions.

🛠️ Tech Stack
Python
Google Gemini API / Google GenAI SDK
Pydantic
SpeechRecognition
Edge TTS
python-dotenv
macOS system utilities
📁 Project Structure
Lyra/
├── brain/
│   ├── llm.py
│   ├── router.py
│   └── prompts/
├── commands/
│   ├── date.py
│   ├── file_manager.py
│   ├── folder_manager.py
│   ├── hello.py
│   ├── launcher.py
│   ├── project_manager.py
│   └── time.py
├── config/
├── utils/
├── web/
├── assistant.py
├── dispatcher.py
├── main.py
├── speech.py
├── requirements.txt
├── .env.example
└── .gitignore
🚀 Installation
1. Clone
git clone https://github.com/aksharaazhagesan-creator/Lyra.git
cd Lyra
2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure the API key

Create your local .env file:

cp .env.example .env

Then add:

GEMINI_API_KEY=your_api_key_here

Never commit your .env file or API key.

5. Configure local paths

Create your personal configuration files from the provided .example.json files and add your own application, folder, and project paths.

6. Run Lyra
python main.py
🔐 Security

Lyra keeps sensitive and machine-specific information outside the public repository.

Local files such as:

.env
config/folders.json
config/projects.json

are excluded from Git.

API keys are loaded through environment variables rather than being hard-coded into the source code.

🗺️ Roadmap

Lyra 1.0 is the foundation for a larger personal AI agent.

🧠 Memory & Context — persistent memory and context-aware conversations
🤖 Agentic Workflows — task planning, tool selection, multi-step execution, and recovery
🖥️ Desktop Agent — deeper macOS control and complete workflows
🎯 Specialized Modes — Study, Coding, Research, Focus, and Agent modes
🌐 Tool Integrations — external APIs, real-time information, and productivity services
👁️ Computer Vision — screen understanding and vision-assisted automation
🔐 Security & Identity — authentication, permissions, and safeguards
🖼️ Dedicated Interface — GUI and eventually a more immersive interface
Long-term vision
Voice Assistant
       ↓
Context-Aware Assistant
       ↓
AI Agent
       ↓
Personal Desktop Agent

The goal is to evolve Lyra from executing individual commands into an AI system that can understand goals, remember context, plan tasks, use tools, interact with the computer, and verify its actions.

📌 Status

Version: 1.0.0
Platform: macOS
Language: Python
Status: Initial version completed
