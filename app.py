from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        memo = request.form["memo"]

        with open("memo.txt", "a", encoding="utf-8") as f:
            f.write(memo + "\n")

        return redirect("/")

    memos = []
    with open("memo.txt", "r", encoding="utf-8") as f:
        memos = f.readlines()

    return render_template("index.html", memos=memos)

@app.route("/delete/<int:index>")
def delete(index):

    with open("memo.txt", "r", encoding="utf-8") as f:
        memos = f.readlines()

    del memos[index]

    with open("memo.txt", "w", encoding="utf-8") as f:
        f.writelines(memos)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)