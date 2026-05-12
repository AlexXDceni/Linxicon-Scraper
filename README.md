# 🧩 Linxicon AI Hinter & Scraper

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Powered by Gemini](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated bridge-builder for the word association game **Linxicon**. This tool utilizes browser automation and JavaScript interception to extract live game data, leveraging the **Google Gemini API** to calculate the perfect semantic link between word groups.

---

## 🚀 Overview

Linxicon is a game of semantic leaps. This tool automates the "bridge-building" process by:
1.  **Extracting** live game state via browser console injection.
2.  **Analyzing** word groups using Large Language Models.
3.  **Solving** the semantic gap by suggesting words that link Group A and Group B.

---

## 🛠️ Requirements

### 🐍 Python Environment
*   **Python 3.9+**
*   **Dependencies:**
    ```bash
    pip install pygetwindow pyautogui pyperclip google-genai python-dotenv
    
---

## ⚙️ How It Works

The project is built on a modular three-tier architecture:

### 1. The Scraper (`screen_view.py`)
The "engine" of the project. It handles the browser-level heavy lifting:
*   **Window Focus:** Locates the "Practice" tab and brings it to the foreground.
*   **JS Injection:** Opens DevTools (`F12`) and injects a custom fetch interceptor to monitor the `/api/updateGame` endpoint.
*   **The Filler Strategy:** Inputs a random word to force a game state update.
*   **Data Extraction:** Captures the JSON payload and copies it to the clipboard.

### 2. The AI Strategist (`ai_chat.py`)
The "brain" that processes semantic logic via Gemini:
*   **Contextual Prompting:** Instructs the model on Linxicon-specific logic.
*   **Semantic Bridging:** Identifies the "Meeting Point" between clusters.
*   **Noise Filtering:** Strips out "Disconnected" words to focus only on the winning path.

### 3. The Orchestrator (`main.py`)
The entry point that ties the scraper and AI together, validating data and delivering the final hint to your terminal.

---

## 📂 Project Structure

| File | Responsibility |
| :--- | :--- |
| **`main.py`** | Coordination and execution flow. |
| **`screen_view.py`** | Browser automation and data scraping. |
| **`ai_chat.py`** | API management and semantic processing. |
| **`.env`** | Secure storage for API keys. |

---

## ⚠️ Troubleshooting

*   **"Tab not found":** Ensure your Linxicon browser tab is active and named exactly "Practice."
*   **JSON Format Error:** If the script copies too fast, increase the `time.sleep()` values in `screen_view.py`.
*   **Automation Focus:** Do not move your mouse while the script is running; it uses `pyautogui` to mimic physical hardware inputs.

---

## ⚖️ Disclaimer

This tool is intended for **educational and research purposes**. Use it to explore web scraping and AI integration. Please respect the terms of service of the game developers and play responsibly!
