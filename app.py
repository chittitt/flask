from flask import Flask, render_template, request

app = Flask(__name__)

games = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        # ユーザーが選択したものに対して勝敗を決定する処理を追加
        player_choice = request.form["choice"]
        computer_choice = "rock" # 仮の値
        result = "win" # 仮の値
        game = {"date": "2023/02/28", "player1": "Player", "player2": "Computer", "winner": "Player"} # 仮の値
        games.append(game)
        return render_template("game.html", player_choice=player_choice, computer_choice=computer_choice, result=result)
    else:
        return render_template("game.html")

@app.route("/result")
def result():
    return render_template("result.html", games=games)

if __name__ == "__main__":
    app.run(debug=True)




