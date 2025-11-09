import albumentations as A
import cv2
import os
from tqdm import tqdm

# === CONFIG ===
INPUT_DIR = "Dataset"
OUTPUT_DIR = "AugmentedDataset"
AUGMENTATIONS_PER_IMAGE = 3

# === DEFINE AUGMENTATION PIPELINE ===
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
    A.RandomRotate90(p=0.5),
    A.ShiftScaleRotate(
        shift_limit=0.05,  # small translation
        scale_limit=0.0,   # no zoom
        rotate_limit=15,   # slight rotation
        border_mode=cv2.BORDER_REFLECT,  # keep full image in frame
        p=0.5
    ),
    A.RandomBrightnessContrast(p=0.4),
    A.HueSaturationValue(p=0.4),
    A.GaussianBlur(p=0.3),
])

os.makedirs(OUTPUT_DIR, exist_ok=True)

for class_name in os.listdir(INPUT_DIR):
    class_input_path = os.path.join(INPUT_DIR, class_name)
    class_output_path = os.path.join(OUTPUT_DIR, class_name)

    if not os.path.isdir(class_input_path):
        continue

    os.makedirs(class_output_path, exist_ok=True)

    for img_name in tqdm(os.listdir(class_input_path), desc=f"Processing {class_name}"):
        input_path = os.path.join(class_input_path, img_name)
        image = cv2.imread(input_path)
        if image is None:
            continue

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Save the original image too
        output_path = os.path.join(class_output_path, f"{img_name}.jpg")
        cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        # === CREATE 3 AUGMENTED VERSIONS ===
        for i in range(AUGMENTATIONS_PER_IMAGE):
            augmented = transform(image=image)
            aug_image = augmented["image"]

            output_name = f"{os.path.splitext(img_name)[0]}_aug_{i+1}.jpg"
            output_path = os.path.join(class_output_path, output_name)
            cv2.imwrite(output_path, cv2.cvtColor(aug_image, cv2.COLOR_RGB2BGR))
