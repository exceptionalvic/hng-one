import requests
from django.http import JsonResponse
from django.conf import settings

ipinfo_api_key = settings.IPINFO_API_KEY
weather_api_key= settings.WEATHER_API_KEY


def get_client_ip_address(request):
    req_headers = request.META
    x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for_value:
        ip_addr = x_forwarded_for_value.split(',')[-1].strip()
    else:
        ip_addr = req_headers.get('REMOTE_ADDR')
    print(ip_addr)
    return ip_addr


def get_visitor_data(request):
    ip = get_client_ip_address(request)
    api_key = ipinfo_api_key 
    # url = f'http://api.ipstack.com/{ip}?access_key={api_key}'
    
    # Alternatively, for ipinfo
    url = f'http://ipinfo.io/{ip}/json?token={api_key}' 
    
    response = requests.get(url)
    data = response.json()
    print(data)

    city = data.get('city', 'Unknown')

    lat = str(data.get('loc', 'Unknown')).split(",")[0]
    lon = str(data.get('loc', 'Unknown')).split(",")[1]

    # Fetch weather data
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    print(weather_data)

    temperature = weather_data['main']['temp'] if 'main' in weather_data else 'Unknown'

    return {'ip': ip, 'city': city, 'temperature': temperature}
