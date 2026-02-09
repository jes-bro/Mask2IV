import os
import re

parent_dir = "/simurgh2/projects/Mask2IV/Mask2IV/done_masks"

pattern = re.compile(r"(im_)0*(\d+)(\.jpg)$")

for root, dirs, files in os.walk(parent_dir):
    if os.path.basename(root) == "images0":
        for name in files:
            match = pattern.match(name)
            if match:
                prefix, number, ext = match.groups()
                new_name = f"{prefix}{int(number)}{ext}"

                old_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)

                if old_path != new_path:
                    os.rename(old_path, new_path)
