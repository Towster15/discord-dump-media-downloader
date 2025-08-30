# Discord Data Dump Media Downloader
A "simple" project from early-2024 to crawl through my discord data dump, retrieving old files that I've long-since lost.

Is it perfect? No. Did it work? Pretty much yeah.

# Required packages
- urllib3
- requests

# Things that need fixing
- It doesn't handle error codes well
  - Error codes are displayed in the console, but it doesn't attempt to re-download the files
  - There's no way to distinguish between if a file is actually unavailable or if you've just got unlucky/connection issues
  - No way to say if you're being rate limited
- Update the user agent/allow user agent selection
  - Still using an old Firefox user agent
- Ideally there would be a slightly nicer user interface

# Future ideas for one day
- A nicer user interface (Tk/Qt based)
- Better search/filter for finding urls within messages
  - When an attachment is sent, it's put into a separate field to the main message
  - When an attachment link is embedded inside a message, it's a lot harder to get to
- Connect data from the CSV file to the media file
  - Having both the file name and timestamp of it being sent would be nice