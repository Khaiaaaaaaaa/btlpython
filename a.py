from player import Player
from playing_time import PlayingTime
from performance import Performance
from standard_expected import StandardExpected
from progression import Progression
from per_90_minutes import Per90Minutes
from goalkeeping_performance import GoalkeepingPerformance
from penalty_kicks import PenaltyKicks
from goalkeeping import Goalkeeping
from shooting_standard import ShootingStandard
from shooting_expected import ShootingExpected
from shooting import Shooting
from passing import Passing
from total import Total
from short import Short
from medium import Medium
from long import Long
from passing_expected import PassingExpected
from pass_types import PassTypes
from pass_type import PassType
from corner_kicks import CornerKicks
from outcomes import Outcomes
from goal_and_shot_creation import GoalAndShotCreation
from sca import SCA
from gca import GCA
from sca_types import SCATypes
from gca_types import GCATypes
from defensive_actions import DefensiveActions
from tackles import Tackles
from challenges import Challenges
from blocks import Blocks
from possession import Possession
from touches import Touches
from takeons import TakeOns
from carries import Carries
from receiving import Receiving
from playing_time_details import PlayingTimeDetails
from starts import Starts
from subs import Subs
from team_success import TeamSuccess
from team_success_xg import TeamSuccessxG
from miscellaneous_stats import MiscellaneousStats
from miscellaneous_performance import MiscellaneousPerformance
from aerial_duels import AerialDuels
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd


squads = ["18bb7c10/2023-2024/Arsenal-Stats", "8602292d/2023-2024/Aston-Villa-Stats", "4ba7cbea/2023-2024/Bournemouth-Stats", "cd051869/2023-2024/Brentford-Stats", "d07537b9/2023-2024/Brighton-and-Hove-Albion-Stats", "943e8050/2023-2024/Burnley-Stats", "cff3d9bb/2023-2024/Chelsea-Stats", "47c64c55/2023-2024/Crystal-Palace-Stats", "d3fd31cc/2023-2024/Everton-Stats", "fd962109/2023-2024/Fulham-Stats", "822bd0ba/2023-2024/Liverpool-Stats", "e297cd13/2023-2024/Luton-Town-Stats", "b8fd03ef/2023-2024/Manchester-City-Stats", "19538871/2023-2024/Manchester-United-Stats", "b2b47a98/2023-2024/Newcastle-United-Stats", "e4a775cb/2023-2024/Nottingham-Forest-Stats", "1df6b87e/2023-2024/Sheffield-United-Stats", "361ca564/2023-2024/Tottenham-Hotspur-Stats", "7c21e445/2023-2024/West-Ham-United-Stats", "8cec06e1/2023-2024/Wolverhampton-Wanderers-Stats"]
teams = [
    "Arsenal", 
    "Aston Villa", 
    "Bournemouth", 
    "Brentford", 
    "Brighton", 
    "Burnley", 
    "Chelsea", 
    "Crystal Palace", 
    "Everton", 
    "Fulham", 
    "Liverpool", 
    "Luton Town", 
    "Manchester City", 
    "Manchester Utd", 
    "Newcastle Utd", 
    "Nott'ham Forest", 
    "Sheffield Utd", 
    "Tottenham", 
    "West Ham", 
    "Wolves"
]


players_of_team = []
players = "Nothing"
def read_file(file_path):
    df = pd.read_csv(file_path)
    headers = pd.read_csv(file_path, header=None, nrows=3, delimiter=',',
                        index_col=0, keep_default_na=False).values.tolist()
    df = pd.read_csv(file_path, delimiter=',', header=[0, 1, 2], index_col=0)
    df.columns = pd.MultiIndex.from_arrays(headers)

    return df

def find_player(player):
    for i in range(len(players_of_team)):
        if(players_of_team[i] == player):
            return i
    return -1

def inject_miscellaneous_stats(df, i):
    team = teams[i]
    global players_of_team

    for idx in df.index:
        if(idx >= df.index.stop - 2): 
            break
        id = find_player(Player(
            df[('Unnamed: 0_level_0', 'Player')][idx],
            df[('Unnamed: 1_level_0', 'Nation')][idx],
            team,
            df[('Unnamed: 2_level_0', 'Pos')][idx],
            int(df[('Unnamed: 3_level_0', 'Age')][idx]) if not math.isnan(df[('Unnamed: 3_level_0', 'Age')][idx]) else 'N/A'
        ))

        miscellaneous_performance = MiscellaneousPerformance(
            int(df[('Performance', 'Fls')][idx]) if not math.isnan(df[('Performance', 'Fls')][idx]) else 'N/A',
            int(df[('Performance', 'Fld')][idx]) if not math.isnan(df[('Performance', 'Fld')][idx]) else 'N/A',
            int(df[('Performance', 'Off')][idx]) if not math.isnan(df[('Performance', 'Off')][idx]) else 'N/A',
            int(df[('Performance', 'Crs')][idx]) if not math.isnan(df[('Performance', 'Crs')][idx]) else 'N/A',
            int(df[('Performance', 'OG')][idx]) if not math.isnan(df[('Performance', 'OG')][idx]) else 'N/A',
            int(df[('Performance', 'Recov')][idx]) if not math.isnan(df[('Performance', 'Recov')][idx]) else 'N/A'
        )

        aerial_duels = AerialDuels(
            int(df[('Aerial Duels', 'Won')][idx]) if not math.isnan(df[('Aerial Duels', 'Won')][idx]) else 'N/A',
            int(df[('Aerial Duels', 'Lost')][idx]) if not math.isnan(df[('Aerial Duels', 'Lost')][idx]) else 'N/A',
            float(df[('Aerial Duels', 'Won%')][idx]) if not math.isnan(df[('Aerial Duels', 'Won%')][idx]) else 'N/A'
        )

        miscellaneous_stats = MiscellaneousStats(miscellaneous_performance, aerial_duels)
        players_of_team[id].set_miscellaneous_stats(miscellaneous_stats)


def inject_playing_time_details_info(df, i):
    team = teams[i]
    global players_of_team

    print(len(players_of_team))
    for idx in range(len(players_of_team)):
        starts = Starts(
            int(df[('Starts', 'Starts')][idx]) if not math.isnan(df[('Starts', 'Starts')][idx]) else 'N/A',
            int(df[('Starts', 'Mn/Start')][idx]) if not math.isnan(df[('Starts', 'Mn/Start')][idx]) else 'N/A',
            int(df[('Starts', 'Compl')][idx]) if not math.isnan(df[('Starts', 'Compl')][idx]) else 'N/A'
        )

        subs = Subs(
            int(df[('Subs', 'Subs')][idx]) if not math.isnan(df[('Subs', 'Subs')][idx]) else 'N/A',
            float(df[('Subs', 'Mn/Sub')][idx]) if not math.isnan(df[('Subs', 'Mn/Sub')][idx]) else 'N/A',
            int(df[('Subs', 'unSub')][idx]) if not math.isnan(df[('Subs', 'unSub')][idx]) else 'N/A'
        ) 

        team_success = TeamSuccess(
            float(df[('Team Success', 'PPM')][idx]) if not math.isnan(df[('Team Success', 'PPM')][idx]) else 'N/A',
            int(df[('Team Success', 'onG')][idx]) if not math.isnan(df[('Team Success', 'onG')][idx]) else 'N/A',
            int(df[('Team Success', 'onGA')][idx]) if not math.isnan(df[('Team Success', 'onGA')][idx]) else 'N/A'
        )

        team_success_xg = TeamSuccessxG(
            float(df[('Team Success (xG)', 'onxG')][idx]) if not math.isnan(df[('Team Success (xG)', 'onxG')][idx]) else 'N/A',
            float(df[('Team Success (xG)', 'onxGA')][idx]) if not math.isnan(df[('Team Success (xG)', 'onxGA')][idx]) else 'N/A'
        )

        playing_time_details = PlayingTimeDetails(starts, subs, team_success, team_success_xg)
        players_of_team[idx].set_playing_time_details(playing_time_details)

