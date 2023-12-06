import requests
import pandas as pd

class TopazAPI:
    def __init__(self, api_key):
        self.base_url = "https://topaz.grv.org.au/api"
        self.headers = {
            'accept': 'application/json',
            'X-API-Key': api_key
        }

    ### Codes
    def get_dog_colours(self) -> pd.DataFrame:
        """
        Gets the dog color codes.

        Returns:
            pd.DataFrame: A DataFrame containing all the dog color codes and their descriptions.
        """
        response = requests.get(f"{self.base_url}/codes/dogcolour", headers=self.headers, timeout=30)
        if response.status_code == 200:
            # Convert the list of dictionaries (which is the expected JSON response) to a DataFrame
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_dog_colour_by_code(self, colour_code: str) -> dict:
        """
        Gets details for a specific dog colour code.

        Args:
            colour_code (str): The colour code to retrieve details for. 
                            Example value would be "BK" for black.

        Returns:
            dict: A dictionary containing the code and the colour description.
        """
        response = requests.get(f"{self.base_url}/codes/dogcolour/{colour_code}", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_owning_authorities(self) -> pd.DataFrame:
        """
        Gets the owning authority codes.

        Returns:
            pd.DataFrame: A DataFrame containing all the owning authority codes and their descriptions.
        """
        response = requests.get(f"{self.base_url}/codes/owningauthority", headers=self.headers, timeout=30)
        if response.status_code == 200:
            # Convert the list of dictionaries (which is the expected JSON response) to a DataFrame
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_owning_authority_by_code(self, authority_code: str) -> dict:
        """
        Gets details for a specific owning authority code.

        Args:
            authority_code (str): The owning authority code to retrieve details for. 
                                Example value would be "VIC" for Victoria.

        Returns:
            dict: A dictionary containing the details of the owning authority.
        """
        response = requests.get(f"{self.base_url}/codes/owningauthority/{authority_code}", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_track_codes(self) -> pd.DataFrame:
        """
        Gets the track codes.

        Returns:
            pd.DataFrame: A DataFrame containing all the track codes and their descriptions.
        """
        response = requests.get(f"{self.base_url}/codes/track", headers=self.headers, timeout=30)
        if response.status_code == 200:
            # Convert the list of dictionaries (which is the expected JSON response) to a DataFrame
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    
    def get_track_by_code(self, track_code: str) -> dict:
        """
        Gets details for a specific track code.

        Args:
            track_code (str): The track code to retrieve details for. 
                            Example value would be "WPK" for Wentworth Park.

        Returns:
            dict: A dictionary containing the details of the specific track.
        """
        response = requests.get(f"{self.base_url}/codes/track/{track_code}", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_grade_codes(self) -> pd.DataFrame:
        """
        Gets the grade codes.

        Returns:
            pd.DataFrame: A DataFrame containing all the grade codes and their descriptions.
        """
        response = requests.get(f"{self.base_url}/codes/grade", headers=self.headers, timeout=30)
        if response.status_code == 200:
            # Convert the list of dictionaries (which is the expected JSON response) to a DataFrame
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_grade_by_code(self, grade_code: str) -> dict:
        """
        Gets details for a specific grade code.

        Args:
            grade_code (str): The grade code to retrieve details for. 
                            Example value would be "1". Yes you have to put a number as a string.

        Returns:
            dict: A dictionary containing the details of the specific grade.
        """
        response = requests.get(f"{self.base_url}/codes/grade/{grade_code}", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    ### Dogs
    def get_dog_details(self, dog_id: int) -> dict:
        """
        Gets details for a specific dog.

        Args:
            dog_id (int): The unique identifier of the dog to retrieve details for. 
                        Example value could be 695144538.

        Returns:
            dict: A dictionary containing the details of the specific dog.
        """
        response = requests.get(f"{self.base_url}/dog/{dog_id}", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_dog_form(self, dog_id: int, meeting_date: str = None) -> pd.DataFrame:
        """
        Gets form details for a specific dog, optionally filtered by a meeting date.

        Args:
            dog_id (int): The GRV id of the dog to get form details for. 
                          E.g. 695144538
            meeting_date (str, optional): You can get form data as at a specified date by specifying a Meeting Date. 
                                          Format should be 'yyyy-mm-dd'. Default is None.
                                          Example for dog_id 695144538 is '2023-12-03'

        Returns:
            pd.DataFrame: A DataFrame containing the form details of the specific dog.
        """
        endpoint = f"{self.base_url}/dog/{dog_id}/form"
        params = {'meetingdate': meeting_date} if meeting_date else {}
        response = requests.get(endpoint, headers=self.headers, params=params, timeout=30)
        
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_dog_statistics(self, dog_id: int) -> dict:
        """
        Gets statistics for a specific dog.

        Args:
            dog_id (int): The GRV id of the dog to get form details for.
                        E.g. 695144538

        Returns:
            dict: A dictionary containing the statistics of the specific dog.
        """
        response = requests.get(f"{self.base_url}/dog/{dog_id}/statistics", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def search_dogs(self, search_term: str, exact_match: bool = False, records: int = 300) -> pd.DataFrame:
        """
        Searches for dogs based on a search term, with options for exact match and record limit.
        Returns a dataframe of dogs and the details of their run within the specified race.

        Args:
            search_term (str): The full or partial name of the target greyhound.
            exact_match (bool, optional): Limits the records returned to the unique greyhound with that name. Default is False.
            records (int, optional): The maximum number of records to return. Default is 300 hits.

        Returns:
            pd.DataFrame: A DataFrame containing the search results.
        """
        params = {
            'searchterm': search_term,
            'exactmatch': exact_match,
            'records': records
        }
        response = requests.get(f"{self.base_url}/search/dogs", headers=self.headers, params=params, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())  # Converts the JSON response to a DataFrame
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    ### Firstsplit
    def get_meeting_first_split_results(self, meeting_id: int) -> dict:
        """
        Returns all the details of the meeting, including races, runs, and results. 
        Includes First Split data for all dogs where available, and returns the most up-to-date data at all times.
        Note: This endpoint requires additional permissions.

        Args:
            meeting_id (int): The unique identifier of the meeting to retrieve first split results for. 
                            Example value could be 509346178.

        Returns:
            dict: A dictionary containing the first split results and other details of the specified meeting.
        
        Raises:
            PermissionError: If the user is not authorized to access this endpoint (HTTP 401 error).
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/results/firstsplit", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        elif response.status_code == 401:  # Unauthorized access
            raise PermissionError("You are not authorized to access this endpoint.")
        else:
            response.raise_for_status()  # Raises an HTTPError for other unsuccessful status codes

    def get_races_first_split(self, meeting_id: int) -> dict:
        """
        Returns a list of all races for the specified meeting. 
        Includes First Split data for all dogs where available, and returns the most up-to-date data at all times.
        Note: This endpoint requires additional permissions.

        Args:
            meeting_id (int): The unique identifier of the meeting to retrieve races' first split results for. 
                            Example value could be 509346178.

        Returns:
            dict: A dictionary containing the first split results and other race details of the specified meeting.
        
        Raises:
            PermissionError: If the user is not authorized to access this endpoint (HTTP 401 error).
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/races/firstsplit", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        elif response.status_code == 401:  # Unauthorized access
            raise PermissionError("You are not authorized to access this endpoint.")
        else:
            response.raise_for_status()  # Raises an HTTPError for other unsuccessful status codes

    def get_race_runs_first_split(self, race_id: int) -> dict:
        """
        Returns a list of dogs and the details of their run within the specified race. 
        The results of this call include First Split information for each run if available and always returns the latest information.
        Note: This endpoint requires additional permissions.

        Args:
            race_id (int): The unique identifier of the race to retrieve runs' first split details for.
                        Example value could be 509346808.

        Returns:
            dict: A dictionary containing the first split details and other run information for the specified race.
        
        Raises:
            PermissionError: If the user is not authorized to access this endpoint (HTTP 401 error).
        """
        response = requests.get(f"{self.base_url}/race/{race_id}/runs/firstsplit", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        elif response.status_code == 401:  # Unauthorized access
            raise PermissionError("You are not authorized to access this endpoint.")
        else:
            response.raise_for_status()  # Raises an HTTPError for other unsuccessful status codes

    # def get_race_first_split(self, race_id: int) -> dict:
    #     """
    #     Returns a list of just the first split data for runs in the specified race. 
    #     Requires the caller to have access to first split information.

    #     Args:
    #         race_id (int): The unique identifier of the race to retrieve first split details for.
    #                     Example value could be 509346808.

    #     Returns:
    #         dict: A dictionary containing the first split data for the specified race.
        
    #     Raises:
    #         PermissionError: If the user is not authorized to access this endpoint (HTTP 401 error).
    #     """
    #     response = requests.get(f"{self.base_url}/race/{race_id}/firstsplit", headers=self.headers, timeout=30)
    #     if response.status_code == 200:
    #         return response.json()  # Returns a dictionary representing the JSON response
    #     elif response.status_code == 401:  # Unauthorized access
    #         raise PermissionError("You are not authorized to access this endpoint.")
    #     else:
    #         response.raise_for_status()  # Raises an HTTPError for other unsuccessful status codes

    ### Internal

    ### Isolynx
    def get_isolynx_splits(self, race_id: int) -> dict:
        """
        Returns a list of runners with ISO Lynx Split data.
        Requires the caller to have access to Isolynx data.

        Args:
            race_id (int): The unique identifier of the race to retrieve ISO Lynx Split data for.
                        Example value could be 509346808.

        Returns:
            dict: A dictionary containing ISO Lynx Split data for the runners in the specified race.
        
        Raises:
            PermissionError: If the user is not authorized to access this endpoint (HTTP 401 error).
        """
        response = requests.get(f"{self.base_url}/isolynx/{race_id}/splits", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        elif response.status_code == 401:  # Unauthorized access
            raise PermissionError("You are not authorized to access this endpoint.")
        else:
            response.raise_for_status()  # Raises an HTTPError for other unsuccessful status codes

    ### Meeting
    def get_meetings(self, from_date: str, to_date: str = None, owning_authority_code: str = None) -> pd.DataFrame:
        """
        Returns a list of Meetings between the two provided dates. When the 'to' date is not supplied, 
        it defaults to the same date as the date provided by 'from'. 
        Where these dates are outside the dates allowed by the configured dates allowed 
        for the user's access to the specified owning authority (state or NZ).

        Args:
            from_date (str): The start date for the query, in YYYY-MM-DD format. Must be a valid date.
            to_date (str, optional): The end date for the query, in YYYY-MM-DD format. Defaults to the same as 'from_date'.
            owning_authority_code (str, optional): The code of the owning authority. Must be one of: 'ACT', 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA', 'NZ'.

        Returns:
            pd.DataFrame: A DataFrame containing the list of meetings.
        """
        params = {
            'from': from_date,
            'to': to_date or from_date,  # Defaults to from_date if to_date is not provided
            'owningauthoritycode': owning_authority_code
        }
        response = requests.get(f"{self.base_url}/meeting", headers=self.headers, params=params, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_updated_meetings(self, since: str, owning_authority_code: str = 'VIC') -> pd.DataFrame:
        """
        Returns a list of Meetings that have changed (scratchings or results) since the specified date/time.
        Meetings are limited to the authorities (owningauthoritycode) that the user has access to. 
        Best used for VIC meetings for timely data.

        Args:
            since (str): Must be a valid date and time. Use format YYYY-MM-DD HH:mm:ss. 
                         Is interpreted as Melbourne Local time unless time zone is specified.
            owning_authority_code (str, optional): Restrict meetings to the specified authority. 
                                                   Defaults to VIC. Valid values: 'ACT', 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA', 'NZ'.

        Returns:
            pd.DataFrame: A DataFrame containing the list of updated meetings.
        """
        params = {
            'since': since,
            'owningauthoritycode': owning_authority_code
        }
        response = requests.get(f"{self.base_url}/meeting/updated", headers=self.headers, params=params, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_meeting_details(self, meeting_id: int, format: str = 'all'):
        """
        Return all the details of the meeting, including races and runs. 
        Returns a dictionary if format is 'all', otherwise returns a DataFrame.

        Args:
            meeting_id (int): The unique identifier of the meeting. E.g.900012680 
            format (str, optional): The format of the meeting details to be returned. 
                                    Valid values: 'all', 'basic', 'basicplus', 'full', 'fullplus'. Default is 'all'.

        Returns:
            dict or pd.DataFrame: Depending on the format, either a dictionary or a DataFrame containing the meeting details.
        """
        params = {'format': format}
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}", headers=self.headers, params=params, timeout=30)
        if response.status_code == 200:
            if format == 'all':
                return response.json()  # Returns a dictionary for 'all' format
            else:
                return pd.DataFrame(response.json())  # Converts the JSON response to a DataFrame for other formats
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_meeting_form(self, meeting_id: int) -> dict:
        """
        Return all the details of the meeting, including races and runs. 
        Also includes Form data for the dogs in the meeting.

        Args:
            meeting_id (int): The unique identifier of the meeting. E.g. 900012680

        Returns:
            dict: A dictionary containing all the details of the meeting, including form data.
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/form", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_meeting_results(self, meeting_id: int) -> dict:
        """
        Return all the details of the meeting, including races, runs, and results.

        Args:
            meeting_id (int): The unique identifier of the meeting. E.g. 900012680.

        Returns:
            dict: A dictionary containing all the details of the meeting, including races, runs, and results.
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/results", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_meeting_results_first_split(self, meeting_id: int) -> dict:
        """
        Return all the details of the meeting, including races, runs, and results. 
        Includes First Split data for all dogs where available, and returns the most up-to-date data at all times.
        Note: This endpoint requires additional permissions.

        Args:
            meeting_id (int): The unique identifier of the meeting. Example value could be 900012680.

        Returns:
            dict: A dictionary containing all the details of the meeting, including races, runs, results, and First Split data.
        
        Raises:
            PermissionError: If the user is not authorized to access this endpoint (HTTP 401 error).
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/results/firstsplit", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        elif response.status_code == 401:  # Unauthorized access
            raise PermissionError("You are not authorized to access this endpoint.")
        else:
            response.raise_for_status()  # Raises an HTTPError for other unsuccessful status codes

    def get_meeting_races(self, meeting_id: int) -> dict:
        """
        Returns a list of all races for the specified meeting.

        Args:
            meeting_id (int): The unique identifier of the meeting. Example value could be 900012680.

        Returns:
            dict: A dictionary containing a list of all races for the specified meeting.
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/races", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_races_first_split(self, meeting_id: int) -> dict:
        """
        Returns a list of all races for the specified meeting. 
        Includes First Split data for all dogs where available, and returns the most up-to-date data at all times.
        Note: This endpoint requires additional permissions.

        Args:
            meeting_id (int): The unique identifier of the meeting. Example value could be 425059749.

        Returns:
            dict: A dictionary containing a list of all races with First Split data for the specified meeting.

        Raises:
            PermissionError: If the user is not authorized to access this endpoint (HTTP 401 error).
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/races/firstsplit", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        elif response.status_code == 401:  # Unauthorized access
            raise PermissionError("You are not authorized to access this endpoint.")
        else:
            response.raise_for_status()  # Raises an HTTPError for other unsuccessful status codes

    def get_meeting_field(self, meeting_id: int) -> dict:
        """
        Gets a minimal set of the latest field information for a meeting, primarily to get latest scratching and reserve details.

        Args:
            meeting_id (int): The unique identifier of the meeting. Example value could be 900012680.

        Returns:
            dict: A dictionary containing the latest field information for the specified meeting.
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/field", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_race_field(self, meeting_id: int, race_id: int) -> pd.DataFrame:
        """
        Gets a minimal set of the latest field information for a race within a meeting, primarily to get latest scratching and reserve details.

        Args:
            meeting_id (int): The id of the meeting to get the latest field for. E.g. 900012680
            race_id (int): The id of the race within the meeting to get the latest field for. E.g. 972428497

        Returns:
            pd.DataFrame: A DataFrame containing the latest field information for the specified race within the meeting.
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/field/{race_id}", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_race_field(self, meeting_id: int, race_id: int) -> dict:
        """
        Gets a minimal set of the latest field information for a race within a meeting, primarily to get latest scratching and reserve details.

        Args:
            meeting_id (int): The id of the meeting to get the latest field for.
            race_id (int): The id of the race within the meeting to get the latest field for.

        Returns:
            dict: A dictionary containing the latest field information for the specified race within the meeting.
        """
        response = requests.get(f"{self.base_url}/meeting/{meeting_id}/field/{race_id}", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    ### Race
    def get_races(self, from_date: str, to_date: str = None, owning_authority_code: str = None) -> pd.DataFrame:
        """
        Get a list of all races between the dates given. Constrained by any configured limits on the users Account's access to the specified state (owningAuthority).

        Args:
            from_date (str): Must be a valid date. Use format YYYY-MM-DD.
            to_date (str, optional): Must be a valid date if present. Use format YYYY-MM-DD. Defaults to the same date as from_date.
            owning_authority_code (str, optional): One of 'ACT', 'NSW', 'NT', 'QLD', 'SA', 'TAS', 'VIC', 'WA', 'NZ'.

        Returns:
            pd.DataFrame: A DataFrame containing all the races within the specified date range and owning authority.
        """
        params = {
            'from': from_date,
            'to': to_date or from_date,  # Defaults to from_date if to_date is not provided
            'owningauthoritycode': owning_authority_code
        }
        response = requests.get(f"{self.base_url}/race", headers=self.headers, params=params, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_races_for_meeting(self, meeting_id: int) -> dict:
        """
        Get the list of Races for a specified meeting.

        Args:
            meeting_id (int): The unique identifier of the meeting. Example value could be 900012673.

        Returns:
            dict: A dictionary containing the list of races for the specified meeting.
        """
        response = requests.get(f"{self.base_url}/race/meeting/{meeting_id}", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_race_result(self, race_id: int) -> dict:
        """
        Retrieves the result of a specific race.

        Args:
            race_id (int): The unique identifier of the race. Example value could be 972428497.

        Returns:
            dict: A dictionary containing the result of the specified race.
        """
        response = requests.get(f"{self.base_url}/race/{race_id}/result", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_race_runs(self, race_id: int) -> pd.DataFrame:
        """
        Returns a list of dogs and the details of their run within the specified race.

        Args:
            race_id (int): The unique identifier of the race. Example value could be 972428497.

        Returns:
            pd.DataFrame: A DataFrame containing the list of dogs and the details of their runs in the specified race.
        """
        response = requests.get(f"{self.base_url}/race/{race_id}/runs", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_race_runs_form(self, race_id: int) -> dict:
        """
        Returns a list of dogs and the details of their run within the specified race, including form data.

        Args:
            race_id (int): The id of the race for which to receive the list of Runs (dogs and their run details for the race specified).

        Returns:
            dict: A dictionary containing the list of dogs and the details of their runs, including form data, in the specified race.
        """
        response = requests.get(f"{self.base_url}/race/{race_id}/runs/form", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_race_field(self, race_id: int) -> dict:
        """
        Gets a minimal set of the latest field information for a race, primarily to get latest scratching and reserve details.

        Args:
            race_id (int): The unique identifier of the race. Example value could be 972428497.

        Returns:
            dict: A dictionary containing the latest field information for the specified race.
        """
        response = requests.get(f"{self.base_url}/race/{race_id}/field", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_race_runs_first_split(self, race_id: int) -> dict:
        """
        Returns a list of dogs and the details of their run within the specified race. 
        The results of this call include First Split information for each run if available and always returns the latest information.
        Note: This endpoint requires additional permissions.

        Args:
            race_id (int): The unique identifier of the race. Example value could be 509346808.

        Returns:
            dict: A dictionary containing the list of dogs and the details of their runs, including First Split information, in the specified race.
        
        Raises:
            PermissionError: If the user is not authorized to access this endpoint (HTTP 401 error).
        """
        response = requests.get(f"{self.base_url}/race/{race_id}/runs/firstsplit", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        elif response.status_code == 401:  # Unauthorized access
            raise PermissionError("You are not authorized to access this endpoint.")
        else:
            response.raise_for_status()  # Raises an HTTPError for other unsuccessful status codes

    def get_race_first_split(self, race_id: int) -> dict:
        """
        Returns a list of just the first split data for runs in the specified race.
        Requires the caller to have access to first split information.
        Note: This endpoint requires additional permissions.

        Args:
            race_id (int): The unique identifier of the race. Example value could be 972428497.

        Returns:
            dict: A dictionary containing just the first split data for the runs in the specified race.
        
        Raises:
            PermissionError: If the user is not authorized to access this endpoint (HTTP 401 error).
        """
        response = requests.get(f"{self.base_url}/race/{race_id}/firstsplit", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        elif response.status_code == 401:  # Unauthorized access
            raise PermissionError("You are not authorized to access this endpoint.")
        else:
            response.raise_for_status()  # Raises an HTTPError for other unsuccessful status codes

    def get_upcoming_races(self, from_datetime: str = None) -> pd.DataFrame:
        """
        Get a list of all remaining races for a particular date after the date and time given. 
        Defaults to the current date and time. (VIC races only).

        Args:
            from_datetime (str, optional): The start date and time for the query in YYYY-MM-DD HH:mm format. 
                                           Defaults to the current date and time.

        Returns:
            pd.DataFrame: A DataFrame containing all the remaining races after the specified date and time.
        """
        params = {'from': from_datetime} if from_datetime else {}
        response = requests.get(f"{self.base_url}/race/upcoming", headers=self.headers, params=params, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    ### RaceResult
    def get_recent_race_results(self) -> dict:
        """
        Get a list of the most recently finalised races with runs and exotic bet types for display on the website.

        Returns:
            dict: A dictionary containing the most recently finalized races, along with runs and exotic bet types.
        """
        response = requests.get(f"{self.base_url}/raceresult/recent", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    ### Race
    def get_runs_for_race(self, race_id: int) -> pd.DataFrame:
        """
        Returns a list of dogs and the details of their run within the specified race.

        Args:
            race_id (int): The unique identifier of the race. Example value could be 972428497.

        Returns:
            pd.DataFrame: A DataFrame containing the list of dogs and the details of their runs in the specified race.
        """
        response = requests.get(f"{self.base_url}/run/race/{race_id}", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    ### Statistics

    ### System
    def get_change_log(self) -> dict:
        """
        Returns change log.

        Returns:
            dict: A dictionary containing the change log.
        """
        response = requests.get(f"{self.base_url}/changelog", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_server_health(self) -> dict:
        """
        Returns indication of the health of the server.

        Returns:
            dict: A dictionary indicating the health of the server.
        """
        response = requests.get(f"{self.base_url}/health", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    def get_cache_health(self) -> dict:
        """
        Returns some stats about the internal usage of cache within the server.

        Returns:
            dict: A dictionary containing statistics about the server's cache usage.
        """
        response = requests.get(f"{self.base_url}/health/cache", headers=self.headers, timeout=30)
        if response.status_code == 200:
            return response.json()  # Returns a dictionary representing the JSON response
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    ### Trainers
    def search_trainers(self, search_term: str, exact_match: bool = False, records: int = 300) -> pd.DataFrame:
        """
        Returns a list of dogs and the details of their run within the specified race.

        Args:
            search_term (str): The full or partial name of the target greyhound trainer.
            exact_match (bool, optional): Limits the records returned to all trainers matched by first name and surname. Default is False.
            records (int, optional): The maximum number of records to return. Default is 300 hits.

        Returns:
            pd.DataFrame: A DataFrame containing the search results.
        """
        params = {
            'searchterm': search_term,
            'exactmatch': exact_match,
            'records': records
        }
        response = requests.get(f"{self.base_url}/search/trainers", headers=self.headers, params=params, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    ### TrialResults
    def get_trial_results(self, from_date: str, to_date: str = None) -> pd.DataFrame:
        """
        Returns a list of Trial Results between the two provided dates. 
        When the 'to' date is not supplied, it defaults to the same date as the date provided by 'from'. 
        Where these dates are outside the dates allowed by the configured dates allowed for the user's access 
        to the specified owning authority (state or NZ).

        Args:
            from_date (str): The start date for the query, in YYYY-MM-DD format.
            to_date (str, optional): The end date for the query, in YYYY-MM-DD format. Defaults to the same as 'from_date'.

        Returns:
            pd.DataFrame: A DataFrame containing the trial results between the specified dates.
        """
        params = {
            'from': from_date,
            'to': to_date or from_date  # Defaults to from_date if to_date is not provided
        }
        response = requests.get(f"{self.base_url}/trialresult", headers=self.headers, params=params, timeout=30)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

    ### Wagering
    ### Watchdog