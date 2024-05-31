#crop the bottom of every image in the dataset to remove the watermark from thispersondoesnotexist.com and avoid the model to predict the watermark

path = "dataset/1000/real"
cropped_path = "dataset/1000/real_cropped"

import os
import numpy as np
from PIL import Image   

for filename in os.listdir(path):
    image = Image.open(os.path.join(path, filename))
    width, height = image.size
    left = 0
    right = width
    top = 0
    bottom = height - 30
    image = image.crop((left, top, right, bottom))
    image.save(os.path.join(cropped_path, filename))