def injectpossession_info(df, i):
    team = teams[i]
    global players_of_team

    for idx in df.index:
        if(idx >= df.index.stop - 2): 
            break
        id = find_player(Player(
            df[('Unnamed: 0_level_0', 'Player')][idx],
            df[('Unnamed: 1_level_0', 'Nation')][idx],
            team,
            df[('Unnamed: 2_level_0', 'Pos')][idx],
            int(df[('Unnamed: 3_level_0', 'Age')][idx]) if not math.isnan(df[('Unnamed: 3_level_0', 'Age')][idx]) else 'N/A'
        ))

        touches = Touches(
            int(df[('Touches', 'Touches')][idx]) if not math.isnan(df[('Touches', 'Touches')][idx]) else 'N/A',
            int(df[('Touches', 'Def Pen')][idx]) if not math.isnan(df[('Touches', 'Def Pen')][idx]) else 'N/A',
            int(df[('Touches', 'Def 3rd')][idx]) if not math.isnan(df[('Touches', 'Def 3rd')][idx]) else 'N/A',
            int(df[('Touches', 'Mid 3rd')][idx]) if not math.isnan(df[('Touches', 'Mid 3rd')][idx]) else 'N/A',
            int(df[('Touches', 'Att 3rd')][idx]) if not math.isnan(df[('Touches', 'Att 3rd')][idx]) else 'N/A',
            int(df[('Touches', 'Att Pen')][idx]) if not math.isnan(df[('Touches', 'Att Pen')][idx]) else 'N/A',
            int(df[('Touches', 'Live')][idx]) if not math.isnan(df[('Touches', 'Live')][idx]) else 'N/A'
        )

        take_ons = TakeOns(
            int(df[('Take-Ons', 'Att')][idx]) if not math.isnan(df[('Take-Ons', 'Att')][idx]) else 'N/A',
            int(df[('Take-Ons', 'Succ')][idx]) if not math.isnan(df[('Take-Ons', 'Succ')][idx]) else 'N/A',
            float(df[('Take-Ons', 'Succ%')][idx]) if not math.isnan(df[('Take-Ons', 'Succ%')][idx]) else 'N/A',
            int(df[('Take-Ons', 'Tkld')][idx]) if not math.isnan(df[('Take-Ons', 'Tkld')][idx]) else 'N/A',
            float(df[('Take-Ons', 'Tkld%')][idx]) if not math.isnan(df[('Take-Ons', 'Tkld%')][idx]) else 'N/A'
        )

        carries = Carries(
            int(df[('Carries', 'Carries')][idx]) if not math.isnan(df[('Carries', 'Carries')][idx]) else 'N/A',
            int(df[('Carries', 'TotDist')][idx]) if not math.isnan(df[('Carries', 'TotDist')][idx]) else 'N/A',
            int(df[('Carries', 'PrgDist')][idx]) if not math.isnan(df[('Carries', 'PrgDist')][idx]) else 'N/A',
            int(df[('Carries', 'PrgC')][idx]) if not math.isnan(df[('Carries', 'PrgC')][idx]) else 'N/A',
            int(df[('Carries', '1/3')][idx]) if not math.isnan(df[('Carries', '1/3')][idx]) else 'N/A',
            int(df[('Carries', 'CPA')][idx]) if not math.isnan(df[('Carries', 'CPA')][idx]) else 'N/A',
            int(df[('Carries', 'Mis')][idx]) if not math.isnan(df[('Carries', 'Mis')][idx]) else 'N/A',
            int(df[('Carries', 'Dis')][idx]) if not math.isnan(df[('Carries', 'Dis')][idx]) else 'N/A'
        )

        receiving = Receiving(
            int(df[('Receiving', 'Rec')][idx]) if not math.isnan(df[('Receiving', 'Rec')][idx]) else 'N/A',
            int(df[('Receiving', 'PrgR')][idx]) if not math.isnan(df[('Receiving', 'PrgR')][idx]) else 'N/A'
        )

        possession = Possession(touches, take_ons, carries, receiving)
        players_of_team[id].set_possession(possession)



def inject_defensive_actions_info(df, i):
    team = teams[i]
    global players_of_team

    new_columns = list(df.columns)
    for i in range(len(new_columns) - 2, len(new_columns) - 6, -1):
        if(new_columns[i][0] != 'Blocks'):
            new_columns[i] = ('Blocks', new_columns[i][1])
    df.columns = pd.MultiIndex.from_tuples(new_columns)


    for idx in df.index:
        if(idx >= df.index.stop - 2): 
            break
        id = find_player(Player(
            df[('Unnamed: 0_level_0', 'Player')][idx],
            df[('Unnamed: 1_level_0', 'Nation')][idx],
            team,
            df[('Unnamed: 2_level_0', 'Pos')][idx],
            int(df[('Unnamed: 3_level_0', 'Age')][idx]) if not math.isnan(df[('Unnamed: 3_level_0', 'Age')][idx]) else 'N/A'
        ))

        tackles = Tackles(
            int(df[('Tackles', 'Tkl')][idx]) if not math.isnan(df[('Tackles', 'Tkl')][idx]) else 'N/A',
            int(df[('Tackles', 'TklW')][idx]) if not math.isnan(df[('Tackles', 'TklW')][idx]) else 'N/A',
            int(df[('Tackles', 'Def 3rd')][idx]) if not math.isnan(df[('Tackles', 'Def 3rd')][idx]) else 'N/A',
            int(df[('Tackles', 'Mid 3rd')][idx]) if not math.isnan(df[('Tackles', 'Mid 3rd')][idx]) else 'N/A',
            int(df[('Tackles', 'Att 3rd')][idx]) if not math.isnan(df[('Tackles', 'Att 3rd')][idx]) else 'N/A'
        )

        challenges = Challenges(
            int(df[('Challenges', 'Tkl')][idx]) if not math.isnan(df[('Challenges', 'Tkl')][idx]) else 'N/A',
            int(df[('Challenges', 'Att')][idx]) if not math.isnan(df[('Challenges', 'Att')][idx]) else 'N/A',
            float(df[('Challenges', 'Tkl%')][idx]) if not math.isnan(df[('Challenges', 'Tkl%')][idx]) else 'N/A',
            int(df[('Challenges', 'Lost')][idx]) if not math.isnan(df[('Challenges', 'Lost')][idx]) else 'N/A'
        )

        blocks = Blocks(
            int(df[('Blocks', 'Blocks')][idx]) if not math.isnan(df[('Blocks', 'Blocks')][idx]) else 'N/A',
            int(df[('Blocks', 'Sh')][idx]) if not math.isnan(df[('Blocks', 'Sh')][idx]) else 'N/A',
            int(df[('Blocks', 'Pass')][idx]) if not math.isnan(df[('Blocks', 'Pass')][idx]) else 'N/A',
            int(df[('Blocks', 'Int')][idx]) if not math.isnan(df[('Blocks', 'Int')][idx]) else 'N/A',
            int(df[('Blocks', 'Tkl+Int')][idx]) if not math.isnan(df[('Blocks', 'Tkl+Int')][idx]) else 'N/A',
            int(df[('Blocks', 'Clr')][idx]) if not math.isnan(df[('Blocks', 'Clr')][idx]) else 'N/A',
            int(df[('Blocks', 'Err')][idx]) if not math.isnan(df[('Blocks', 'Err')][idx]) else 'N/A'
        )

        defensive_actions = DefensiveActions(tackles, challenges, blocks)
        players_of_team[id].set_defensive_actions(defensive_actions)



