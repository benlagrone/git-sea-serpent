from PIL import Image
import numpy as np

def image_to_pixel_art(path, output_size=(52, 7), shades=4):
    # Load the image
    img = Image.open(path)
    
    # Convert to grayscale
    img_gray = img.convert('L')
    
    # Resize to fit GitHub's contributions graph dimensions
    img_resized = img_gray.resize(output_size)
    
    # Convert to numpy array
    img_array = np.array(img_resized)
    
    # Normalize the array to a scale of 0 to shades-1
    # This maps grayscale values to a specific number of commits
    # The higher the number, the more commits it represents
    max_value = 255
    img_normalized = np.floor((img_array / max_value) * shades).astype(int)
    
    # Convert to list of lists
    pixel_art = img_normalized.tolist()
    
    return pixel_art

# Example usage
path = 'image/serpent.png'
pixel_art = image_to_pixel_art(path, shades=4)  # Adjust 'shades' as needed

# Optionally, save to a JSON file
import json
with open('pixel_art.json', 'w') as f:
    json.dump({"art": pixel_art}, f)

print("Pixel art array has been saved to pixel_art.json")