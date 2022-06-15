
<h1 align="center"> M3U generator </h1>

[![M3U generator for YouTube](https://github.com/chungplay/chungplay.github.io/actions/workflows/m3u_Generator.yml/badge.svg)](https://github.com/chungplay/chungplay.github.io/actions/workflows/m3u_Generator.yml)

`https://github.com/chungplay/chungplay.github.io/blob/main/playlist.m3u`

Updated m3u links of YouTube live channels, **auto-updated every hour**.


### Add more channels
Edit `URL_link.txt` to add your favourite YouTube livestreams
### Usage
Paste this URL: `https://raw.githubusercontent.com/chungplay/chungplay.github.io/main/playlist.m3u` to any player which supports M3U playlists

### Run the tool on your local machine
``` bash
git clone https://github.com/chungplay/chungplay.github.io.git
cd chungplay.github.io
chmod +x autorun.sh
./autorun.sh
```

Do not forget to add a cron job set for every 4 hours(or 5) if you plan to run the script locally.
