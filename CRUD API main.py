from flask import Flask, request, jsonify

app=Flask(__name__)

USERS=[
    {
        "id":1,
        "name":"Dhanush",
        "course":"ECE"
    },
    {
       "id":2,
        "name":"Dhanush B",
        "course":"ECE"
    } 
    
]
@app.route("/get-user/<int:user_id>",methods=["GET"])
def get_user(user_id):
    for user in USERS:
        if user['id']==user_id:
            return user
        
        return {'error':'Nothing found'}


@app.route("/create-user",methods=["POST"])
def create_user():
    data=request.get_json()

    return jsonify(data) , 201


if __name__ == "__main__" :
    app.run(debug=True)
