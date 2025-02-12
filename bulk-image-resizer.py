from PIL import Image
import os

initial_images = "images"
resized_images = "resized"

os.makedirs(resized_images, exist_ok=True)

print("The following images have been resized to size 1920 by 1080:")

for file in os.listdir(initial_images):
    if file.endswith((".jpg", ".png", ".jpeg")):
        img = Image.open(os.path.join(initial_images, file))
        img = img.resize((1920, 1080))  
        img.save(os.path.join(resized_images, file))
        print(f"{file}")


