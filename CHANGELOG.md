# Changelog

All notable changes to this project will be documented in this file.

## [0.0.7] - 2026-06-10

### Added

- `get_isolynx_positions(race_id)` for `GET /isolynx/{raceId}/positions`
- `get_isolynx_positions_with_dnf(race_id)` for `GET /isolynx/{raceId}/positionswithdnf`
- `__version__` attribute on the `topaz` package
- Note: Isolynx data is currently only available for Victorian (VIC) races

### Fixed

- Removed duplicate definitions of `get_races_first_split` and `get_race_runs_first_split`
  (Python silently kept only the last definition, so behaviour is unchanged)
- Renamed the meeting-scoped field method (`GET /meeting/{meetingId}/field/{raceId}`) to
  `get_meeting_race_field(meeting_id, race_id)`. It previously shared the name
  `get_race_field` with the race-scoped method (`GET /race/{raceId}/field`) and was
  unreachable. `get_race_field(race_id)` is unchanged.
- Corrected project URLs in package metadata (previously pointed to a placeholder repo)

## [0.0.6] and earlier

- Initial releases: wrapper methods for codes, dogs, first split, Isolynx splits,
  meetings, races, trainers, trials, bulk data, and utility endpoints.
