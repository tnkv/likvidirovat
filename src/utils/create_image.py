from PIL import Image, ImageFont, ImageDraw
import math
import io


def likvidirovat(input_bytes) -> bytes:
    image = Image.open(io.BytesIO(input_bytes))  # Укажите путь к вашей картинке

    width, height = image.size

    text_to_be_rotated = 'ЛИКВИДИРОВАН'
    message_length = len(text_to_be_rotated)

    FONT_RATIO = 2.5
    DIAGONAL_PERCENTAGE = .5
    diagonal_length = int(math.sqrt((width ** 2) + (height ** 2)))
    diagonal_to_use = diagonal_length * DIAGONAL_PERCENTAGE
    font_size = int(diagonal_to_use / (message_length / FONT_RATIO))
    font = ImageFont.truetype('src/resources/impact.ttf', font_size)

    mark_width, mark_height = font.getsize(text_to_be_rotated)
    watermark = Image.new('RGBA', (mark_width, mark_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)
    draw.text((0, 0), text=text_to_be_rotated, font=font, fill=(255, 0, 0, 255))
    angle = math.degrees(math.atan(height / width))
    watermark = watermark.rotate(angle, expand=True)

    # merge
    wx, wy = watermark.size
    px = int((width - wx) / 2)
    py = int((height - wy) / 2)
    image.paste(watermark, (px, py, px + wx, py + wy), watermark)

    likvidirovano_image = io.BytesIO()
    image.save(likvidirovano_image, format='PNG')

    return likvidirovano_image.getvalue()
