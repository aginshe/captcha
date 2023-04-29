from PIL import Image, ImageDraw, ImageFont
import random
import string
import uuid
import os
import cv2
import os
import numpy as np


current_directory = os.path.dirname(os.path.abspath(__file__))
fonts_directory = os.path.join(current_directory, 'fonts')

def generate_captcha(characters, length=5, font_paths=None, font_size=24, width=150, height=50, margin=5, vertical_offset=10):
    if font_paths is None:
        font_paths = [
            os.path.join(fonts_directory, 'arial.ttf'),
            os.path.join(fonts_directory, 'mytype.ttf'),
        ]
    image = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    char_spacing = (width - 2 * margin) // length

    chars = ""
    for i in range(length):
        random_font_path = random.choice(font_paths)
        font = ImageFont.truetype(random_font_path, font_size)

        char = random.choice(characters)
        x = margin + i * char_spacing
        y = ((height - font_size) // 2) + random.randint(-vertical_offset, vertical_offset)
        draw.text((x, y), char, font=font, fill=(0, 0, 0))
        chars = chars + char
    return image, chars
