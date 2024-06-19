from PIL import Image, ImageDraw, ImageFont

def generate_meme(image_path, top_text, bottom_text, output_path, font_path='arial.ttf', font_size=40, text_color='white'):
    
    img = Image.open(image_path)

    
    draw = ImageDraw.Draw(img)

    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    
    width, height = img.size
    top_text_position = (width // 2, 10)
    bottom_text_position = (width // 2, height - font_size - 10)

    
    def draw_text(draw, text, position, font, max_width):
        lines = []
        words = text.split()
        while words:
            line = ''
            while words and font.getbbox(line + words[0])[2] <= max_width:
                line += (words.pop(0) + ' ')
            lines.append(line)

        y = position[1]
        for line in lines:
            text_width, text_height = font.getbbox(line)[2], font.getbbox(line)[3]
            draw.text(((width - text_width) / 2, y), line, font=font, fill=text_color)
            y += text_height

    
    draw_text(draw, top_text, top_text_position, font, width)
    draw_text(draw, bottom_text, bottom_text_position, font, width)

    
    img.save(output_path)


blank_image_path = "input.jpg"
output_image_path = "output_meme.jpg"


blank_image = Image.new('RGB', (500, 500), color = 'white')
blank_image.save(blank_image_path)


generate_meme(blank_image_path, 'Top Text', 'Bottom Text', output_image_path)

output_image_path
