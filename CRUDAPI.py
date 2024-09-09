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

@app.route('/get-user',methods=["GET"])
def get_user():
    return USERS
    

@app.route('/get-user/<int:user_id>',methods=["GET"])
def get_user1(user_id):
    for user in USERS:
        if user['id']==user_id:
            return user
        
    return {"ERROR":"BOOK NOT FOUND"} 


@app.route("/create-user",methods=["POST"])
def create_user():
    new_user={'id': len(USERS)+1, 'name':request.json['name'],'course': request.json['course']}
    USERS.append(new_user)
    return new_user

@app.route("/update-user/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    for user in USERS :
        if user['id']==user_id:
            user['name']=request.json['name']
            user['course']=request.json['course']
            return user
    return {'error':'NOT FOUND'}


@app.route("/delete-user/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
    for user in USERS :
        if user['id']==user_id:
            USERS.remove(user)
            return {"DATA DELETED SUCCESSFULLY"}
    return {"NOTHING TO BE DELETED REGARDING THE DATA GIVEN"}

if __name__ == "__main__" :
    app.run(debug=True)