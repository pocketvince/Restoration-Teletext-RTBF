import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import re
from matplotlib.colors import ListedColormap

folder_path = 'teletexte_images'

file_pattern = r'(\d{4})(\d{2})(\d{2})_(\d+)_(\d+)\.gif'

pages_by_month = defaultdict(set)

for filename in os.listdir(folder_path):
    match = re.match(file_pattern, filename)
    if match:
        year, month, day, page, subpage = match.groups()
        month_key = f"{year}-{month}"
        pages_by_month[month_key].add(page)

all_pages = set()
for month, pages in pages_by_month.items():
    all_pages.update(pages)

df_monthly = pd.DataFrame(0, index=pages_by_month.keys(), columns=sorted(all_pages))

for month, pages in pages_by_month.items():
    df_monthly.loc[month, list(pages)] = 1

df_filtered_monthly = df_monthly.loc[:, (df_monthly != 0).any(axis=0)]

df_filtered_monthly = df_filtered_monthly[(df_filtered_monthly.T != 0).any()]

background_color = 'black'
grid_color = '#00FF00'
text_color = '#FFFF00'

cmap_black_inside = ListedColormap([background_color, grid_color])

plt.figure(figsize=(20, 16), facecolor=background_color)
plt.imshow(df_filtered_monthly, cmap=cmap_black_inside, aspect='auto')

plt.xlabel("Page", fontsize=12, color=text_color)
plt.ylabel("Months", fontsize=12, color=text_color)
plt.title("Representation of Available Teletext Pages by Month", fontsize=30, color=text_color)

plt.xticks(ticks=range(0, len(df_filtered_monthly.columns), 50),
           labels=df_filtered_monthly.columns[::50], rotation=90, ha='center', fontsize=10, color=text_color)
plt.yticks(ticks=range(len(df_filtered_monthly.index)), labels=df_filtered_monthly.index, fontsize=8, color=text_color)

plt.grid(False)
plt.tight_layout()

plt.savefig('teletexte_pages_monthly_black.png', facecolor=background_color)
plt.show()
