#!/bin/bash
if [ -z "$2" ]; then
URL="http://rtbf.be:80/services/teletexte/cgi-bin/GetPage.cgi?PAGE=$1"
sub=1
else
URL="http://rtbf.be:80/services/teletexte/cgi-bin/GetPage.cgi?PAGE=$1&SUB=$sub"
sub=$2
fi

curl "http://web.archive.org/cdx/search/cdx?url=$URL&output=json&fl=timestamp,original&collapse=digest" | jq -r '.[] | .[0], .[1]' | tail -n +3 | while read -r timestamp; do
  read -r original_url

  date=${timestamp:0:8}

  echo "$date $1 $sub" >> id.txt
done
found=$(cat id.txt | wc -l)
echo "$found link(s) found"
