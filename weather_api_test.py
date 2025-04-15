# import requests

city = "London"
api_key = "b552cfe4d458442296475614251504"  # Replace with your actual WeatherAPI.com API key
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(f"Current weather in {city}:")
#     print(f"Temperature: {data['current']['temp_c']}°C")
#     print(f"Weather: {data['current']['condition']['text']}")
#     print(f"Humidity: {data['current']['humidity']}%")
#     print(f"Wind: {data['current']['wind_kph']} km/h")
#     print(f"Feels like: {data['current']['feelslike_c']}°C")
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)

import httpx

async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no")
        return response.text
    


if __name__ == "__main__":
    import asyncio
    
    async def main():
        weather_data = await fetch_weather("London")
        print(weather_data)
    
    asyncio.run(main())

