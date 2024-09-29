import os
import shutil
import cv2
from tqdm import tqdm
from collections import defaultdict

source_folder = "teletexte_images"
duplicate_folder = "duplicate"

if not os.path.exists(duplicate_folder):
    os.makedirs(duplicate_folder)

def images_are_identical(file1, file2):
    img1 = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(file2, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        print(f"Error : Impossible to check  {file1} or {file2}.")
        return False

    if img1.shape != img2.shape:
        return False

    difference = cv2.absdiff(img1, img2)

    return difference.sum() == 0

def move_duplicate_to_folder(filepath, page_number, subpage_number):
    folder_name = f"{page_number}_{subpage_number}"
    folder_path = os.path.join(duplicate_folder, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(filepath, os.path.join(folder_path, os.path.basename(filepath)))

file_dict = defaultdict(list)

png_files = [f for f in os.listdir(source_folder) if f.endswith(".png")]

for filename in tqdm(png_files, desc="Détection et déplacement des doublons", ncols=100):
    parts = filename.split('_')
    if len(parts) >= 3:
        page_number = parts[1]
        subpage_number = parts[2].split('.')[0]

        filepath = os.path.join(source_folder, filename)

        page_key = f"{page_number}_{subpage_number}"

        if file_dict[page_key]:
            for existing_file in file_dict[page_key]:
                existing_filepath = os.path.join(source_folder, existing_file)

                if images_are_identical(filepath, existing_filepath):
                    move_duplicate_to_folder(filepath, page_number, subpage_number)
                    break
            else:
                file_dict[page_key].append(filename)
        else:
            file_dict[page_key].append(filename)

