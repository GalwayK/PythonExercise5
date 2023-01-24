import requests
import datetime

CURRENT_DATE = datetime.datetime.now().strftime("%Y-%m-%d")
API_KEY = "WsEgjKMZeP0qBeI45nSx8LnEn4k1TjZO1p6G0JYZ"
print(CURRENT_DATE)


def get_image_of_the_day_response():
    response = requests.get(f"https://api.nasa.gov/planetary/apod?"
                            f"date={CURRENT_DATE}"
                            f"&api_key={API_KEY}")
    return response.json()


def get_image_of_the_day_image(url):
    image = requests.get(url)

    return image.content
