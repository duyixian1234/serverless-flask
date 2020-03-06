from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(success=True,msg='',code=0,data="Hello,serverless")

if __name__ == "__main__":
    app.run()