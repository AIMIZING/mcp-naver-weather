from typing import Any
import requests
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP
import sys

# Initialize MCP server
mcp = FastMCP("weather")

# Tool for fetching weather information from Naver
@mcp.tool()
def get_naver_weather(region: str) -> str:
    """
    Retrieves weather information for a specific region from Naver.

    Args:
        region: The name of the region to query (e.g., Seoul, Busan)
    """
    try:
        # Access Naver search results page
        search_url = f"https://search.naver.com/search.naver?query={region}+날씨"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Parse key weather information
        temperature = soup.select_one(".temperature_text > strong")
        status = soup.select_one(".weather_main")  # Weather condition: sunny, cloudy, etc.

        if not temperature or not status:
            return f"Unable to retrieve weather information for [{region}]. Please check the region name."

        temp_text = temperature.get_text(strip=True)
        status_text = status.get_text(strip=True)

        return f"The current weather in {region} is '{status_text}', and the temperature is {temp_text}."

    except Exception as e:
        return f"[Error] An issue occurred while fetching weather information: {str(e)}"

# Run the MCP server
if __name__ == "__main__":
    print("🔧 MCP server is starting", file=sys.stderr)
    mcp.run(transport="stdio")
