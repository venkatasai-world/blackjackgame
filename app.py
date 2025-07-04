from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "venkatasai"

cards = [1,2,3,4,5,6,7,8,9,10,10,10,11]

@app.route("/", methods=["GET", "POST"])
def blackjack():
    if request.method == "POST":
        if "start" in request.form:
            session["your_cards"] = [random.choice(cards), random.choice(cards)]
            session["comp_cards"] = [random.choice(cards), random.choice(cards)]
            session["game_over"] = False
            return redirect("/")
        
        elif "hit" in request.form:
            session["your_cards"].append(random.choice(cards))
            session["comp_cards"].append(random.choice(cards))
        
        elif "stand" in request.form:
            session["game_over"] = True

    your_total = sum(session.get("your_cards", []))
    comp_total = sum(session.get("comp_cards", []))

    result = ""
    if session.get("game_over"):
        if your_total > 21:
            result = "❌ You busted! Computer wins."
        elif comp_total > 21 or your_total > comp_total:
            result = "🎉 You won!"
        elif your_total == comp_total:
            result = "🤝 It's a tie!"
        else:
            result = "💻 Computer wins!"

    return render_template("index.html",
                           your_cards=session.get("your_cards", []),
                           comp_cards=session.get("comp_cards", []),
                           your_total=your_total,
                           comp_total=comp_total,
                           result=result,
                           game_over=session.get("game_over", False))

if __name__ == "__main__":
    app.run(debug=True)
