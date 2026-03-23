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

#削除機能
@app.route("/delete/<int:index>")
def delete(index):

    with open("memo.txt", "r", encoding="utf-8") as f:
        memos = f.readlines()

    del memos[index]

    with open("memo.txt", "w", encoding="utf-8") as f:
        f.writelines(memos)

    return redirect("/")

#編集機能
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):

    with open("memo.txt", "r", encoding="utf-8") as f:
        memos = f.readlines()

    if request.method == "POST":
        new_memo = request.form["memo"]
        memos[index] = new_memo + "\n"

        with open("memo.txt", "w", encoding="utf-8") as f:
            f.writelines(memos)

        return redirect("/")

    memo = memos[index]
    return render_template("edit.html", memo=memo, index=index)

if __name__ == "__main__":
    app.run(debug=True)