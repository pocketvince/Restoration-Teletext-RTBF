import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

directory = 'teletexte_images'

file_list = [f for f in os.listdir(directory) if f.endswith('.gif')]

data = []
for file_name in file_list:
    parts = file_name.split('_')
    date = parts[0]
    page_number = parts[1]
    data.append((date, page_number))

df = pd.DataFrame(data, columns=["Date", "Page"])

df_pivot = df.pivot_table(index='Date', columns='Page', aggfunc=lambda x: 1, fill_value=0)

custom_cmap = ['#FF5050', '#70AD47']

plt.figure(figsize=(15, 10))
sns.heatmap(df_pivot, cmap=custom_cmap, cbar=False, linewidths=0.5, linecolor='black')

plt.title('Exported teletext page', fontsize=18)
plt.xlabel('Page Numbers', fontsize=12)
plt.ylabel('Dates', fontsize=12)

plt.gca().xaxis.set_label_position('top')
plt.gca().xaxis.tick_top()
plt.xticks(rotation=90)

output_path = 'map_teletext.png'
plt.savefig(output_path)

print(f"Heatmap saved to {output_path}")