def inject_goal_and_shot_creation_info(df, i):
    team = teams[i]
    global players_of_team

    for idx in df.index:
        if(idx >= df.index.stop - 2): 
            break
        id = find_player(Player(
            df[('Unnamed: 0_level_0', 'Player')][idx],
            df[('Unnamed: 1_level_0', 'Nation')][idx],
            team,
            df[('Unnamed: 2_level_0', 'Pos')][idx],
            int(df[('Unnamed: 3_level_0', 'Age')][idx]) if not math.isnan(df[('Unnamed: 3_level_0', 'Age')][idx]) else 'N/A'
        ))

        sca = SCA(
            int(df[('SCA', 'SCA')][idx]) if not math.isnan(df[('SCA', 'SCA')][idx]) else 'N/A',
            float(df[('SCA', 'SCA90')][idx]) if not math.isnan(df[('SCA', 'SCA90')][idx]) else 'N/A'
        )

        sca_types = SCATypes(
            int(df[('SCA Types', 'PassLive')][idx]) if not math.isnan(df[('SCA Types', 'PassLive')][idx]) else 'N/A',
            int(df[('SCA Types', 'PassDead')][idx]) if not math.isnan(df[('SCA Types', 'PassDead')][idx]) else 'N/A',
            int(df[('SCA Types', 'TO')][idx]) if not math.isnan(df[('SCA Types', 'TO')][idx]) else 'N/A',
            int(df[('SCA Types', 'Sh')][idx]) if not math.isnan(df[('SCA Types', 'Sh')][idx]) else 'N/A',
            int(df[('SCA Types', 'Fld')][idx]) if not math.isnan(df[('SCA Types', 'Fld')][idx]) else 'N/A',
            int(df[('SCA Types', 'Def')][idx]) if not math.isnan(df[('SCA Types', 'Def')][idx]) else 'N/A'
        )

        gca = GCA(
            int(df[('GCA', 'GCA')][idx]) if not math.isnan(df[('GCA', 'GCA')][idx]) else 'N/A',
            float(df[('GCA', 'GCA90')][idx]) if not math.isnan(df[('GCA', 'GCA90')][idx]) else 'N/A'
        )

        gca_types = GCATypes(
            int(df[('GCA Types', 'PassLive')][idx]) if not math.isnan(df[('GCA Types', 'PassLive')][idx]) else 'N/A',
            int(df[('GCA Types', 'PassDead')][idx]) if not math.isnan(df[('GCA Types', 'PassDead')][idx]) else 'N/A',
            int(df[('GCA Types', 'TO')][idx]) if not math.isnan(df[('GCA Types', 'TO')][idx]) else 'N/A',
            int(df[('GCA Types', 'Sh')][idx]) if not math.isnan(df[('GCA Types', 'Sh')][idx]) else 'N/A',
            int(df[('GCA Types', 'Fld')][idx]) if not math.isnan(df[('GCA Types', 'Fld')][idx]) else 'N/A',
            int(df[('GCA Types', 'Def')][idx]) if not math.isnan(df[('GCA Types', 'Def')][idx]) else 'N/A'
        )

        goal_and_shot_creation = GoalAndShotCreation(sca, sca_types, gca, gca_types)
        players_of_team[id].set_goal_and_shot_creation(goal_and_shot_creation)




def inject_passtypes_info(df, i):
    team = teams[i]
    global players_of_team

    for idx in df.index:
        if(idx >= df.index.stop - 2): 
            break
        id = find_player(Player(
            df[('Unnamed: 0_level_0', 'Player')][idx],
            df[('Unnamed: 1_level_0', 'Nation')][idx],
            team,
            df[('Unnamed: 2_level_0', 'Pos')][idx],
            int(df[('Unnamed: 3_level_0', 'Age')][idx]) if not math.isnan(df[('Unnamed: 3_level_0', 'Age')][idx]) else 'N/A'
        ))

        pass_type = PassType(
            int(df[('Pass Types', 'Live')][idx]) if not math.isnan(df[('Pass Types', 'Live')][idx]) else 'N/A',
            int(df[('Pass Types', 'Dead')][idx]) if not math.isnan(df[('Pass Types', 'Dead')][idx]) else 'N/A',
            int(df[('Pass Types', 'FK')][idx]) if not math.isnan(df[('Pass Types', 'FK')][idx]) else 'N/A',
            int(df[('Pass Types', 'TB')][idx]) if not math.isnan(df[('Pass Types', 'TB')][idx]) else 'N/A',
            int(df[('Pass Types', 'Sw')][idx]) if not math.isnan(df[('Pass Types', 'Sw')][idx]) else 'N/A',
            int(df[('Pass Types', 'Crs')][idx]) if not math.isnan(df[('Pass Types', 'Crs')][idx]) else 'N/A',
            int(df[('Pass Types', 'TI')][idx]) if not math.isnan(df[('Pass Types', 'TI')][idx]) else 'N/A',
            int(df[('Pass Types', 'CK')][idx]) if not math.isnan(df[('Pass Types', 'CK')][idx]) else 'N/A'
        )

        corner_kicks = CornerKicks(
            int(df[('Corner Kicks', 'In')][idx]) if not math.isnan(df[('Corner Kicks', 'In')][idx]) else 'N/A',
            int(df[('Corner Kicks', 'Out')][idx]) if not math.isnan(df[('Corner Kicks', 'Out')][idx]) else 'N/A',
            int(df[('Corner Kicks', 'Str')][idx]) if not math.isnan(df[('Corner Kicks', 'Str')][idx]) else 'N/A'
        )

        outcomes = Outcomes(
            int(df[('Outcomes', 'Cmp')][idx]) if not math.isnan(df[('Outcomes', 'Cmp')][idx]) else 'N/A',
            int(df[('Outcomes', 'Off')][idx]) if not math.isnan(df[('Outcomes', 'Off')][idx]) else 'N/A',
            int(df[('Outcomes', 'Blocks')][idx]) if not math.isnan(df[('Outcomes', 'Blocks')][idx]) else 'N/A'
        )

        pass_types = PassTypes(pass_type, corner_kicks, outcomes)
        players_of_team[id].set_pass_types(pass_types)


