import requests
import json

# Your Brave Search API key
api_key = "BSAKX9fLyuevUrUhSygp_7RCgJWQcsh"

# Set up the request
headers = {
    "Accept": "application/json",
    "X-Subscription-Token": api_key
}

# Parameters for news search
params = {
    "q": "Bengal Riots in April 2025",  # Your search query for news topics
    "count": 10,        # Number of results to return
    "freshness": "week" # Time period (day, week, month)
}

# Brave Search API endpoint for news
url = "https://api.search.brave.com/res/v1/news/search"

# # Make the GET request
# response = requests.get(url, headers=headers, params=params)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse and display the results
#     news_results = response.json()
    
####################################################################

import httpx

async def brave_search_results(news: str) -> str:
    """Fetch search results from brave search engine"""
    headers = {
    "Accept": "application/json",
    "X-Subscription-Token": api_key}

    # Parameters for news search
    params = {
    "q": {news},  # Your search query for news topics
    "count": 10,        # Number of results to return
    "freshness": "week" # Time period (day, week, month)
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.search.brave.com/res/v1/news/search", headers=headers, params=params)
        return response.text
    


if __name__ == "__main__":
    import asyncio
    
    async def main():
        weather_data = await brave_search_results("Bengal Riots in April 2025")
        print(weather_data)
    
    asyncio.run(main())
