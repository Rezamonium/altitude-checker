# Altitude Checker

This Python script retrieves elevation data (in meters) for a list of geographic coordinates using the [Open-Elevation API](https://open-elevation.com/).

## Features

- Reads coordinates from Excel (`Altitude check.xlsx`)
- Sends queries to Open-Elevation API
- Adds an `Elevation` column
- Saves a new file: `Altitude check with Elevation.xlsx`

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
