import requests
from config import settings

class Meteo:
    def __init__(self, weather_api_key: str, location: str):
        self.weather_api_key = weather_api_key
        self.location = location

    def get_weather_uv(self):
        api_url = f"http://api.weatherapi.com/v1/current.json?key={self.weather_api_key}&q={self.location}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            uv_index = data['current']['uv']
            return uv_index
        else:
            raise Exception(f"Error fetching weather data: {response.status_code} - {response.text}")

    def get_forecast_uv(self):
        api_url = f"http://api.weatherapi.com/v1/forecast.json?key={self.weather_api_key}&q={self.location}&days=2"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            forecast_today = data['forecast']['forecastday'][0]['hour']
            forecast_tomorrow = data['forecast']['forecastday'][1]['hour']

            uv_list_hour = [[], []]
            for hour in forecast_today:
                uv_list_hour[0].append(hour['uv'])
            for hour in forecast_tomorrow:
                uv_list_hour[1].append(hour['uv'])
            return uv_list_hour
        else:
            raise Exception(f"Error fetching forecast data: {response.status_code} - {response.text}")

    def should_i_put_sunscreen_right_now(self):
        uv_index = self.get_weather_uv()

        if uv_index < 3:
            return False
        return True

    def hours_above_uv_threshold(self, threshold: int = 3):
        uv_list_hour = self.get_forecast_uv()
        sunscreen_hours = []
        for day in uv_list_hour:
            start_sunscreen = 0
            end_sunscreen = 0
            hour = 0
            
            while end_sunscreen == 0 and hour < len(day)-1:
                if day[hour] >= threshold and start_sunscreen == 0: 
                    start_sunscreen = hour
                if day[hour] < threshold and start_sunscreen != 0:
                    end_sunscreen = hour
                hour += 1
            
            sunscreen_hours.append((start_sunscreen,end_sunscreen))

        return sunscreen_hours

    def max_uv_today(self):
        uv_list_hour = self.get_forecast_uv()[0]
        return max(uv_list_hour)


if __name__ == "__main__":
    # Example usage
    meteo = Meteo(settings.api_key, "Brest, France")
    try:
        uv_index = meteo.get_weather_uv()
        print(f"current UV Index : {uv_index}")
        print(meteo.should_i_put_sunscreen_right_now())
        print(meteo.get_forecast_uv())
        print(meteo.hours_above_uv_threshold())
        print(meteo.max_uv_today())
    except Exception as e:
        print(e)