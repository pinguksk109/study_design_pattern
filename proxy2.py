import time
from typing import Dict
from abc import ABC, abstractmethod

class WeatherAPI(ABC):
    @abstractmethod
    def get_weather(self, location: str) -> str:
        pass

class RealWeatherAPI(WeatherAPI):
    def get_weather(self, location: str) -> str:
        print(f"Fetching weather data for {location} from API...")
        time.sleep(2)
        return f"Weather data for {location}"
    
class WeatherAPIProxy(WeatherAPI):
    def __init__(self, real_api: RealWeatherAPI):
        self.real_api = real_api
        self.cache: Dict[str, str] = {}
        self.last_access_time: Dict[str, float] = {}
        self.rate_limit_interval = 5

    def get_weather(self, location: str) -> str:
        current_time = time.time()
        cached_data = self.cache.get(location)
        last_access = self.last_access_time.get(location, 0)

        if cached_data and (current_time - last_access < self.rate_limit_interval):
            print(f"Returning cached data for {location}.")
            return cached_data
        
        data = self.real_api.get_weather(location)
        self.cache[location] = data
        self.last_access_time[location] = current_time
        return data
    
def main():
    real_api = RealWeatherAPI()
    weather_proxy = WeatherAPIProxy(real_api)
    
    print(weather_proxy.get_weather("Tokyo"))
    
    print(weather_proxy.get_weather("Tokyo"))
    
    print("Waiting for rate limit interval to expire...")
    time.sleep(6)
    
    print(weather_proxy.get_weather("Tokyo"))

main()