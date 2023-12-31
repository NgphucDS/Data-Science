# -*- coding: utf-8 -*-
"""B22DCAT224

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OXhjpZrTfH3qv2omnq5j1nLajzAPsb-o
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive',force_remount=True)

data =pd.read_csv("/content/drive/MyDrive/Nguyễn Hữu Phúc b2/AB_NYC_2019 (1).csv")
data

"""### *Bài 1: Vẽ biểu đồ cột cho neighborhood group*"""

print("BAI 1")
bars=data['neighbourhood_group'].value_counts()
plt.barh(bars.index,bars.values)
plt.title("Bar chart")
plt.ylabel("Neighborhood")
plt.show()

"""### *Bài 2: Tạo histogram cho neighborhood*"""

print("BAI 2")
plt.hist(data['neighbourhood'])
plt.title('Histogram')
plt.show()

"""### *Bài 3:Biểu diễn mối liên hệ giữa neighbourgroup và Availability của các phòng*"""

from google.colab import drive
drive.mount('/content/drive')

print("BAI 3")
plt.figure(figsize=(10, 6))  # Adjust the figure size as desired
sns.barplot(x="neighbourhood_group", y="availability_365", data=data)

# Add labels and title
plt.xlabel("Neighbourhood Group")
plt.ylabel("Availability")
plt.title("Availability by Neighbourhood Group")

# Show the plot
plt.show()

"""### *Bài 4: Vẽ bản đồ (scatter plot) của neighborhood dựa theo tọa độ lat lon*"""

print("BAI 4")
plt.figure(figsize=(20, 10))
sns.scatterplot(x='latitude', y='longitude', data=data,hue='neighbourhood')
plt.show()

"""### *Bài 5 :Sử dụng heatmap để biểu diễn mối quan hệ (correlation) giữa tất cả các thuộc tính trong dữ liệu*"""

data.corr()

print("BAI 5")
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(data.corr(), cmap=cmap)