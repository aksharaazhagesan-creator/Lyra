# Lyra

A Python-based AI voice assistant designed to understand natural language commands and perform actions on a Mac.

## Features

- 🎤 Voice input
- 🔊 Text-to-speech responses
- 🧠 LLM-powered command understanding
- 📂 Open folders and files
- 🚀 Launch applications
- 📁 Open projects
- 🌐 Web search
- 🧩 Modular command architecture
- ⚙️ Configurable local paths

## Architecture

Lyra is divided into several components:

- `speech.py` — handles speech recognition and text-to-speech
- `assistant.py` — main assistant loop
- `brain/` — handles LLM interaction and command routing
- `commands/` — contains Lyra's executable actions
- `dispatcher.py` — sends LLM-selected tools to the correct command
- `config/` — stores configurable application and path settings
- `web/` — handles web search
- `utils/` — utility functions

## Tech Stack

- Python
- SpeechRecognition
- Edge TTS
- Gemini API
- macOS native tools
- Git / GitHub

## Setup

Clone the repository:

```bash
git clone https://github.com/aksharaazhagesan-creator/Lyra.git
cd Lyra
