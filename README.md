# 📺 Restoration Teletext RTBF

This project aims to restore and preserve the teletext history of RTBF.

By archiving this legacy content, the goal is to save a valuable piece of broadcasting history for future reference and research.

Watch the evolution of the map and download the archives via https://teletext.pocketvince.com

Currently contains more than 2500 pages!

## Description
On 12/02/2024, RTBF decided to discontinue its teletext service.

In the past, RTBF teletext offered access to subtitles, news, sports updates, weather,... Making it a key information source before the internet.

My goal now is to extract as many screenshots as possible, enhance them, and recreate a snapshot of the past.

Teletext evolved over the years, and I’ll keep updating the project on GitHub.

## Setup
```shell
pip3 install pandas requests matplotlib beautifulsoup4 Pillow numpy opencv-python-headless tqdm
apt-get install curl jq
```

## Usage
### Extractor_teletext.py
Images will be systematically exported to the teletexte_images folder in yearmonthday_page_subpage.gif format.
Export will not take place if:

• The file already exists

• The image is corrupted

• Temporary archive ban

• Image does not exist

You can use the first python script to export page by page, sub page by sub page for a specific timestamp:
```shell
python3 extractor_teletext.py YYYYMMDD
```
### Missing.py
If you prefer to search a specific page/subpage, you can run missing.py
It will keep the same rules for saving an image except that it will search for specific pages for a specific date that you can insert in a text file named id.txt, in the format “yearmonthday page subpage”.
If you're not looking for a specific subpage, enter 1 by default (i.e. “yearmonthday page 1”).
To run the script:

```shell
python3 missing.py
```
### Missing.sh
If you need help generating timestamp ids, you can run the shell script missing.sh with the page number (and subpage if necessary) as argument, and save the result in the file id.txt, example:
```shell
./missing.sh 128 5
```
Example output:

20001117 128 5

20010504 128 5

20020223 128 5

20030113 128 5

20030225 128 5

Then running missing.py will search for all queries stored in id.txt.

### Resize.py
By executing the script, it will retrieve all the images from the teletexte_images folder (previously exported), process them and place the new images in the upscaled_images folder.

In terms of processing, the script will: 

• Upscale images

• Reduce saturation

• Color enhancement

```shell
python3 resize.py
```

The project is open and collaborative, if you have sources on your side, don't hesitate to share them.

### Black Map
The “Black Map” scripts generate a map that provides a visualization based on the pages available vs date. 
Year, year month or day level.
You can see an example in the “status” section
To run it, simply launch the appropriate version:

```shell
python3 black-map-daily.py
python3 black-map-monthly.py
python3 black-map-yearly.py
```

### Duplicate.py
The script will scan the teletexte_images folder and move duplicate files to “duplicate”.

The script works on a pixel-perfect basis; if the images are a little different, they are ignored.

Placement in the “duplicate” folder will be filed in folders in page_subpage format for easy verification.

```shell
python3 duplicate.py
```

## Last Update
### 20240929:
The missing python script is progressing well and has been able to continue retrieving images, for the moment we are on 739/999.

This currently totals over 8500 images, but contains duplicates.

I've already written the cleanup script (duplicate.py) that will clean everything up.

As already noted in previous analyses, it seems that some images have not been updated over time, for example:

Page 732 sub-page 1 returns the same image for the dates: 20030321, 20040904, 20010828, 20010417, 20001215, 20001014, 20000615, 20000604, 20000503, 20000422,...

The online version published at https://teletext.pocketvince.com displays unduplicated versions (for greater fluidity and performance), but the complete archives can be downloaded.

I presume the script will need to run for part of the week, my vacation is soon over, so as soon as I have a minute, I'll post the rest (:

### 20240926:
The script is currently running (331/999), but cleaning it up while it's running is an error, as it re-downloads the duplicates.

In the meantime, I've made the resize.py script, which allows you to:

• Upscale images

• Reduce saturation

• Color enhancement

The web version has also been updated to take the enhanced png version, and no longer the small gif format.

