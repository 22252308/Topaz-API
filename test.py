from topaz import TopazAPI
import pandas as pd

api_key = 'YOUR_API_KEY_HERE'
topaz_api = TopazAPI(api_key)

# print(topaz_api.get_dog_colours())
# print(topaz_api.get_dog_colour_by_code(colour_code='BK'))
# print(topaz_api.get_owning_authorities())
# print(topaz_api.get_owning_authority_by_code(authority_code='VIC'))
# print(topaz_api.get_track_codes())
# print(topaz_api.get_track_by_code(track_code='WPK'))
# print(topaz_api.get_grade_codes())
# print(topaz_api.get_grade_by_code(grade_code='1'))
# print(topaz_api.get_dog_details(dog_id=695144538))
# print(topaz_api.get_dog_form(dog_id = 695144538))
# print(topaz_api.get_dog_form(dog_id = 695144538, meeting_date='2023-12-03'))
# print(topaz_api.get_dog_statistics(dog_id = 695144538))
# print(topaz_api.search_dogs(search_term='Crimson', exact_match=False, records=10))
# print(topaz_api.get_meeting_first_split_results(meeting_id=509346178))
# print(topaz_api.get_races_first_split(meeting_id=509346178))
# print(topaz_api.get_race_runs_first_split(race_id=509346808))
# print(topaz_api.get_race_first_split(race_id=509346808))
# print(topaz_api.get_meetings(from_date='2023-12-05'))
# print(topaz_api.get_updated_meetings(since = '2023-12-05 10:33:00'))
# print(topaz_api.get_meeting_details(meeting_id=900012680, format = 'basic'))
# print(topaz_api.get_meeting_form(meeting_id=900012680))
# print(topaz_api.get_meeting_results(meeting_id=900012680))
# print(topaz_api.get_meeting_results_first_split(meeting_id=900012680))
# print(topaz_api.get_meeting_races(meeting_id=900012680))
# print(topaz_api.get_races_first_split(meeting_id=900012680))
# print(topaz_api.get_meeting_field(meeting_id=900012680))
# print(topaz_api.get_race_field(meeting_id=900012680, race_id=972428497))
# print(topaz_api.get_races(from_date= '2023-12-01',to_date = '2023-12-01', owning_authority_code='VIC'))
# print(topaz_api.get_races_for_meeting(meeting_id=900012673))
# print(topaz_api.get_race_result(race_id=972428497))
# print(topaz_api.get_race_runs(race_id = 972428497))
# print(topaz_api.get_race_runs_form(race_id=972428497))
# print(topaz_api.get_race_field(race_id=972428497))
# print(topaz_api.get_race_runs_first_split(race_id=972428497))
# print(topaz_api.get_race_first_split(race_id=972428497))
# print(topaz_api.get_upcoming_races())
# print(topaz_api.get_recent_race_results())
# print(topaz_api.get_runs_for_race(race_id=972428497))
# print(topaz_api.get_change_log())
# print(topaz_api.get_server_health())
# print(topaz_api.get_cache_health())
# print(topaz_api.search_trainers(search_term='ivan', exact_match=False, records=300))
# print(topaz_api.get_trial_results(from_date='2023-12-01', to_date='2023-12-06'))
# print(topaz_api.get_bulk_runs_by_day(owning_authority_code='VIC', year=2023, month=12, day=1))
# print(topaz_api.get_bulk_runs_by_month(owning_authority_code='VIC', year=2023, month=12))

authority_codes = ['NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA']
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

race_runs = []
for race_id in race_ids:
    race_run = topaz_api.get_race_runs(race_id=race_id)
    race_runs.append(race_run)

race_runs = pd.concat(race_runs)
print(race_runs)
