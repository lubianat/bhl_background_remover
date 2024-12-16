from rembg import remove
from PIL import Image

# Load the input image
input_path = "input_image.jpeg"  # Replace with your input image path
output_path = "output_image.png"  # Output path with transparency

# Open the image using PIL
input_image = Image.open(input_path)

# Apply Rembg background removal
output_image = remove(input_image)

# Save the output image
output_image.save(output_path)

print(f"Background removed! Output saved to: {output_path}")
