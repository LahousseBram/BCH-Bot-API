from flask import Flask, request

app = Flask(__name__)

# Initialize global variables
high_score = 0
total_bets = 0

@app.route("/add-statistic", methods=['POST'])
def add_statistic():
    cs = request.form.get("current_streak")
    hs = int(request.form.get("high_score"))
    cb = request.form.get("current_bets")

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
    print(f"Current high score: {high_score}")
    print(f"Total bets: {total_bets}")
    print(f"Current Amount of Bets for this Bot: {cb}")
    print("--------------------------")

if __name__ == "__main__":
    app.run()
