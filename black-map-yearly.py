import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import re
from matplotlib.colors import ListedColormap

folder_path = 'teletexte_images'

file_pattern = r'(\d{4})(\d{2})(\d{2})_(\d+)_(\d+)\.gif'

pages_by_year = defaultdict(set)

for filename in os.listdir(folder_path):
    match = re.match(file_pattern, filename)
    if match:
        year, month, day, page, subpage = match.groups()
        year_key = f"{year}"
        pages_by_year[year_key].add(page)

all_pages = set()
for year, pages in pages_by_year.items():
    all_pages.update(pages)

df_yearly = pd.DataFrame(0, index=pages_by_year.keys(), columns=sorted(all_pages))

for year, pages in pages_by_year.items():
    df_yearly.loc[year, list(pages)] = 1

df_filtered_yearly = df_yearly.loc[:, (df_yearly != 0).any(axis=0)]

df_filtered_yearly = df_filtered_yearly[(df_filtered_yearly.T != 0).any()]

background_color = 'black'
grid_color = '#00FF00'
text_color = '#FFFF00'

cmap_black_inside = ListedColormap([background_color, grid_color])

plt.figure(figsize=(20, 16), facecolor=background_color)
plt.imshow(df_filtered_yearly, cmap=cmap_black_inside, aspect='auto')

plt.xlabel("Page", fontsize=12, color=text_color)
plt.ylabel("Years", fontsize=12, color=text_color)
plt.title("Representation of Available Teletext Pages by Year", fontsize=30, color=text_color)

plt.xticks(ticks=range(0, len(df_filtered_yearly.columns), 50),
           labels=df_filtered_yearly.columns[::50], rotation=90, ha='center', fontsize=10, color=text_color)
plt.yticks(ticks=range(len(df_filtered_yearly.index)), labels=df_filtered_yearly.index, fontsize=35, color=text_color)

plt.grid(False)
plt.tight_layout()

plt.savefig('teletexte_pages_yearly_black.png', facecolor=background_color)
plt.show()
