# move the first 1000 images to a folder
import os
import shutil

real_images_dir = "dataset/100/real"
ai_images_dir = "dataset/100/fake"

real_images = os.listdir(real_images_dir)
ai_images = os.listdir(ai_images_dir)

for i in range(30):
    shutil.copy(os.path.join(real_images_dir, real_images[i]), "dataset/30/real")
    shutil.copy(os.path.join(ai_images_dir, ai_images[i]), "dataset/30/fake")

    