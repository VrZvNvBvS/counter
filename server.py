from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/', methods=['GET'])
def counter():
    if "visits" not in session:
        session["visits"] = 0
        if "count2" not in session:
            session["count2"] = 0
    else:
        session['visits'] += 1

    return render_template("index.html")


@app.route('/reset/', methods=['GET'])
def reset():
    session.clear()
    return redirect('/')


@app.route('/two/', methods=['GET'])
def add_two():
    session['count2'] += 2
    print(request.cookies['session'])
    return redirect("/")

# ENTER NUMBER for Count


@app.route('/add/', methods=['POST'])
def add():

    session["count2"] = 0
    session['count2'] = int(request.form['num'])

    return redirect("/")


@app.route('/destroy_session/', methods=['GET'])
def destroy():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