### 20240925:
I've rewritten an equivalent script to look for missing pages, the script has a shell part where you can specify the page and subpage you're looking for, and it will return all the timestamps in a text file (id.txt).
And then by executing missing.py it will do the job based on the registered ids.
Checking whether the script is working properly, I've noticed that there are a lot of useless images, for example, page 100 is the same between 2 very distant dates.
When the script has finished running, it will be important to delete the duplicates for better visualization.
For the moment, we're at 128/999.

### 20240924:
I think all the exportable pages have been successfully downloaded, it was also possible to add a part of 2024 containing "the end of teletext" message, thanks to the dandumontp archives ( https://www.journaldulapin.com/2024/02/12/teletexte-rtbf/ ).
A final check needs to be made to ensure that nothing is missing, ~~and then we can try to improve the images.~~

### 20240922:
The python script exported everything linked to the https://www.rtbf.be/services/teletexte/ link, other URLs need to be scanned, but given the number of URLs, this part will probably be done manually (to avoid spending more time scripting than doing the work), the reason being that over time the rtbf switched to a javascript solution which prevented the wayback machine from retrieving all the images from:

http://ds.static.rtbf.be/teletext/

https://static-misc.rtbf.be/teletext/

https://ds1.static.rtbf.be/teletext/

http://ds1.ds.static.rtbf.be/teletext/

http://old.rtbf.be/services/

### 20240915:
A visual part has been added on the site which allows navigation between pages, sub-pages and date.
During creation it was noticed that some images have the wrong date, this is related to the fact that the capture keeps the initial date, but the wayback machine seems to return the same images for different date, a manual cleaning will have to be done in the future :)

### 20240909:
I've set up a small website to share the archives with updates of the image map to have a vision of what needs to be completed, and the image archives, I guess within a few weeks I'll have enough data to start the clean and visualization part.

### 20240908:
The script works and doesn't seem to return any errors, it's currently running on my laptop, my vps, my raspberry pi and on 2 old 3G phones, the archives are filling up quite quickly.

## Status

