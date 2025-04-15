# 🚀 Build Custom MCP Servers 📝☀️📰

## 📖 Project Description

This project demonstrates a simple MCP Servers built using the MCP `mcp[cli]` Python SDK. It provides several tools exposed through the MCP server:

*   **Note Management:** Add, read, retrieve the latest, and generate summaries of notes stored locally.
*   **Weather Information:** Fetch current weather data for a specified city using the WeatherAPI.com service.
*   **News Search:** Perform news searches using the Brave Search API.

It utilizes API keys stored in a `.env` file for external services.

## 🛠️ Setup Instructions

Follow these steps to get the FastMCP agent running:

1.  **Prerequisites:**
    *   Python 3.12 installed.
    *   A virtual environment manager (like `venv`, `pipenv`, `poetry`, or `uv`) is recommended.

2.  **Clone the Repository (if you haven't already):**
    ```bash
    # Make sure you are in the correct parent directory
    git clone https://github.com/sourangshupal/Build-Custom-MCP-Servers # Or use the current directory if already cloned
    cd Build-Custom-MCP-Servers 
    ```

3.  **Set up Virtual Environment & Install Dependencies:**
    *   Install dependencies (assuming uv, based on uv.lock, otherwise adjust for pip/poetry):
        ```bash
        uv sync
        uv lock
        source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
        ```
    *   OR
        ```bash
        pip install uv # if you don't have uv
        uv pip install -r requirements.txt # Or uv sync if using pyproject.toml directly
        # If not using uv, likely: pip install -r requirements.txt or poetry install or pip install .
        ```

4.  **Configure Environment Variables:**
    *   Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    *   Edit the newly created `.env` file and add your API keys:
        ```dotenv
        WEATHER_API_KEY="YOUR_WEATHER_API_KEY"
        BRAVE_API_KEY="YOUR_BRAVE_API_KEY"
        ```

5.  **Run the Agent:**
    *   Execute the main script:
        ```bash
        mcp install main.py
        ```
    *   The FastMCP server should be added to Claude Desktop.

        ```bash
        mcp dev main.py
        ```
    *   Debug the MCP Server

## ✨ Features

*   Note-taking capabilities (add, read, latest, summarize) 📝
*   Current weather fetching ☀️
*   Brave Search integration for news 📰
*   Configuration via `.env` file 🔑
*   Built with `mcp[cli]` ⚙️

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.
