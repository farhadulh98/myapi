import flask
from flask import Flask, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"]=True


users = [
    {
      "userId": 1,
      "firstName": "Krish",
      "lastName": "Lee",
      "phoneNumber": 123456,
      "emailAddress": "krish.lee@learningcontainer.com"
    },
    {
      "userId": 2,
      "firstName": "racks",
      "lastName": "jacson",
      "phoneNumber": 123456,
      "emailAddress": "racks.jacson@learningcontainer.com"
    },
    {
      "userId": 3,
      "firstName": "denial",
      "lastName": "roast",
      "phoneNumber": 33333333,
      "emailAddress": "denial.roast@learningcontainer.com"
    },
    {
      "userId": 4,
      "firstName": "devid",
      "lastName": "neo",
      "phoneNumber": 222222222,
      "emailAddress": "devid.neo@learningcontainer.com"
    },
    {
      "userId": 5,
      "firstName": "jone",
      "lastName": "mac",
      "phoneNumber": 111111111,
      "emailAddress": "jone.mac@learningcontainer.com"
    }

        ]


@app.route('/home')
def home():
    return "<h1> Welcome to my first API</h1>"


@app.route('/home/user', methods=['GET'])
def get():
    return jsonify({'USERS': users})


@app.route('/user/<int:userId>', methods=["GET"])
def get_user(userId):
    return jsonify('USER with ID', users[userId])


#@app.route('/user/<int:userId>', methods=['GET'])
#def get_user(phoneNumber):
#    return jsonify('USER', users[phoneNumber])


if __name__ == "__main__":
    app.run(debug=True)