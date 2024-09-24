# 📺 Restoration Teletext RTBF

This project aims to restore and preserve the teletext history of RTBF.

By archiving this legacy content, the goal is to save a valuable piece of broadcasting history for future reference and research.

Watch the evolution of the map and download the archives via https://teletext.pocketvince.com

Currently contains more than 2500 pages!

## Description
On 12/02/2024, RTBF decided to discontinue its teletext service.

In the past, RTBF teletext offered access to subtitles, news, sports updates, weather,... Making it a key information source before the internet.

I first encountered teletext in the late 90's.

Coming from a modest family without internet or a computer, teletext was a game-changer.

Although exporting from old VHS tapes failed, I found archived versions of RTBF teletext on the Wayback Machine.

My goal now is to extract as many screenshots as possible, enhance them, and recreate a snapshot of the past.

Teletext evolved over the years, and I’ll keep updating the project on GitHub.

## Last Update
### 20240924:
I think all the exportable pages have been successfully downloaded, it was also possible to add a part of 2024 containing "the end of teletext" message, thanks to the dandumontp archives ( https://www.journaldulapin.com/2024/02/12/teletexte-rtbf/ ).
A final check needs to be made to ensure that nothing is missing, and then we can try to improve the images.

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

![Alt text](https://teletext.pocketvince.com/teletexte_pages_yearly_black.png?1 "todo")
![Alt text](https://teletext.pocketvince.com/teletexte_pages_monthly_black.png?1 "todo")
![Alt text](https://teletext.pocketvince.com/teletexte_pages_daily_black.png?1 "todo")

## Todolist
✔️ Write python code with beautifulsoup to automate export

❌ Write a script for image cleaning and upscaling

✔️ Create a script to generate an image map

⌛ Search for missing or incorrect files

✔️ Visualisation script

## Contributing

Readme generator: https://www.makeareadme.com/

http://ds.static.rtbf.be/teletext/ via wayback.archive.org

https://static-misc.rtbf.be/teletext/ via wayback.archive.org

https://ds1.static.rtbf.be/teletext/ via wayback.archive.org

http://ds1.ds.static.rtbf.be/teletext/ via wayback.archive.org

https://www.rtbf.be/article/la-fin-d-une-epoque-le-teletexte-a-la-rtbf-c-est-termine-sauf-pour-les-sous-titres-11325912

https://www.journaldulapin.com/2024/02/12/teletexte-rtbf/

https://x.com/a_libotte/status/1837380993113903437
