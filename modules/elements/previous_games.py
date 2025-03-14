from datetime import datetime
from modules.fetch_nhl_api import get_logo

__all__ = ['display_game_result', 'get_previous_games','display_latest_game_result']

def display_game_result(game):
    opponent_logo = get_logo(game['opponent_abr'])
    game_disp = f"""
                {game['game_venue']}
                <a href="javascript:void(0);" class="team-link">
                <img src="{opponent_logo}" style="width: 85px">
                </a>
                {game['home_score']} -  {game['away_score']} ({game['result']})
                <a href={game["recap_URL"]} target="_blank" rel="noopener noreferrer" class="recap-link">                
                <span class="material-symbols-outlined">
                    open_in_new
                </span></a> <br>
                """

    return game_disp

def display_latest_game_result(game):
    opponent_logo = get_logo(game['opponent_abr'])
    game_disp = f"""
                {game['game_venue']}
                <a href="javascript:void(0);" class="team-link">
                <img src="{opponent_logo}" style="width: 85px">
                </a>
                <div class="spoiler-wrapper">
                    <button class="toggle-spoiler">
                        <span class="material-symbols-outlined">
                            visibility
                        </span>
                    </button>  
                    <span class="hide-spoiler"> {game['home_score']} -  {game['away_score']} ({game['result']}) </span>
                </div>
                <a href={game["recap_URL"]} target="_blank" rel="noopener noreferrer" class="recap-link">                
                <span class="material-symbols-outlined">
                    open_in_new
                </span></a> <br>
                """

    return game_disp

def get_previous_games(games_by_date,nr_games=3):
    # Get the current date and time
    current_date = datetime.now()
    current_date = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    previous_games = sorted([game for game in games_by_date if game['game_date'] < current_date], key= lambda x: x['game_date'])
    last_games = previous_games[-nr_games:] if len(previous_games) >= nr_games else previous_games
    last_game_disp = [display_latest_game_result(last_games[-1])]  # First game uses different function
    last_game_disp += [display_game_result(game) for game in reversed(last_games[:-1])]  # The rest use the normal function

    return last_game_disp