def inject_passing_info(df, i):
    team = teams[i]
    global players_of_team

    new_columns = list(df.columns)
    for i in range(len(new_columns) - 2, len(new_columns) - 11, -1):
        if(new_columns[i][0] != 'Expected'):
            new_columns[i] = ('Expected', new_columns[i][1])
    df.columns = pd.MultiIndex.from_tuples(new_columns)


    for idx in df.index:
        if(idx >= df.index.stop - 2): 
            break
        id = find_player(Player(
            df[('Unnamed: 0_level_0', 'Player')][idx],
            df[('Unnamed: 1_level_0', 'Nation')][idx],
            team,
            df[('Unnamed: 2_level_0', 'Pos')][idx],
            int(df[('Unnamed: 3_level_0', 'Age')][idx]) if not math.isnan(df[('Unnamed: 3_level_0', 'Age')][idx]) else 'N/A'
        ))

        total = Total(
            int(df[('Total', 'Cmp')][idx]) if not math.isnan(df[('Total', 'Cmp')][idx]) else 'N/A',
            int(df[('Total', 'Att')][idx]) if not math.isnan(df[('Total', 'Att')][idx]) else 'N/A',
            float(df[('Total', 'Cmp%')][idx]) if not math.isnan(df[('Total', 'Cmp%')][idx]) else 'N/A',
            int(df[('Total', 'TotDist')][idx]) if not math.isnan(df[('Total', 'TotDist')][idx]) else 'N/A',
            int(df[('Total', 'PrgDist')][idx]) if not math.isnan(df[('Total', 'PrgDist')][idx]) else 'N/A'
        )

        short = Short(
            int(df[('Short', 'Cmp')][idx]) if not math.isnan(df[('Short', 'Cmp')][idx]) else 'N/A',
            int(df[('Short', 'Att')][idx]) if not math.isnan(df[('Short', 'Att')][idx]) else 'N/A',
            float(df[('Short', 'Cmp%')][idx]) if not math.isnan(df[('Short', 'Cmp%')][idx]) else 'N/A'
        )

        medium = Medium(
            int(df[('Medium', 'Cmp')][idx]) if not math.isnan(df[('Medium', 'Cmp')][idx]) else 'N/A',
            int(df[('Medium', 'Att')][idx]) if not math.isnan(df[('Medium', 'Att')][idx]) else 'N/A',
            float(df[('Medium', 'Cmp%')][idx]) if not math.isnan(df[('Medium', 'Cmp%')][idx]) else 'N/A'
        )

        long = Long(
            int(df[('Long', 'Cmp')][idx]) if not math.isnan(df[('Long', 'Cmp')][idx]) else 'N/A',
            int(df[('Long', 'Att')][idx]) if not math.isnan(df[('Long', 'Att')][idx]) else 'N/A',
            float(df[('Long', 'Cmp%')][idx]) if not math.isnan(df[('Long', 'Cmp%')][idx]) else 'N/A'
        )

        passing_expected = PassingExpected(
            int(df[('Expected', 'Ast')][idx]) if not math.isnan(df[('Expected', 'Ast')][idx]) else 'N/A',
            float(df[('Expected', 'xAG')][idx]) if not math.isnan(df[('Expected', 'xAG')][idx]) else 'N/A',
            float(df[('Expected', 'xA')][idx]) if not math.isnan(df[('Expected', 'xA')][idx]) else 'N/A',
            float(df[('Expected', 'A-xAG')][idx]) if not math.isnan(df[('Expected', 'A-xAG')][idx]) else 'N/A',
            int(df[('Expected', 'KP')][idx]) if not math.isnan(df[('Expected', 'KP')][idx]) else 'N/A',
            int(df[('Expected', '1/3')][idx]) if not math.isnan(df[('Expected', '1/3')][idx]) else 'N/A',
            int(df[('Expected', 'PPA')][idx]) if not math.isnan(df[('Expected', 'PPA')][idx]) else 'N/A',
            int(df[('Expected', 'CrsPA')][idx]) if not math.isnan(df[('Expected', 'CrsPA')][idx]) else 'N/A',
            int(df[('Expected', 'PrgP')][idx]) if not math.isnan(df[('Expected', 'PrgP')][idx]) else 'N/A'
        )

        passing = Passing(total, short, medium, long, passing_expected)
        players_of_team[id].set_passing(passing)



def inject_shooting_info(df, i):
    team = teams[i]
    global players_of_team

    for idx in df.index:
        if(idx >= df.index.stop - 2): 
            break
        id = find_player(Player(
            df[('Unnamed: 0_level_0', 'Player')][idx],
            df[('Unnamed: 1_level_0', 'Nation')][idx],
            team,
            df[('Unnamed: 2_level_0', 'Pos')][idx],
            int(df[('Unnamed: 3_level_0', 'Age')][idx]) if not math.isnan(df[('Unnamed: 3_level_0', 'Age')][idx]) else 'N/A'
        ))

        shooting_standard = ShootingStandard(
            int(df[('Standard', 'Gls')][idx]) if not math.isnan(df[('Standard', 'Gls')][idx]) else 'N/A',
            int(df[('Standard', 'Sh')][idx]) if not math.isnan(df[('Standard', 'Sh')][idx]) else 'N/A',
            int(df[('Standard', 'SoT')][idx]) if not math.isnan(df[('Standard', 'SoT')][idx]) else 'N/A',
            float(df[('Standard', 'SoT%')][idx]) if not math.isnan(df[('Standard', 'SoT%')][idx]) else 'N/A',
            float(df[('Standard', 'Sh/90')][idx]) if not math.isnan(df[('Standard', 'Sh/90')][idx]) else 'N/A',
            float(df[('Standard', 'SoT/90')][idx]) if not math.isnan(df[('Standard', 'SoT/90')][idx]) else 'N/A',
            float(df[('Standard', 'G/Sh')][idx]) if not math.isnan(df[('Standard', 'G/Sh')][idx]) else 'N/A',
            float(df[('Standard', 'G/SoT')][idx]) if not math.isnan(df[('Standard', 'G/SoT')][idx]) else 'N/A',
            float(df[('Standard', 'Dist')][idx]) if not math.isnan(df[('Standard', 'Dist')][idx]) else 'N/A',
            int(df[('Standard', 'FK')][idx]) if not math.isnan(df[('Standard', 'FK')][idx]) else 'N/A',
            int(df[('Standard', 'PK')][idx]) if not math.isnan(df[('Standard', 'PK')][idx]) else 'N/A',
            int(df[('Standard', 'PKatt')][idx]) if not math.isnan(df[('Standard', 'PKatt')][idx]) else 'N/A'
        )

        shooting_expected = ShootingExpected(
            float(df[('Expected', 'xG')][idx]) if not math.isnan(df[('Expected', 'xG')][idx]) else 'N/A',
            float(df[('Expected', 'npxG')][idx]) if not math.isnan(df[('Expected', 'npxG')][idx]) else 'N/A',
            float(df[('Expected', 'npxG/Sh')][idx]) if not math.isnan(df[('Expected', 'npxG/Sh')][idx]) else 'N/A',
            float(df[('Expected', 'G-xG')][idx]) if not math.isnan(df[('Expected', 'G-xG')][idx]) else 'N/A',
            float(df[('Expected', 'np:G-xG')][idx]) if not math.isnan(df[('Expected', 'np:G-xG')][idx]) else 'N/A'
        )

        shooting = Shooting(shooting_standard, shooting_expected)
        players_of_team[id].set_shooting(shooting)



def inject_goalkeeping_info(df, i):
    team = teams[i]
    global players_of_team

    for idx in df.index:
        if(idx >= df.index.stop - 2): 
            break
        id = find_player(Player(
            df[('Unnamed: 0_level_0', 'Player')][idx],
            df[('Unnamed: 1_level_0', 'Nation')][idx],
            team,
            df[('Unnamed: 2_level_0', 'Pos')][idx],
            int(df[('Unnamed: 3_level_0', 'Age')][idx]) if not math.isnan(df[('Unnamed: 3_level_0', 'Age')][idx]) else 'N/A'
        ))

        goalkeeping_performance = GoalkeepingPerformance(
            int(df[('Performance', 'GA')][idx]) if not math.isnan(df[('Performance', 'GA')][idx]) else 'N/A',
            float(df[('Performance', 'GA90')][idx]) if not math.isnan(df[('Performance', 'GA90')][idx]) else 'N/A',
            int(df[('Performance', 'SoTA')][idx]) if not math.isnan(df[('Performance', 'SoTA')][idx]) else 'N/A',
            int(df[('Performance', 'Saves')][idx]) if not math.isnan(df[('Performance', 'Saves')][idx]) else 'N/A',
            float(df[('Performance', 'Save%')][idx]) if not math.isnan(df[('Performance', 'Save%')][idx]) else 'N/A',
            int(df[('Performance', 'W')][idx]) if not math.isnan(df[('Performance', 'W')][idx]) else 'N/A',
            int(df[('Performance', 'D')][idx]) if not math.isnan(df[('Performance', 'D')][idx]) else 'N/A',
            int(df[('Performance', 'L')][idx]) if not math.isnan(df[('Performance', 'L')][idx]) else 'N/A',
            int(df[('Performance', 'CS')][idx]) if not math.isnan(df[('Performance', 'CS')][idx]) else 'N/A',
            float(df[('Performance', 'CS%')][idx]) if not math.isnan(df[('Performance', 'CS%')][idx]) else 'N/A'
        )

        penalty_kicks = PenaltyKicks(
            int(df[('Penalty Kicks', 'PKatt')][idx]) if not math.isnan(df[('Penalty Kicks', 'PKatt')][idx]) else 'N/A',
            int(df[('Penalty Kicks', 'PKA')][idx]) if not math.isnan(df[('Penalty Kicks', 'PKA')][idx]) else 'N/A',
            int(df[('Penalty Kicks', 'PKsv')][idx]) if not math.isnan(df[('Penalty Kicks', 'PKsv')][idx]) else 'N/A',
            int(df[('Penalty Kicks', 'PKm')][idx]) if not math.isnan(df[('Penalty Kicks', 'PKm')][idx]) else 'N/A',
            float(df[('Penalty Kicks', 'Save%')][idx]) if not math.isnan(df[('Penalty Kicks', 'Save%')][idx]) else 'N/A'
        )

        goalkeeping = Goalkeeping(goalkeeping_performance, penalty_kicks)
        players_of_team[id].set_goalkeeping(goalkeeping)
        

def inject_standard_info(df, i):
    pd.set_option('display.max_columns', None)
    name = ""
    nation = ""
    position = ""
    age = None
    playing_time = None
    performance = None
    standard_expected = None
    progression = None
    per_90_minutes = None 

    team = teams[i]
    global players_of_team

    df.columns = pd.MultiIndex.from_tuples(
        [('Playing Time', 'MP') if col == ('Unnamed: 4_level_0', 'MP') else col for col in df.columns]
    )

    

    for idx in df.index:
        if idx >= df.index.stop - 2: 
            break

        name = df[('Unnamed: 0_level_0', 'Player')][idx]
        nation = df[('Unnamed: 1_level_0', 'Nation')][idx]
        position = df[('Unnamed: 2_level_0', 'Pos')][idx]
        age = int(df[('Unnamed: 3_level_0', 'Age')][idx]) if not math.isnan(df[('Unnamed: 3_level_0', 'Age')][idx]) else 'N/A'

        played_minutes = (float(df[('Playing Time', '90s')][idx]) * 90) if not math.isnan(df[('Playing Time', '90s')][idx]) else 'N/A'
        if played_minutes == 'N/A' or played_minutes <= 90:
            continue

        playing_time = PlayingTime(
            int(df[('Playing Time', 'MP')][idx]) if not math.isnan(df[('Playing Time', 'MP')][idx]) else 'N/A', 
            int(df[('Playing Time', 'Starts')][idx]) if not math.isnan(df[('Playing Time', 'Starts')][idx]) else 'N/A',
            int(df[('Playing Time', 'Min')][idx]) if not math.isnan(df[('Playing Time', 'Min')][idx]) else 'N/A', 
            played_minutes
        )

        performance = Performance(
            int(df[('Performance', 'G-PK')][idx]) if not math.isnan(df[('Performance', 'G-PK')][idx]) else 'N/A', 
            int(df[('Performance', 'PK')][idx]) if not math.isnan(df[('Performance', 'PK')][idx]) else 'N/A',
            int(df[('Performance', 'Ast')][idx]) if not math.isnan(df[('Performance', 'Ast')][idx]) else 'N/A', 
            int(df[('Performance', 'CrdY')][idx]) if not math.isnan(df[('Performance', 'CrdY')][idx]) else 'N/A',
            int(df[('Performance', 'CrdR')][idx]) if not math.isnan(df[('Performance', 'CrdR')][idx]) else 'N/A'
        )

        standard_expected = StandardExpected(
            float(df[('Expected', 'xG')][idx]) if not math.isnan(df[('Expected', 'xG')][idx]) else 'N/A', 
            float(df[('Expected', 'npxG')][idx]) if not math.isnan(df[('Expected', 'npxG')][idx]) else 'N/A', 
            float(df[('Expected', 'xAG')][idx]) if not math.isnan(df[('Expected', 'xAG')][idx]) else 'N/A'
        )

        progression = Progression(
            int(df[('Progression', 'PrgC')][idx]) if not math.isnan(df[('Progression', 'PrgC')][idx]) else 'N/A', 
            int(df[('Progression', 'PrgP')][idx]) if not math.isnan(df[('Progression', 'PrgP')][idx]) else 'N/A', 
            int(df[('Progression', 'PrgR')][idx]) if not math.isnan(df[('Progression', 'PrgR')][idx]) else 'N/A'
        )

        per_90_minutes = Per90Minutes(
            float(df[('Per 90 Minutes', 'Gls')][idx]) if not math.isnan(df[('Per 90 Minutes', 'Gls')][idx]) else 'N/A',
            float(df[('Per 90 Minutes', 'Ast')][idx]) if not math.isnan(df[('Per 90 Minutes', 'Ast')][idx]) else 'N/A',
            float(df[('Per 90 Minutes', 'G+A')][idx]) if not math.isnan(df[('Per 90 Minutes', 'G+A')][idx]) else 'N/A',
            float(df[('Per 90 Minutes', 'G-PK')][idx]) if not math.isnan(df[('Per 90 Minutes', 'G-PK')][idx]) else 'N/A',
            float(df[('Per 90 Minutes', 'G+A-PK')][idx]) if not math.isnan(df[('Per 90 Minutes', 'G+A-PK')][idx]) else 'N/A',
            float(df[('Per 90 Minutes', 'xG')][idx]) if not math.isnan(df[('Per 90 Minutes', 'xG')][idx]) else 'N/A',
            float(df[('Per 90 Minutes', 'xAG')][idx]) if not math.isnan(df[('Per 90 Minutes', 'xAG')][idx]) else 'N/A',
            float(df[('Per 90 Minutes', 'xG+xAG')][idx]) if not math.isnan(df[('Per 90 Minutes', 'xG+xAG')][idx]) else 'N/A',
            float(df[('Per 90 Minutes', 'npxG')][idx]) if not math.isnan(df[('Per 90 Minutes', 'npxG')][idx]) else 'N/A',
            float(df[('Per 90 Minutes', 'npxG+xAG')][idx]) if not math.isnan(df[('Per 90 Minutes', 'npxG+xAG')][idx]) else 'N/A'
        )

        player = Player(name, nation, team, position, age, playing_time, performance, standard_expected, progression, per_90_minutes)
        players_of_team.append(player)

