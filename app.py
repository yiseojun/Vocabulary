<<<<<<< Updated upstream
from flask import Flask, render_template
import Qlist

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template("index.html")

@app.route("/단어장")
def voca() :
    return render_template("voca.html")

@app.route("/단어시험")
def exam() :
    return render_template("exam.html")

@app.route("/단어목록")
def qlist() :
    examlist = Qlist.scanFolder()
    return render_template("qlist.html", list = examlist)

@app.route("/단어목록/<exam>")
def wlist(exam) :
    wordlist = Qlist.scanFile(exam)
    return render_template("elist.html", list = wordlist)

if __name__ == "__main__" :
=======
from flask import Flask, render_template
import Qlist

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template("index.html")

@app.route("/단어장")
def voca() :
    return render_template("voca.html")

@app.route("/단어시험")
def exam() :
    return render_template("exam.html")

@app.route("/단어목록")
def qlist() :
    examlist = Qlist.scanFolder()
    return render_template("qlist.html", list = examlist)

@app.route("/단어목록/<exam>")
def wlist(exam) :
    wordlist = Qlist.scanFile(exam)
    return render_template("elist.html", list = wordlist)

@app.route("/단어목록/<exam>/<number>")
def start_voca(exam, number) :
    return render_template("voca.html", path=f"/static/data/voca_list/{ exam }/{ number }.txt")

if __name__ == "__main__" :
>>>>>>> Stashed changes
    app.run(debug=True)