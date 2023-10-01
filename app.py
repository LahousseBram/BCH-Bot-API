from flask import Flask, request

app = Flask(__name__)

high_score = 0
total_bets = 0

@app.route("/add-statistic", methods=['POST'])
def add_statistic():
    cs = request.args.get("current_streak")
    hs = int(request.args.get("high_score"))
    cb = request.args.get("current_bets")
    global high_score, total_bets

    total_bets += 1
    
    if hs > high_score:
        high_score = hs

    log_info(cs, hs, cb)

    return "result logged"

def log_info(cs, hs, cb):
    print("--------------------------")
    print(f"Bot made new bet")
    print(f"Its streak: {cs}")
    print(f"Current high score: {hs}")
    print(f"Total bets: {total_bets}")
    print(f"Current Amount of Bets for this Bot: {cb}")
    print("--------------------------")

app.run()