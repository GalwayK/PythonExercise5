import streamlit
import nasa_image

request = nasa_image.get_image_of_the_day_response()

image_text = request["explanation"]
image_title = request["title"]
image_url = request["hdurl"]
image_bytes = nasa_image.get_image_of_the_day_image(image_url)

image_filename = "image_of_the_day.jpg"
with open(image_filename, "wb") as image:
    image.write(image_bytes)

streamlit.title("Nasa Image of the Day")

streamlit.header(image_title)
streamlit.image(image_filename)
streamlit.write(image_text)

