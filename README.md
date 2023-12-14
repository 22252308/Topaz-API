# Topaz API

A simple Python Wrapper for the GRV Topaz API. Quickly written with the help of ChatGPT.

Requires a Topaz API key obtainable through the Betfair Automation team @ api@betfair.com.au

[Docs](https://topaz.grv.org.au/docs/)

## Installation
```
pip install topaz_api
```

## Usage
```
from topaz import TopazAPI

api_key = 'YOUR_API_KEY_HERE'
topaz_api = TopazAPI(api_key)
```

## Suggested work flow
```
import pandas as pd

authority_codes = [ 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA']
all_races = []

for code in authority_codes:
    try:
        races = topaz_api.get_races(from_date='2023-12-01', to_date='2023-12-06', owning_authority_code=code)
        all_races.append(races)
    except Exception as e:
        print(f"Error fetching races for {code}: {e}")

# Concatenate all fetched races into a single DataFrame
all_races_df = pd.concat(all_races, ignore_index=True)

# Extract unique race IDs
race_ids = list(all_races_df['raceId'].unique())
```

