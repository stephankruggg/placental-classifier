import os
import random
import shutil
from math import ceil

# === CONFIG ===
INPUT_DIR = "AugmentedDataset"  # your folder with class subfolders
OUTPUT_DIR = "DatasetSplit"     # output folder
SPLIT = {"train": 0.8, "valid": 0.1, "test": 0.1}
random.seed(42)

# === CREATE OUTPUT FOLDERS ===
for split_name in SPLIT.keys():
    os.makedirs(os.path.join(OUTPUT_DIR, split_name), exist_ok=True)

# === LOOP OVER CLASSES ===
for class_name in os.listdir(INPUT_DIR):
    class_input_path = os.path.join(INPUT_DIR, class_name)
    if not os.path.isdir(class_input_path):
        continue

    # Get all images in class
    images = [f for f in os.listdir(class_input_path)
              if f.lower().endswith((".jpg", ".jpeg", ".png", ".jfif"))]
    
    if not images:
        continue

    random.shuffle(images)

    n = len(images)
    n_valid = max(1, ceil(SPLIT["valid"] * n))
    n_test  = max(1, ceil(SPLIT["test"] * n))
    n_train = n - n_valid - n_test
    if n_train < 1:  # ensure at least one image in train
        n_train = 1
        if n_valid > 1:
            n_valid -= 1
        elif n_test > 1:
            n_test -= 1

    # Split images
    train_imgs = images[:n_train]
    valid_imgs = images[n_train:n_train+n_valid]
    test_imgs  = images[n_train+n_valid:]

    # Helper to copy files
    def copy_files(img_list, split_name):
        split_class_path = os.path.join(OUTPUT_DIR, split_name, class_name)
        os.makedirs(split_class_path, exist_ok=True)
        for img in img_list:
            shutil.copy2(os.path.join(class_input_path, img),
                         os.path.join(split_class_path, img))

    # Copy images
    copy_files(train_imgs, "train")
    copy_files(valid_imgs, "valid")
    copy_files(test_imgs, "test")

    print(f"{class_name}: train={len(train_imgs)}, valid={len(valid_imgs)}, test={len(test_imgs)}")
