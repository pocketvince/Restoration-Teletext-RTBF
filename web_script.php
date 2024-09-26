<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Restoration Teletext RTBF</title>
<style>
body {
    background-color: black;
    color: white;
    font-family: 'Courier New', Courier, monospace;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 100vh;
}
.container {
    max-width: 800px;
    margin: auto;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex-grow: 1;
}
.page-header {
    text-align: left;
    padding: 5px;
    letter-spacing: 2px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.page-number {
    color: white;
    font-size: 24px;
}
.datetime {
    color: green;
    font-size: 24px;
}
.time {
    color: yellow;
}
.title {
    background-color: navy;
    color: white;
    padding: 1px;
    text-align: center;
    font-size: 18px;
    letter-spacing: 3px;
}
.content {
    flex-grow: 1;
    padding: 1px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1px;
}
.content p {
    margin: 0;
    font-size: 20px;
    line-height: 1.5;
    letter-spacing: 1px;
}
.footer {
    background-color: crimson;
    padding: 10px;
    text-align: center;
    color: yellow;
    font-size: 18px;
    letter-spacing: 2px;
}
.links {
    display: flex;
    justify-content: space-between;
    padding: 10px;
    margin-bottom: 10px;
}
.link {
    padding: 10px;
    font-weight: bold;
    text-align: center;
    width: 22%;
    font-size: 20px;
    letter-spacing: 1px;
}
.link.red { color: red; }
.link.green { color: green; }
.link.yellow { color: yellow; }
.link.cyan { color: cyan; }
.link a {
    color: inherit;
    text-decoration: none;
}
.selector-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
}

.selector-group {
    display: flex;
    align-items: center;
    margin-bottom: 0;
}

.selector-group span {
    margin-right: 10px;
    font-size: 18px;
    width: 80px;
}

.section-title {
    margin-bottom: 10px;
}
select {
    background-color: #333;
    color: white;
    border: 1px solid #555;
    padding: 5px;
    font-size: 16px;
    width: 120px;
}
#image-container {
    text-align: left;
    margin-top: 0px;
}
#image-container img {
    max-width: 100%;
    height: auto;
}
.download-button {
    text-align: center;
    margin: 20px 0;
}
.download-button a {
    display: inline-block;
    background-color: navy;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    font-weight: bold;
    border: 2px solid yellow;
}
.section-title {
    color: cyan;
    font-size: 20px;
    margin-bottom: 0px;
}
@media screen and (max-width: 600px) {
    .page-header, .title, .content, .footer, .links {
        font-size: 16px;
    }
    .link {
        padding: 5px;
    }
}
</style>
</head>
<body>
<div class="container">
    <header class="page-header">
        <div class="page-number">P100</div>
        <div class="datetime">
            <span id="currentDate">Saturday, 7 September 2024</span> 
            <span class="time" id="currentTime">14:05:32</span>
        </div>
    </header>

    <div class="title"><p>Restoration Teletext RTBF</p></div>

    <p class="section-title">Description</p>
    <div class="content">
        <p style="color:yellow;">The goal of this project is to restore RTBF teletext for preservation purposes, and to recreate a snapshot of the past, follow the project on <a href="https://github.com/pocketvince/Restoration-Teletext-RTBF">Github</a></p>
    </div>

    <div class="download-button">
        <a href="teletexte_upscaled.zip" download>DOWNLOAD UPSCALED FILES</a>
        <a href="teletexte_original.zip" download>DOWNLOAD ORIGINAL FILES</a>
    </div>

<p class="section-title">Teletext Viewer</p>
<div class="selector-container">
    <div class="selector-group">
        <span style="color:yellow">Page:</span>
        <select id="page" onchange="updateDropdowns('page')"></select>
    </div>
    <div class="selector-group">
        <span style="color:green">Subpage:</span>
        <select id="subpage" onchange="updateDropdowns('subpage')"></select>
    </div>
    <div class="selector-group">
        <span style="color:red">Date:</span>
        <select id="date" onchange="updateDropdowns('date')"></select>
    </div>
</div>

    <div id="image-container">
        <h2 id="page-info"></h2>
        <img id="image" alt="Teletexte Image" src="">
    </div>

    <p id="no-image" style="display:none;">No images available for this combination of date, page and subpage.<br>Try a different date or subpage</p>

    <footer class="footer">Overview</footer>

    <img src="teletexte_pages_yearly_black.png" alt="Yearly Overview">
    <img src="teletexte_pages_monthly_black.png" alt="Monthly Overview">
    <img src="teletexte_pages_daily_black.png" alt="Daily Overview">
    
    <div class="links">
        <div class="link red"><a href="https://www.rtbf.be/article/la-fin-d-une-epoque-le-teletexte-a-la-rtbf-c-est-termine-sauf-pour-les-sous-titres-11325912">RTBF</a></div>
        <div class="link green"><a href="https://pocketvince.com">Pocketvince</a></div>
        <div class="link yellow"><a href="https://github.com/pocketvince/Restoration-Teletext-RTBF">Github</a></div>
        <div class="link cyan"><a href="https://en.wikipedia.org/wiki/Teletext">Wikipedia</a></div>
    </div>
