import json
from PIL import Image

def render_pixel_art_to_png(json_file, output_file, pixel_size=10):
    # Load pixel art from JSON
    with open(json_file, 'r') as file:
        pixel_art = json.load(file)['art']

    # Calculate the size of the output image
    width = len(pixel_art[0]) * pixel_size
    height = len(pixel_art) * pixel_size

    # Create a new image with a white background
    img = Image.new('RGB', (width, height), 'white')
    pixels = img.load()

    # Define colors for different commit counts (adjusted for correct GitHub-like colors)
    # Lighter colors for fewer commits, darker for more commits
    colors = {
        0: (235, 237, 240),  # No commits - light gray (background)
        1: (214, 230, 133),  # Few commits - lighter green
        2: (140, 198, 101),  # Some commits - medium green
        3: (68, 163, 64),    # Many commits - dark green
        4: (30, 104, 35)     # Most commits - darkest green
    }

    # Render the pixel art
    for y, row in enumerate(pixel_art):
        for x, commit_count in enumerate(row):
            color = colors.get(commit_count, (255, 0, 0))  # Default to red for unexpected values
            for dy in range(pixel_size):
                for dx in range(pixel_size):
                    pixels[x*pixel_size + dx, y*pixel_size + dy] = color

    # Save the image
    img.save(output_file)

if __name__ == '__main__':
    render_pixel_art_to_png('pixel_art.json', 'pixel_art.png')