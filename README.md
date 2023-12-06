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
# Might take 4 or 5 mins to run
races = topaz_api.get_races(from_date='2023-12-01', to_date='2023-12-06')
race_ids = list(races['raceId'].unique())

race_runs = []
for race_id in race_ids:
    race_run = topaz_api.get_race_runs(race_id=race_id)
    race_runs.append(race_run)

race_runs = pd.concat(race_runs)
print(race_runs)
```

