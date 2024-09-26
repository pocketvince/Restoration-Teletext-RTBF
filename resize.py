import os
import numpy as np
from PIL import Image
import cv2
from tqdm import tqdm

input_dir = './teletexte_images'
output_dir = './upscaled_images'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

scale_factor = 4

def upscale_image_with_lanczos(input_path, scale_factor=4):
    img = Image.open(input_path)
    img = img.convert('RGB')
    img_resized = img.resize((img.width * scale_factor, img.height * scale_factor), Image.LANCZOS)
    return img_resized

def enhance_colors_and_sharpen(image):
    img_array = np.array(image)
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1,  9, -1],
                                  [-1, -1, -1]])
    sharpened_img = cv2.filter2D(img_array, -1, sharpening_kernel)
    return Image.fromarray(sharpened_img)

def reduce_overall_saturation(image, reduction_factor=0.85):
    img_array = np.array(image)
    hsv_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
    hsv_img[:, :, 1] = (hsv_img[:, :, 1] * reduction_factor).clip(0, 255)
    rgb_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
    return Image.fromarray(rgb_img)

gif_files = [f for f in os.listdir(input_dir) if f.endswith('.gif')]

for filename in tqdm(gif_files, desc="Treatment in progress", ncols=100):
    img_path = os.path.join(input_dir, filename)
    
    upscaled_image = upscale_image_with_lanczos(img_path)
    
    sharpened_image = enhance_colors_and_sharpen(upscaled_image)
    
    final_image = reduce_overall_saturation(sharpened_image)
    
    new_filename = os.path.splitext(filename)[0] + '.png'
    final_image.save(os.path.join(output_dir, new_filename), format='PNG')

print("Processing complete.")

