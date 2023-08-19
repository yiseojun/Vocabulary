from flask import Flask, render_template
from Qlist import *

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template("index.html")

@app.route("/단어목록")
def qlist() :
    examlist = scanFolder("단어목록").scan()
    return render_template("qlist.html", list = examlist, adress = "/")

@app.route("/단어목록/<exam>")
def wlist(exam) :
    wordlist = scanFile("단어목록").scan(exam)
    return render_template("elist.html", list = wordlist)

@app.route("/단어목록/<exam>/<number>")
def start_voca(exam, number) :
    return render_template("voca.html", path=f"/static/data/voca_list/{ exam }/{ number }.txt", adress = f"/단어목록/{ exam }")

@app.route("/단어시험")
def exam() :
    examlist = scanFolder("단어시험").scan()
    return render_template("qlist.html", list = examlist, adress = "/")

@app.route("/단어시험/<exam>")
def examList(exam) :
    examlist = scanFile("단어시험").scan(exam)
    return render_template("qlist.html", list = examlist, adress = "/단어시험")

@app.route("/단어시험/<exam>/<number>")
def start_exam(exam, number) :
    return render_template("exam.html", path = f"/static/data/voca_list/{ exam }/{ number }.txt", adress = f"/단어시험/{ exam }")

@app.route("/빈출단어")
def frequent() :
    return render_template("WordBoard.html", table = makeTable.makeHTML())    

if __name__ == "__main__" :
    app.run(host='0.0.0.0', port=5000, debug=True)