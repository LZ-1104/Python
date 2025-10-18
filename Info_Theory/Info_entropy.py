#导入OpenCV库
import cv2
import numpy as np
#导入Matplotlib库
import matplotlib.pyplot as plt

#读取图像
image = cv2.imread('D:/vscode/Python/Test/pic2/4.jpg', cv2.IMREAD_COLOR)#以RGB模式读取图像，
#计算图像RGBs三个通道的信息熵
def calculate_entropy(channel):
    # 计算直方图
    hist, _ = np.histogram(channel, bins=256, range=(0, 256))
    # 归一化直方图
    hist = hist / hist.sum()
    # 计算熵
    entropy = -np.sum(hist * np.log2(hist + 1e-10))  # 加上一个小常数以避免log(0)
    return entropy
# 分离图像的RGB通道
b_channel, g_channel, r_channel = cv2.split(image)
# 计算每个通道的熵
b_entropy = calculate_entropy(b_channel)
g_entropy = calculate_entropy(g_channel)
r_entropy = calculate_entropy(r_channel)
print(f'Blue Channel Entropy: {b_entropy}')
print(f'Green Channel Entropy: {g_entropy}')
print(f'Red Channel Entropy: {r_entropy}')
# 显示图像
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 绘制各通道熵值的柱状图
channels = ['Blue', 'Green', 'Red']
entropies = [b_entropy, g_entropy, r_entropy]
plt.bar(channels, entropies, color=['blue', 'green', 'red'])
plt.xlabel('Color Channels')
plt.ylabel('Entropy')
plt.title('Entropy of RGB Channels')
plt.show()