![Alt text](https://teletext.pocketvince.com/teletexte_pages_yearly_black.png?3 "todo")
![Alt text](https://teletext.pocketvince.com/teletexte_pages_monthly_black.png?3 "todo")
![Alt text](https://teletext.pocketvince.com/teletexte_pages_daily_black.png?3 "todo")

## Todolist
✔️ Write python code with beautifulsoup to automate export

✔️ Write a script for image cleaning and upscaling

✔️ Create a script to generate an image map

⌛ Search for missing or incorrect files

✔️ Visualisation script

✔️ Elimination of duplicates for multiple dates in the same period (solved via duplicate.py)

## Contributing

Readme generator: https://www.makeareadme.com/

http://ds.static.rtbf.be/teletext/ via wayback.archive.org

https://static-misc.rtbf.be/teletext/ via wayback.archive.org

https://ds1.static.rtbf.be/teletext/ via wayback.archive.org

http://ds1.ds.static.rtbf.be/teletext/ via wayback.archive.org

https://www.rtbf.be/article/la-fin-d-une-epoque-le-teletexte-a-la-rtbf-c-est-termine-sauf-pour-les-sous-titres-11325912

https://www.journaldulapin.com/2024/02/12/teletexte-rtbf/

https://x.com/a_libotte/status/1837380993113903437

## More details about the project
I have always been fascinated by teletext.

Growing up without a computer or the internet until the early 2000s, teletext was a real source of information for me, and in a way, it allowed me to entertain myself, search for test pages, debug modes,...

When I learned about the shutdown of teletext, out of nostalgia, I wanted to consult some archives, and I was quite surprised to see that none existed.

I tried to restore part of the teletext using old VHS tapes, but the images were filled with artifacts and were unusable.

Remembering that a web version existed in the past, I thought they must have been saved by the Wayback Machine, I tried to look.

Obviously, everything was very slow on isolated servers, and it was quite tedious to browse teletext in this manner.

So, I started building a structure that would include all the available dates, pages, and sub-pages, allowing them to be viewed through a clean and fast web interface.

The project is currently well underway, and I am happy to have already received support from some people on social media or various contributions.

I sincerely hope to bring this project to completion because, once again, there are no public archives of this relic from the past, and I think it would be a shame if future generations could not consult it.

Other European countries maintain archives of their teletexts or even still have teletext services, and if I take France as an example, the Minitel service has disappeared but can still be viewed via the internet, and the goal here was clearly to have this vision of the past.

I have managed to cover a large period that starts at the beginning of 1999 and goes up to the year 2024.

I would like to expand this project further before potentially tackling other French-speaking Belgian TV channels.

Since RTBF was the only channel that implemented a web version, this may prove to be a challenge.

In terms of script construction, in the past, the pages were managed in HTML and in JavaScript scripts that simply made calls to URLs and were directly redirected to a page that would show a specific teletext page and sub-page.

During my research, I found that no less than six versions of this teletext existed.

There is the main one, which started in the mid-90s and lasted until around 2005-2006.

The other versions included a JavaScript version that directly called the image.

The Wayback Machine works by clicking and following links, which allowed it to save many pages and record a large number of images.

Unfortunately, other pages could not be fully saved because it was no longer possible to click a button to reach a specific page;

Instead, you had to enter the value.

Fortunately, many external services to RTBF were able to use teletext images, such as for weather forecasts.

People had put a direct link to the file.

The advantage was that the URL never changed, so the Wayback Machine, while crawling other websites, was able to preserve those URLs as well.

However, many others have simply been lost to time, as they could not be saved.


The main script that was published is therefore based on the first version, which spans from the 1990s to 2005-2006.

The other versions of teletext were manually scraped, as they represented less than 300 pages.

As for the 2024 part, it was not saved at all, but it was retrieved through videos published on YouTube and articles posted on blogs.

While building the scripts, I was able to explore and navigate through the existing code, which had not been deliberately complicated, and I gained a better understanding of how everything worked.

Before adopting a more conventional naming format, the pages were stored in folders in blocks of 100 and were manually called to pages.

For example, they had to build an index that would redirect, say, page 100 to the folder ‘mag1/page00_1.gif’ A part of my script involved creating an easier conventional naming system to re-encode image visualization.

During the scraping process conducted by the Wayback Machine, while repeatedly searching the visualization of subfolders, I stumbled upon pages that contained indexes, where I found copies of files forgotten by developers, unused gif headers, but unfortunately, only their names indicated this as the data was unrecoverable.

Additionally, there was an unexploitable, non-exportable text file named ‘LAUNE.FR.la_taille.TXT’ which I imagine served as a reference for remembering how to name the files.

While developing the script Missing.py, I also noticed that teletext was not always updated in its web version and could contain old pages that hadn't been refreshed, or simply copyrights reflecting earlier dates. For example, the images corresponding to page 100 from 1999 already displayed a 2000 copyright, and conversely, after 2015, it seems the copyright was stuck on 2015. I didn't find any hidden or accidentally forgotten elements in the teletext pages, apart from the test page, which seems to have remained the same throughout the lifespan of teletext. I still found it amusing that the test page was listed in the teletext's own index. This index itself was reduced over the years. At first, they used a cyan color on the page number if the page wasn't visible. In the end, they only kept what already existed.

Today, September 25, 2024, the project is almost complete. I believe all the pages that could be saved have been exported. All screenshots that were posted on social media, in press articles, on personal blogs, or elsewhere have been retrieved. One remaining task is to clean up all these duplicates, like page 100, which repeats endlessly throughout teletext's existence, to streamline and make usage as friendly as possible.


Regarding the visualization of pages on the website teletext.pocketvince.com, you can select a page number, and it will display the first image it finds in the database.

If you want, you can change the date.

By default, it will only show the available dates.

You can also select another sub-page.

If you choose a sub-page that doesn't exist for that date, it will automatically switch to the closest date containing that sub-page.

Similarly, if you land on a page where the date wasn't available, it will switch to the closest possible date.

This allows smoother navigation and avoids landing on pages with entirely different content.

Although for many years, a certain structure remained, it seems that before replacing one page with another while keeping the same number, the index had to be quite full.

This was no longer the case toward the end of teletext's life.

This also means that having only been able to recover about thirty pages and sub-pages for the year 2024, this year may not be as pleasant to view, apart from the homepage that announced the end of teletext.

I hope the project interests you.

Feel free to contact me if you have any archives, anecdotes, or any other information that could contribute to the project.

Thank you for reading, and I wish you a great day (:

