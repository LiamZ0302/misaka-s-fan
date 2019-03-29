import numpy as np 
import matplotlib.pylab as plt
im = plt.imread("misaka.jpg")
print(im.shape) # 输出图像尺
new_im = np.zeros((1600, 827, 3), np.uint8)
new_im = new_im + 255
new_im[200:1369, :, :] = im
plt.imsave("misaka.jpg", new_im)