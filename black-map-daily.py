import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import re
from matplotlib.colors import ListedColormap

folder_path = 'teletexte_images'

file_pattern = r'(\d{4})(\d{2})(\d{2})_(\d+)_(\d+)\.gif'

pages_by_date = defaultdict(set)

for filename in os.listdir(folder_path):
    match = re.match(file_pattern, filename)
    if match:
        year, month, day, page, subpage = match.groups()
        date = f"{year}-{month}-{day}"
        pages_by_date[date].add(page)

all_pages = set()
for date, pages in pages_by_date.items():
    all_pages.update(pages)

df = pd.DataFrame(0, index=pages_by_date.keys(), columns=sorted(all_pages))

for date, pages in pages_by_date.items():
    df.loc[date, list(pages)] = 1

df_filtered = df.loc[:, (df != 0).any(axis=0)]

df_filtered = df_filtered[(df_filtered.T != 0).any()]

background_color = 'black'
grid_color = '#00FF00'
text_color = '#FFFF00'

cmap_black_inside = ListedColormap([background_color, grid_color])

plt.figure(figsize=(20, 16), facecolor=background_color)

plt.imshow(df_filtered, cmap=cmap_black_inside, aspect='auto', interpolation='nearest')

plt.gca().set_facecolor(background_color)
plt.xlabel("Page", fontsize=12, color=text_color)
plt.ylabel("Dates", fontsize=12, color=text_color)
plt.title("Representation of Available Teletext Pages by Date", fontsize=30, color=text_color)

plt.xticks(ticks=range(0, len(df_filtered.columns), 50),
           labels=df_filtered.columns[::50], rotation=90, ha='center', fontsize=10, color=text_color)
plt.yticks(ticks=range(len(df_filtered.index)), labels=df_filtered.index, fontsize=8, color=text_color)

plt.grid(False)

plt.tight_layout()

plt.savefig('teletexte_pages_daily_black.png', facecolor=background_color)
plt.show()
