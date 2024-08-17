from flask import Flask,render_template,jsonify

app = Flask(__name__)

INTERESTS=[
    {
        'id':1,
        'sports':'Football',
        'Amount of interest':'100%',
        'salary':'Rs.1000000'
    },
    {
        'id':2,
        'sports':'Cricket',
        'Amount of interest':'80%',
        'salary':'Rs.10000000'
    },
    {
        'id':3,
        'sports':'Kabaddi',
        'Amount of interest':'75%',
        'salary':'Rs.100000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',interests=INTERESTS)

@app.route("/interests")
def interests():
    return jsonify(INTERESTS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)