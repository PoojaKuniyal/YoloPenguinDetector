# YOLO format should be:
#<class_id> <x_center> <y_center> <width> <height>
#All values are normalized between 0 and 1.

# Here we are normalizing it

import os
from PIL import Image

# Set your dataset paths for both train and validation
datasets = {
    "train": {
        "images_dir": r"C:\Users\Lenovo\OIDv4_ToolKit\OID\Dataset\images\train",
        "labels_dir": r"C:\Users\Lenovo\OIDv4_ToolKit\OID\Dataset\labels\train"
    },
    "validation": {
        "images_dir": r"C:\Users\Lenovo\OIDv4_ToolKit\OID\Dataset\images\validation",
        "labels_dir": r"C:\Users\Lenovo\OIDv4_ToolKit\OID\Dataset\labels\validation"
    }
}

# Process both train and validation datasets
for dataset_type, paths in datasets.items():
    images_dir = paths["images_dir"]
    labels_dir = paths["labels_dir"]

    print(f"Processing {dataset_type} dataset...")

    # Process each label file
    for label_file in os.listdir(labels_dir):
        if not label_file.endswith(".txt"):
            continue

        label_path = os.path.join(labels_dir, label_file)
        image_path = os.path.join(images_dir, label_file.replace(".txt", ".jpg"))

        # Check if corresponding image exists
        if not os.path.exists(image_path):
            print(f"Image not found for {label_file}, skipping...")
            continue

        # Get image dimensions
        with Image.open(image_path) as img:
            img_width, img_height = img.size

        # Read original labels
        with open(label_path, 'r') as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                continue  # Skip malformed lines
            cls, x_center, y_center, width, height = map(float, parts)

            # Normalize
            x_center /= img_width
            y_center /= img_height
            width /= img_width
            height /= img_height

            # Round to 6 decimals
            new_line = f"{int(cls)} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"
            new_lines.append(new_line)

        # Overwrite with normalized labels
        with open(label_path, 'w') as f:
            f.writelines(new_lines)

    print(f"✅ Label conversion complete for {dataset_type} dataset.")

print("All labels processed successfully!")