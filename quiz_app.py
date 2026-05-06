from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "final_quiz_key"

questions = [
    {"question": "Capital of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "answer": "Delhi"},
    {"question": "Who developed Python?", "options": ["Elon Musk", "Guido van Rossum", "Bill Gates", "Mark Zuckerberg"], "answer": "Guido van Rossum"},
    {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Frontend language?", "options": ["HTML", "Python", "Java", "SQL"], "answer": "HTML"},
    {"question": "CSS is used for?", "options": ["Logic", "Styling", "Database", "AI"], "answer": "Styling"},
    {"question": "Database example?", "options": ["MySQL", "HTML", "CSS", "Python"], "answer": "MySQL"},
    {"question": "Which is NOT a language?", "options": ["Python", "Java", "HTML", "C++"], "answer": "HTML"},
    {"question": "CPU stands for?", "options": ["Central Processing Unit", "Control Unit", "Central Print Unit", "None"], "answer": "Central Processing Unit"},
    {"question": "5 + 3 = ?", "options": ["8", "7", "6", "9"], "answer": "8"},
    {"question": "JS is used for?", "options": ["Styling", "Logic", "Structure", "None"], "answer": "Logic"},
    {"question": "Python keyword for function?", "options": ["def", "fun", "define", "function"], "answer": "def"},
    {"question": "HTML stands for?", "options": ["Hyper Text Markup Language", "High Text Machine Language", "Hyperlinks Text", "None"], "answer": "Hyper Text Markup Language"}
]

random.shuffle(questions)


@app.route("/", methods=["GET", "POST"])
def quiz():
    if "i" not in session:
        session["i"] = 0
        session["score"] = 0
        session["answers"] = []

    i = session["i"]

    if i >= len(questions):
        return redirect("/result")

    if request.method == "POST":
        selected = request.form.get("option")
        correct = questions[i]["answer"]

        session["answers"].append({
            "q": questions[i]["question"],
            "selected": selected,
            "correct": correct
        })

        if selected == correct:
            session["score"] += 1

        session["i"] = i + 1
        return redirect("/")

    progress = int((i / len(questions)) * 100)

    return render_template("index.html",
                           q=questions[i],
                           num=i+1,
                           total=len(questions),
                           progress=progress)


@app.route("/result")
def result():
    score = session.get("score", 0)
    answers = session.get("answers", [])
    total = len(questions)

    session.clear()

    return render_template("result.html",
                           score=score,
                           total=total,
                           answers=answers)


if __name__ == "__main__":
    app.run(debug=True)
    
    


    
    
    
    
    
    
    
    