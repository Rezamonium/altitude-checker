import pandas as pd
import requests
import time

# Load the Excel file
df = pd.read_excel("Altitude check.xlsx")

# Ensure correct column names
df.columns = ['Lat', 'Long']

# Function to get elevation
def get_elevation(lat, lon):
    url = 'https://api.open-elevation.com/api/v1/lookup'
    params = {'locations': f'{lat},{lon}'}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json()['results']
            if results:
                return results[0]['elevation']
    except Exception as e:
        print(f"Error fetching elevation for ({lat}, {lon}): {e}")
    return None

# Get elevation for each coordinate, with progress
elevations = []
total = len(df)

for index, row in df.iterrows():
    print(f"Processing row {index + 1} of {total}")
    elevation = get_elevation(row['Lat'], row['Long'])
    elevations.append(elevation)
    time.sleep(1)  # pause to avoid rate limiting

df['Elevation'] = elevations

# Save to new Excel file
df.to_excel("Altitude check with Elevation.xlsx", index=False)
print("✅ Done! Saved as 'Altitude check with Elevation.xlsx'")