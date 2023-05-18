from PIL import Image
from collections import defaultdict

def get_color_type(color):
    r, g, b = color
    if r > g and r > b:
        return 'Red'
    elif g > r and g > b:
        return 'Green'
    elif b > r and b > g:
        return 'Blue'
    elif r == g and g == b:
        return 'Gray'
    else:
        return 'Mixed'

def analyze_image_colors(image_path):
    image = Image.open(image_path)
    pixels = image.load()

    color_types = defaultdict(int)

    width, height = image.size
    for y in range(height):
        for x in range(width):
            color = pixels[x, y][:3]  # Extract RGB values, ignore alpha channel if present
            color_type = get_color_type(color)
            color_types[color_type] += 1

    return color_types

# Path to the image file
image_path = 'path/to/your/image.jpg'

# Analyze the image colors
color_types = analyze_image_colors(image_path)

# Print the color types and their counts
for color_type, count in color_types.items():
    print(f'{color_type}: {count}')