</div>

<?php
$imageDirectory = 'teletexte_images';
$images = [];

if ($handle = opendir($imageDirectory)) {
    while (false !== ($entry = readdir($handle))) {
        if (preg_match('/(\\d{8})_(\\d{3})_(\\d{2})\\.png$/', $entry, $matches)) {
            $date = $matches[1];   // Date from the filename
            $page = $matches[2];   // Page from the filename
            $subpage = $matches[3]; // Subpage from the filename
            $images[] = [
                'nom' => $entry,
                'date' => $date,
                'page' => $page,
                'subpage' => $subpage
            ];
        }
    }
    closedir($handle);
}
?>

<script>
function updateDateTime() {
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    
    const now = new Date();
    const dayName = days[now.getDay()];
    const day = now.getDate();
    const month = months[now.getMonth()];
    const year = now.getFullYear();

    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    document.getElementById("currentDate").textContent = `${dayName}, ${day} ${month} ${year}`;
    document.getElementById("currentTime").textContent = `${hours}:${minutes}:${seconds}`;
}

setInterval(updateDateTime, 1000);
updateDateTime();

const images = <?php echo json_encode($images); ?>;
const imageDirectory = '<?php echo $imageDirectory; ?>';

let currentSelection = {
    page: '100',
    subpage: '01',
    date: null
};

function populateDropdowns() {
    const pageSelect = document.getElementById('page');
    const subpageSelect = document.getElementById('subpage');
    const dateSelect = document.getElementById('date');

    const pages = [...new Set(images.map(img => img.page))].sort((a, b) => a - b);
    pages.forEach(page => {
        const option = document.createElement('option');
        option.value = page;
        option.text = page;
        pageSelect.appendChild(option);
    });

    pageSelect.value = currentSelection.page;
    updateDropdowns('page');
}

function updateDropdowns(changedElement) {
    const pageSelect = document.getElementById('page');
    const subpageSelect = document.getElementById('subpage');
    const dateSelect = document.getElementById('date');

    if (changedElement === 'page') {
        const subpages = [...new Set(images.filter(img => img.page === pageSelect.value).map(img => img.subpage))].sort((a, b) => a - b);
        subpageSelect.innerHTML = '';
        subpages.forEach(subpage => {
            const option = document.createElement('option');
            option.value = subpage;
            option.text = subpage;
            subpageSelect.appendChild(option);
        });

        currentSelection.page = pageSelect.value;
        currentSelection.subpage = '01';
        subpageSelect.value = '01';

        updateDropdowns('subpage');
    }

    if (changedElement === 'subpage') {
        currentSelection.subpage = subpageSelect.value;

        const availableDates = [...new Set(images.filter(img => img.page === currentSelection.page && img.subpage === currentSelection.subpage).map(img => img.date))].sort((a, b) => a - b);

        dateSelect.innerHTML = '';
        availableDates.forEach(date => {
            const option = document.createElement('option');
            option.value = date;
            option.text = date;
            dateSelect.appendChild(option);
        });

        const selectedDate = findClosestDate(currentSelection.date, availableDates);
        currentSelection.date = selectedDate;
        dateSelect.value = selectedDate;

        showImage();
    }

    if (changedElement === 'date') {
        currentSelection.date = dateSelect.value;
        showImage();
    }
}

function findClosestDate(targetDate, availableDates) {
    if (!targetDate || availableDates.includes(targetDate)) {
        return targetDate || availableDates[0];
    }

    const target = parseInt(targetDate, 10);
    let closest = availableDates[0];

    availableDates.forEach(date => {
        const currentDate = parseInt(date, 10);
        if (Math.abs(currentDate - target) < Math.abs(parseInt(closest, 10) - target)) {
            closest = date;
        }
    });

    return closest;
}

function showImage() {
    const image = images.find(img => img.page === currentSelection.page && img.subpage === currentSelection.subpage && img.date === currentSelection.date);

    const imageContainer = document.getElementById('image-container');
    const noImage = document.getElementById('no-image');
    const imageElement = document.getElementById('image');
    const pageInfo = document.getElementById('page-info');

    if (image) {
        imageElement.src = `${imageDirectory}/${image.nom}`;
        imageContainer.style.display = 'block';
        noImage.style.display = 'none';
    } else {
        imageContainer.style.display = 'none';
        noImage.style.display = 'block';
        pageInfo.textContent = '';
    }
}

populateDropdowns();
</script>

</body>
</html>
