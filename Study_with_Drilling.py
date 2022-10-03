import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as img

path = 'C:/Users/k5000/Videos/test'
os.chdir(path)
file_list = os.listdir(path)
jpg = [file for file in file_list if file.endswith('.png')]
case = img.imread(random.choice(jpg))
plt.imshow(case)
plt.show()

