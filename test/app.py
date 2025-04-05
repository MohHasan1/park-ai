import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inference.Model import ParkAI
from inference.ImageProcessor import ImageProcessor
from inference.FileDB import FileDB
import os

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, '..', 'inference', 'park_ai.pt')
image_path = os.path.join(script_dir, '..', 'shared', 'images', 'park_3.webp')

model = ParkAI()
processor = ImageProcessor()
db = FileDB()

img = processor.add_image(image_path)

print("🧠 Running prediction...")
results = model.predict(img)

print("📷 processing image...")
annot_img = processor.annotate_image(results)

print("✅ Occupied Spots:", processor.get_occupied_spots())

index =  db.read("index") if db.read("index") else 0
updated_index = index + 1
db.update("index", updated_index) 

processor.save_and_show(f"./inference/output/output{updated_index}.jpg", show=True)
print(f"💾 Image saved to: output{updated_index}.jpg")