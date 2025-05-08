# Count objects and average bounding box size
import os
import numpy as np

label_folder = r"C:\Users\Lenovo\OIDv4_ToolKit\OID\Dataset\labels\train"  # or validation
sizes = []

for file in os.listdir(label_folder):
    if file.endswith(".txt"):
        with open(os.path.join(label_folder, file), "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                w, h = float(parts[3]), float(parts[4])
                sizes.append(w * h)

print("Average bbox size:", np.mean(sizes))
print("Smallest bbox:", np.min(sizes))
print("Largest bbox:", np.max(sizes))
