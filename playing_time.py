class PlayingTime:
    def __init__(self, matches_played='N/A', starts='N/A', minutes='N/A', played_minutes='N/A'):
        self.__matches_played = matches_played
        self.__starts = starts
        self.__minutes = minutes
        self.__played_minutes = played_minutes

    def get_matches_played(self):
        return self.__matches_played

    def get_starts(self):
        return self.__starts

    def get_minutes(self):
        return self.__minutes

    def get_played_minutes(self):
        return self.__played_minutes

    def set_matches_played(self, matches_played):
        self.__matches_played = matches_played

    def set_starts(self, starts):
        self.__starts = starts

    def set_minutes(self, minutes):
        self.__minutes = minutes

    def set_played_minutes(self, played_minutes):
        self.__played_minutes = played_minutes

    def __str__(self):
        return (f"Playing Time:\n"
                f"Matches Played: {self.__matches_played}\n"
                f"Starts: {self.__starts}\n"
                f"Minutes: {self.__minutes}\n"
                f"Played Minutes: {self.__played_minutes}")
