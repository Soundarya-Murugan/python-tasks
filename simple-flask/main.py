


from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/voting/eligibility")
def get_voting_eligibility():

     age     = int(request.values.get("age"))

     content = ""
     if age > 18:
         content = "You are eligible to vote"
     else:
         content = "You are not eligible to vote"

     return content
 
 
if __name__ == '__main__':
    app.run(
        debug=True
    )