def task1():
    global players
    global players_of_team
    for i in range(1, len(squads) + 1):
        print(i)  
        df = pd.read_html("https://f...content-available-to-author-only...f.com/en/squads/" + squads[i - 1])
        players_of_team = []
        inject_standard_info(df[0], i - 1)
        inject_goalkeeping_info(df[2],i - 1)
        inject_shooting_info(df[4], i - 1)
        inject_passing_info(df[5], i - 1)
        inject_passtypes_info(df[6], i - 1)
        inject_goal_and_shot_creation_info(df[7], i - 1)
        inject_defensive_actions_info(df[8], i - 1)
        injectpossession_info(df[9], i - 1)
        inject_playing_time_details_info(df[10], i - 1)
        inject_miscellaneous_stats(df[11], i - 1)
        
        if players == "Nothing":
            players = players_of_team
        else:
            players = players + players_of_team
    players = sorted(players, key=lambda player: (player.get_name().split()[0], -player.get_age_for_comparing()))
    

    
    count = 0
    for pl in players:
        if(pl.get_age() >= 23.39 and pl.get_age() <=25.34): count+=1
    print(count)
    data = {
    # Basic info
        ('Basic Info','' ,'Name'): [player.get_name() for player in players],
        ('Basic Info', '','Nation'): [player.get_nation() for player in players],
        ('Basic Info', '','Team'): [player.get_team() for player in players],
        ('Basic Info', '','Position'): [player.get_position() for player in players],
        ('Basic Info', '','Age'): [player.get_age() for player in players],

        # Playing Time
        ('Basic Info', 'Playing Time', 'MP'): [player.get_playing_time().get_matches_played() for player in players],
        ('Basic Info', 'Playing Time', 'Starts'): [player.get_playing_time().get_starts() for player in players],
        ('Basic Info', 'Playing Time', 'Mins'): [player.get_playing_time().get_minutes() for player in players],

        # Performance
        ('Basic Info', 'Performance', 'G-PK'): [player.get_performance().get_non_penalty_goals() for player in players],
        ('Basic Info', 'Performance', 'PK'): [player.get_performance().get_penalty_goals() for player in players],
        ('Basic Info', 'Performance', 'Ast'): [player.get_performance().get_assists() for player in players],
        ('Basic Info', 'Performance', 'CrdY'): [player.get_performance().get_yellow_cards() for player in players],
        ('Basic Info', 'Performance', 'CrdR'): [player.get_performance().get_red_cards() for player in players],

        # Expected Stats
        ('Basic Info', 'Expected', 'xG'): [player.get_expected().get_xG() for player in players],
        ('Basic Info', 'Expected', 'npxG'): [player.get_expected().get_npxG() for player in players],
        ('Basic Info', 'Expected', 'xAG'): [player.get_expected().get_xAG() for player in players],

        # Progression
        ('Basic Info', 'Progression', 'PrgC'): [player.get_progression().get_prg_c() for player in players],
        ('Basic Info', 'Progression', 'PrgP'): [player.get_progression().get_prg_p() for player in players],
        ('Basic Info', 'Progression', 'PrgR'): [player.get_progression().get_prg_r() for player in players],

        # Per 90 minutes
        ('Basic Info', 'Per 90 Minutes', 'Gls'): [player.get_per_90_minutes().get_gls() for player in players],
        ('Basic Info', 'Per 90 Minutes', 'Ast'): [player.get_per_90_minutes().get_ast() for player in players],
        ('Basic Info', 'Per 90 Minutes', 'G+A'): [player.get_per_90_minutes().get_g_plus_a() for player in players],
        ('Basic Info', 'Per 90 Minutes', 'G-PK'): [player.get_per_90_minutes().get_g_minus_pk() for player in players],
        ('Basic Info', 'Per 90 Minutes', 'G+A-PK'): [player.get_per_90_minutes().get_g_plus_a_minus_pk() for player in players],
        ('Basic Info', 'Per 90 Minutes', 'xG'): [player.get_per_90_minutes().get_xG() for player in players],
        ('Basic Info', 'Per 90 Minutes', 'xAG'): [player.get_per_90_minutes().get_xAG() for player in players],
        ('Basic Info', 'Per 90 Minutes', 'xG + xAG'): [player.get_per_90_minutes().get_xG_plus_xAG() for player in players],
        ('Basic Info', 'Per 90 Minutes', 'npxG'): [player.get_per_90_minutes().get_npxG() for player in players],
        ('Basic Info', 'Per 90 Minutes', 'npxG + xAG'): [player.get_per_90_minutes().get_npxG_plus_xAG() for player in players],

        # Goalkeeping
        ('Goalkeeping', 'Performance', 'GA'): [player.get_goalkeeping().get_performance().get_ga() for player in players],
        ('Goalkeeping', 'Performance', 'GA90'): [player.get_goalkeeping().get_performance().get_ga90() for player in players],
        ('Goalkeeping', 'Performance', 'SoTA'): [player.get_goalkeeping().get_performance().get_sota() for player in players],
        ('Goalkeeping', 'Performance', 'Saves'): [player.get_goalkeeping().get_performance().get_saves() for player in players],
        ('Goalkeeping', 'Performance', 'Save%'): [player.get_goalkeeping().get_performance().get_save_percent() for player in players],
        ('Goalkeeping', 'Performance', 'W'): [player.get_goalkeeping().get_performance().get_w() for player in players],
        ('Goalkeeping', 'Performance', 'D'): [player.get_goalkeeping().get_performance().get_d() for player in players],
        ('Goalkeeping', 'Performance', 'L'): [player.get_goalkeeping().get_performance().get_l() for player in players],
        ('Goalkeeping', 'Performance', 'CS'): [player.get_goalkeeping().get_performance().get_cs() for player in players],
        ('Goalkeeping', 'Performance', 'CS%'): [player.get_goalkeeping().get_performance().get_cs_percent() for player in players],

        ('Goalkeeping', 'Penalty Kicks', 'PKatt'): [player.get_goalkeeping().get_penalty_kicks().get_pk_att() for player in players],
        ('Goalkeeping', 'Penalty Kicks', 'PKA'): [player.get_goalkeeping().get_penalty_kicks().get_pka() for player in players],
        ('Goalkeeping', 'Penalty Kicks', 'PKsv'): [player.get_goalkeeping().get_penalty_kicks().get_pk_sv() for player in players],
        ('Goalkeeping', 'Penalty Kicks', 'PKm'): [player.get_goalkeeping().get_penalty_kicks().get_pk_m() for player in players],
        ('Goalkeeping', 'Penalty Kicks', 'Save%'): [player.get_goalkeeping().get_penalty_kicks().get_save_percent() for player in players],


        # Shooting
        ('Shooting', 'Standard', 'Gls'): [player.get_shooting().get_standard().get_gls() for player in players],
        ('Shooting', 'Standard', 'Sh'): [player.get_shooting().get_standard().get_sh() for player in players],
        ('Shooting', 'Standard', 'SoT'): [player.get_shooting().get_standard().get_sot() for player in players],
        ('Shooting', 'Standard', 'SoT%'): [player.get_shooting().get_standard().get_sot_percent() for player in players],
        ('Shooting', 'Standard', 'Sh/90'): [player.get_shooting().get_standard().get_sh_per_90() for player in players],
        ('Shooting', 'Standard', 'SoT/90'): [player.get_shooting().get_standard().get_sot_per_90() for player in players],
        ('Shooting', 'Standard', 'G/Sh'): [player.get_shooting().get_standard().get_g_per_sh() for player in players],
        ('Shooting', 'Standard', 'G/SoT'): [player.get_shooting().get_standard().get_g_per_sot() for player in players],
        ('Shooting', 'Standard', 'Dist'): [player.get_shooting().get_standard().get_dist() for player in players],
        ('Shooting', 'Standard', 'FK'): [player.get_shooting().get_standard().get_fk() for player in players],
        ('Shooting', 'Standard', 'PK'): [player.get_shooting().get_standard().get_pk() for player in players],
        ('Shooting', 'Standard', 'PKatt'): [player.get_shooting().get_standard().get_pkat() for player in players],

        # Expected Shooting
        ('Shooting', 'Expected', 'xG'): [player.get_shooting().get_shooting_expected().get_xG() for player in players],
        ('Shooting', 'Expected', 'npxG'): [player.get_shooting().get_shooting_expected().get_npxG() for player in players],
        ('Shooting', 'Expected', 'npxG/Sh'): [player.get_shooting().get_shooting_expected().get_npxG_per_sh() for player in players],
        ('Shooting', 'Expected', 'G-xG'): [player.get_shooting().get_shooting_expected().get_g_minus_xG() for player in players],
        ('Shooting', 'Expected', 'np:G-xG'): [player.get_shooting().get_shooting_expected().get_np_g_minus_xG() for player in players],

        # Passing
        # Total Passing
        ('Passing', 'Total', 'Cmp'): [player.get_passing().get_total().get_cmp() for player in players],
        ('Passing', 'Total', 'Att'): [player.get_passing().get_total().get_att() for player in players],
        ('Passing', 'Total', 'Cmp%'): [player.get_passing().get_total().get_cmp_percent() for player in players],
        ('Passing', 'Total', 'TotDist'): [player.get_passing().get_total().get_tot_dist() for player in players],
        ('Passing', 'Total', 'PrgDist'): [player.get_passing().get_total().get_prg_dist() for player in players],

        # Short Passing
        ('Passing', 'Short', 'Cmp'): [player.get_passing().get_short().get_cmp() for player in players],
        ('Passing', 'Short', 'Att'): [player.get_passing().get_short().get_att() for player in players],
        ('Passing', 'Short', 'Cmp%'): [player.get_passing().get_short().get_cmp_percent() for player in players],

        # Medium Passing
        ('Passing', 'Medium', 'Cmp'): [player.get_passing().get_medium().get_cmp() for player in players],
        ('Passing', 'Medium', 'Att'): [player.get_passing().get_medium().get_att() for player in players],
        ('Passing', 'Medium', 'Cmp%'): [player.get_passing().get_medium().get_cmppercent() for player in players],

        # Long Passing
        ('Passing', 'Long', 'Cmp'): [player.get_passing().get_long().get_cmp() for player in players],
        ('Passing', 'Long', 'Att'): [player.get_passing().get_long().get_att() for player in players],
        ('Passing', 'Long', 'Cmp%'): [player.get_passing().get_long().get_cmppercent() for player in players],

        # Expected Passing
        ('Passing', 'Expected', 'Ast'): [player.get_passing().get_passing_expected().get_ast() for player in players],
        ('Passing', 'Expected', 'xAG'): [player.get_passing().get_passing_expected().get_xAG() for player in players],
        ('Passing', 'Expected', 'xA'): [player.get_passing().get_passing_expected().get_xA() for player in players],
        ('Passing', 'Expected', 'A-xAG'): [player.get_passing().get_passing_expected().get_a_minus_xAG() for player in players],
        ('Passing', 'Expected', 'KP'): [player.get_passing().get_passing_expected().get_kp() for player in players],
        ('Passing', 'Expected', '1/3'): [player.get_passing().get_passing_expected().get_one_third() for player in players],
        ('Passing', 'Expected', 'PPA'): [player.get_passing().get_passing_expected().get_ppa() for player in players],
        ('Passing', 'Expected', 'CrsPA'): [player.get_passing().get_passing_expected().get_crsPA() for player in players],
        ('Passing', 'Expected', 'PrgP'): [player.get_passing().get_passing_expected().get_prgP() for player in players],

        # Pass Types
        # Pass Types
        ('Pass Types', 'Pass Types', 'Live'): [player.get_pass_types().get_pass_type().get_live() for player in players],
        ('Pass Types', 'Pass Types', 'Dead'): [player.get_pass_types().get_pass_type().get_dead() for player in players],
        ('Pass Types', 'Pass Types', 'FK'): [player.get_pass_types().get_pass_type().get_fk() for player in players],
        ('Pass Types', 'Pass Types', 'TB'): [player.get_pass_types().get_pass_type().get_tb() for player in players],
        ('Pass Types', 'Pass Types', 'Sw'): [player.get_pass_types().get_pass_type().get_sw() for player in players],
        ('Pass Types', 'Pass Types', 'Crs'): [player.get_pass_types().get_pass_type().get_crs() for player in players],
        ('Pass Types', 'Pass Types', 'TI'): [player.get_pass_types().get_pass_type().get_ti() for player in players],
        ('Pass Types', 'Pass Types', 'CK'): [player.get_pass_types().get_pass_type().get_ck() for player in players],

        # Corner Kicks
        ('Pass Types', 'Corner Kicks', 'In'): [player.get_pass_types().get_corner_kicks().get_in_kick() for player in players],
        ('Pass Types', 'Corner Kicks', 'Out'): [player.get_pass_types().get_corner_kicks().get_out_kick() for player in players],
        ('Pass Types', 'Corner Kicks', 'Str'): [player.get_pass_types().get_corner_kicks().get_str_kick() for player in players],

        # Outcomes
        ('Pass Types', 'Outcomes', 'Cmp'): [player.get_pass_types().get_outcomes().get_cmp() for player in players],
        ('Pass Types', 'Outcomes', 'Off'): [player.get_pass_types().get_outcomes().get_off() for player in players],
        ('Pass Types', 'Outcomes', 'Block'): [player.get_pass_types().get_outcomes().get_blocks() for player in players],

        # Goal and Shot Creation
        # SCA
        ('Goal and Shot Creation', 'SCA', 'SCA'): [player.get_goal_and_shot_creation().get_sca().get_sca() for player in players],
        ('Goal and Shot Creation', 'SCA', 'SCA90'): [player.get_goal_and_shot_creation().get_sca().get_sca90() for player in players],

        # SCA Types
        ('Goal and Shot Creation', 'SCA Types', 'PassLive'): [player.get_goal_and_shot_creation().get_sca_types().get_pass_live() for player in players],
        ('Goal and Shot Creation', 'SCA Types', 'PassDead'): [player.get_goal_and_shot_creation().get_sca_types().get_pass_dead() for player in players],
        ('Goal and Shot Creation', 'SCA Types', 'TO'): [player.get_goal_and_shot_creation().get_sca_types().get_to() for player in players],
        ('Goal and Shot Creation', 'SCA Types', 'Sh'): [player.get_goal_and_shot_creation().get_sca_types().get_sh() for player in players],
        ('Goal and Shot Creation', 'SCA Types', 'Fld'): [player.get_goal_and_shot_creation().get_sca_types().get_fld() for player in players],
        ('Goal and Shot Creation', 'SCA Types', 'Def'): [player.get_goal_and_shot_creation().get_sca_types().get_def() for player in players],

        # GCA
        ('Goal and Shot Creation', 'GCA', 'GCA'): [player.get_goal_and_shot_creation().get_gca().get_gca() for player in players],
        ('Goal and Shot Creation', 'GCA', 'GCA90'): [player.get_goal_and_shot_creation().get_gca().get_gca90() for player in players],

        # GCA Types
        ('Goal and Shot Creation', 'GCA Types', 'PassLive'): [player.get_goal_and_shot_creation().get_gca_types().get_pass_live() for player in players],
        ('Goal and Shot Creation', 'GCA Types', 'PassDead'): [player.get_goal_and_shot_creation().get_gca_types().get_pass_dead() for player in players],
        ('Goal and Shot Creation', 'GCA Types', 'TO'): [player.get_goal_and_shot_creation().get_gca_types().get_to() for player in players],
        ('Goal and Shot Creation', 'GCA Types', 'Sh'): [player.get_goal_and_shot_creation().get_gca_types().get_sh() for player in players],
        ('Goal and Shot Creation', 'GCA Types', 'Fld'): [player.get_goal_and_shot_creation().get_gca_types().get_fld() for player in players],
        ('Goal and Shot Creation', 'GCA Types', 'Def'): [player.get_goal_and_shot_creation().get_gca_types().get_def() for player in players],

        # Defensive Actions
        # Tackles
        ('Defensive Actions', 'Tackles', 'Tkl'): [player.get_defensive_actions().get_tackles().get_tkl() for player in players],
        ('Defensive Actions', 'Tackles', 'TklW'): [player.get_defensive_actions().get_tackles().get_tklw() for player in players],
        ('Defensive Actions', 'Tackles', 'Def 3rd'): [player.get_defensive_actions().get_tackles().get_def_3rd() for player in players],
        ('Defensive Actions', 'Tackles', 'Mid 3rd'): [player.get_defensive_actions().get_tackles().get_mid_3rd() for player in players],
        ('Defensive Actions', 'Tackles', 'Att 3rd'): [player.get_defensive_actions().get_tackles().get_att_3rd() for player in players],

        # Challenges
        ('Defensive Actions', 'Challenges', 'Tkl'): [player.get_defensive_actions().get_challenges().get_tkl() for player in players],
        ('Defensive Actions', 'Challenges', 'Att'): [player.get_defensive_actions().get_challenges().get_att() for player in players],
        ('Defensive Actions', 'Challenges', 'Tkl%'): [player.get_defensive_actions().get_challenges().get_tkl_percentage() for player in players],
        ('Defensive Actions', 'Challenges', 'Lost'): [player.get_defensive_actions().get_challenges().get_lost() for player in players],

        # Blocks
        ('Defensive Actions', 'Blocks', 'Blocks'): [player.get_defensive_actions().get_blocks().get_blocks() for player in players],
        ('Defensive Actions', 'Blocks', 'Sh'): [player.get_defensive_actions().get_blocks().get_sh() for player in players],
        ('Defensive Actions', 'Blocks', 'Pass'): [player.get_defensive_actions().get_blocks().get_pass() for player in players],
        ('Defensive Actions', 'Blocks', 'Int'): [player.get_defensive_actions().get_blocks().get_int() for player in players],
        ('Defensive Actions', 'Blocks', 'Tkl + Int'): [player.get_defensive_actions().get_blocks().get_tkl_plus_int() for player in players],
        ('Defensive Actions', 'Blocks', 'Clr'): [player.get_defensive_actions().get_blocks().get_clr() for player in players],
        ('Defensive Actions', 'Blocks', 'Err'): [player.get_defensive_actions().get_blocks().get_err() for player in players],

        # Possession
        # Touches
        ('Possession', 'Touches', 'Touches'): [player.get_possession().get_touches().get_touches() for player in players],
        ('Possession', 'Touches', 'Def Pen'): [player.get_possession().get_touches().get_def_pen() for player in players],
        ('Possession', 'Touches', 'Def 3rd'): [player.get_possession().get_touches().get_def_3rd() for player in players],
        ('Possession', 'Touches', 'Mid 3rd'): [player.get_possession().get_touches().get_mid_3rd() for player in players],
        ('Possession', 'Touches', 'Att 3rd'): [player.get_possession().get_touches().get_att_3rd() for player in players],
        ('Possession', 'Touches', 'Att Pen'): [player.get_possession().get_touches().get_att_pen() for player in players],
        ('Possession', 'Touches', 'Live'): [player.get_possession().get_touches().get_live() for player in players],

        # Take-Ons
        ('Possession', 'Take-Ons', 'Att'): [player.get_possession().get_take_ons().get_att() for player in players],
        ('Possession', 'Take-Ons', 'Succ'): [player.get_possession().get_take_ons().get_succ() for player in players],
        ('Possession', 'Take-Ons', 'Succ%'): [player.get_possession().get_take_ons().get_succ_percentage() for player in players],
        ('Possession', 'Take-Ons', 'Tkld'): [player.get_possession().get_take_ons().get_tkld() for player in players],
        ('Possession', 'Take-Ons', 'Tkld%'): [player.get_possession().get_take_ons().get_tkld_percentage() for player in players],

        # Carries
        ('Possession', 'Carries', 'Carries'): [player.get_possession().get_carries().get_carries() for player in players],
        ('Possession', 'Carries', 'TotDist'): [player.get_possession().get_carries().get_tot_dist() for player in players],
        ('Possession', 'Carries', 'ProDist'): [player.get_possession().get_carries().get_pro_dist() for player in players],
        ('Possession', 'Carries', 'ProgC'): [player.get_possession().get_carries().get_prog_c() for player in players],
        ('Possession', 'Carries', '1/3'): [player.get_possession().get_carries().get_one_third() for player in players],
        ('Possession', 'Carries', 'CPA'): [player.get_possession().get_carries().get_cpa() for player in players],
        ('Possession', 'Carries', 'Mis'): [player.get_possession().get_carries().get_mis() for player in players],
        ('Possession', 'Carries', 'Dis'): [player.get_possession().get_carries().get_dis() for player in players],

        # Receiving
        ('Possession', 'Receiving', 'Rec'): [player.get_possession().get_receiving().get_rec() for player in players],
        ('Possession', 'Receiving', 'PrgR'): [player.get_possession().get_receiving().get_prg_r() for player in players],

        # Playing Time Details
        # Starts
        ('Playing Time Details', 'Starts', 'Starts'): [player.get_playing_time_details().get_starts().get_starts() for player in players],
        ('Playing Time Details', 'Starts', 'Mn/Start'): [player.get_playing_time_details().get_starts().get_mn_per_start() for player in players],
        ('Playing Time Details', 'Starts', 'Compl'): [player.get_playing_time_details().get_starts().get_compl() for player in players],

        # Subs
        ('Playing Time Details', 'Subs', 'Subs'): [player.get_playing_time_details().get_subs().get_subs() for player in players],
        ('Playing Time Details', 'Subs', 'Mn/Sub'): [player.get_playing_time_details().get_subs().get_mn_per_sub() for player in players],
        ('Playing Time Details', 'Subs', 'unSub'): [player.get_playing_time_details().get_subs().get_un_sub() for player in players],  # Đã sửa từ get_unsub() thành get_un_sub()

        # Team Success
        ('Playing Time Details', 'Team Success', 'PPM'): [player.get_playing_time_details().get_team_success().get_ppm() for player in players],
        ('Playing Time Details', 'Team Success', 'onG'): [player.get_playing_time_details().get_team_success().get_on_g() for player in players],
        ('Playing Time Details', 'Team Success', 'onGA'): [player.get_playing_time_details().get_team_success().get_on_ga() for player in players],

        # Team Success xG
        ('Playing Time Details', 'Team Success xG', 'onxG'): [player.get_playing_time_details().get_team_success_xg().get_on_xg() for player in players],
        ('Playing Time Details', 'Team Success xG', 'onxGA'): [player.get_playing_time_details().get_team_success_xg().get_on_xga() for player in players],

        # Miscellaneous Stats
        # Performance
        ('Miscellaneous Stats', 'Performance', 'Fls'): [player.get_miscellaneous_stats().get_performance().get_fls() for player in players],
        ('Miscellaneous Stats', 'Performance', 'Fld'): [player.get_miscellaneous_stats().get_performance().get_fld() for player in players],
        ('Miscellaneous Stats', 'Performance', 'Off'): [player.get_miscellaneous_stats().get_performance().get_off() for player in players],
        ('Miscellaneous Stats', 'Performance', 'Crs'): [player.get_miscellaneous_stats().get_performance().get_crs() for player in players],
        ('Miscellaneous Stats', 'Performance', 'OG'): [player.get_miscellaneous_stats().get_performance().get_og() for player in players],
        ('Miscellaneous Stats', 'Performance', 'Recov'): [player.get_miscellaneous_stats().get_performance().get_recov() for player in players],

        # Aerial Duels
        ('Miscellaneous Stats', 'Aerial Duels', 'Won'): [player.get_miscellaneous_stats().get_aerial_duels().get_won() for player in players],
        ('Miscellaneous Stats', 'Aerial Duels', 'Lost'): [player.get_miscellaneous_stats().get_aerial_duels().get_lost() for player in players],
        ('Miscellaneous Stats', 'Aerial Duels', 'Won%'): [player.get_miscellaneous_stats().get_aerial_duels().get_won_percentage() for player in players]

    }

    df_for_csv = pd.DataFrame(data)
    # df_for_csv.to_csv("result.csv")