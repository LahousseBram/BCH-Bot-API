from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # You should use a secure secret key in a production environment

if 'high_score' not in session:
    session['high_score'] = 0
if 'total_bets' not in session:
    session['total_bets'] = 0

@app.route("/add-statistic", methods=['POST'])
def add_statistic():
    cs = request.form.get("current_streak")
    hs = int(request.form.get("high_score"))
    cb = request.form.get("current_bets")

    session['total_bets'] += 1
    
    if hs > session['high_score']:
        session['high_score'] = hs

    log_info(cs, hs, cb)

    return "result logged"

def log_info(cs, hs, cb):
    print("--------------------------")
    print(f"Bot made new bet")
    print(f"Its streak: {cs}")
    print(f"Current high score: {session['high_score']}")
    print(f"Total bets: {session['total_bets']}")
    print(f"Current Amount of Bets for this Bot: {cb}")
    print("--------------------------")

if __name__ == "__main__":
    app.run()