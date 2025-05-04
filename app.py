from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Mock teams for demonstration
SOCCER_LEAGUES = [
    "Premier League",
    "La Liga",
    "Bundesliga",
    "Serie A",
    "Ligue 1"
]
SOCCER_TEAMS = [
    ("Real Madrid", "Barcelona"),
    ("Manchester United", "Liverpool"),
    ("Bayern Munich", "Borussia Dortmund"),
]
BASKETBALL_LEAGUES = [
    "NBA",
    "EuroLeague",
    "ACB",
    "LNB Pro A"
]
BASKETBALL_TEAMS = [
    ("Lakers", "Warriors"),
    ("Celtics", "Heat"),
    ("Bulls", "Knicks"),
]

def mock_prediction():
    # Returns a random prediction string
    outcomes = ["Home Win", "Draw", "Away Win"]
    return random.choice(outcomes)

@app.route('/', methods=['GET', 'POST'])
def home():
    predictions = None
    sport = request.form.get('sport', 'soccer') if request.method == 'POST' else 'soccer'
    # Default to first league of the sport
    if sport == 'soccer':
        leagues = SOCCER_LEAGUES
    else:
        leagues = BASKETBALL_LEAGUES
    league = request.form.get('league', leagues[0]) if request.method == 'POST' else leagues[0]
    if request.method == 'POST':
        if sport == 'soccer':
            games = SOCCER_TEAMS
        else:
            games = BASKETBALL_TEAMS
        predictions = [
            {"home": home, "away": away, "prediction": mock_prediction()} for home, away in games
        ]
    return render_template('home.html', predictions=predictions, sport=sport, league=league, leagues=leagues)

if __name__ == '__main__':
    app.run(debug=True)

