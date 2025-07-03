# Altitude Checker

This Python script retrieves elevation data (in meters) for a list of geographic coordinates using the [Open-Elevation API](https://open-elevation.com/).

## Features

- Reads coordinates from Excel (`Altitude check.xlsx`)
- Sends queries to Open-Elevation API
- Adds an `Elevation` column
- Saves a new file: `Altitude check with Elevation.xlsx`

## Checking the altitude (after you already did the Setup)
1. Input your long and lat in the "Altitude check.xlsx" file
2. Run the altitude.py file
3. You can see a new created .xlsx file that include altitude

## Setup
1. Download all files and save to your folder.
2. Install dependencies:
  - Install Python
  - Go to command prompt (cmd)
    
```bash
F:
cd Python\altitude-checker #  ← example if you save the downloaded files into "F:\Python\altitude-checker" folder
dir   # ← optional, just to confirm the file is listed
pip install -r requirements.txt
