import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/abdullah-zubair/WheelsMasail/Web Scraping/textPreprocessing/Threads_and_title.csv'

df = pd.read_csv(file_path)
category_counts = df['Category'].value_counts()
threshold_count = 0.04 * category_counts.sum()
categories_to_combine = category_counts[category_counts < threshold_count].index

df['Category'] = df['Category'].replace(categories_to_combine, 'Other')
category_counts = df['Category'].value_counts()

category_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, legend=False)
plt.title('Distribution of Car Categories in the Dataset')
plt.show()
