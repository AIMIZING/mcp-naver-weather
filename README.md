## mcp-naver-weather
A lightweight MCP (Model Context Protocol) server that fetches real-time weather data from Naver and sends it to Claude Desktop via a local folder.

This project is intended to be used with **Claude's MCP desktop feature**, and does not require response handling — it simply delivers weather content as `.txt` files.

---

## Features

- Crawls current weather info from Naver
- Saves the result to Claude Desktop’s input folder
- Minimal setup using [uv](https://github.com/astral-sh/uv)

---

## How to Use

### 1. Install Claude Desktop (if not installed)
- Download [Claude Desktop](https://claude.ai/download) and install it.

### 2. Download `mcp-naver-weather`
**Option 1: Download as ZIP**
- Click **"Code"** > **"Download ZIP"**
- Extract the downloaded ZIP file

**Option 2: Clone with Git**
```sh
git clone https://github.com/AIMIZING/mcp-naver-weather.git
cd mcp-naver-weather
```

### 3. Set Up UV Environment
**Option 1: Manual Setup**
- Install uv (if not installed):
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
- Initialize the UV project and create a virtual environment:
```sh
uv init weather
cd weather
uv venv
.venv\Scripts\activate
```
- Install dependencies:
```sh
pip install -r requirements.txt
```

**Option 2: Automatic Setup (Windows)**
- run the included **"setup.bat"** file

### 4. Configure Claude Desktop
Open the included **"weather_config.json"** file, and copy its content.
Then, open your existing Claude Desktop configuration file and append the copied content.

To locate the Claude Desktop config file:
- Open Claude Desktop
- Go to Menu → File → Settings → Developer Mode → Edit Configuration
- This will open your current **"claude_desktop_config.json"** file
- Paste the additional content at the appropriate position (e.g. within the mcp list or relevant section)

⚠️ Before copying, make sure to replace the path
"D:\\PLACEHOLDER\\naver-weather" in weather_config.json
with your actual local project path (e.g. C:\\Users\\YourName\\Documents\\naver-weather).

⚠️ Do not overwrite the entire file — make sure to append or merge the content to avoid breaking existing configurations.

### 5. Run Claude Desktop
Launch Claude Desktop.
Once it's running, it will automatically detect and connect to the configured MCP tool.
You can now ask Claude for weather information like:
> "What's the weather in Seoul?"
