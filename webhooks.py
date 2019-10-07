from flask import Flask,request
app = Flask(__name__)


# Receive webhooks from TeleCMI platform when call receive or make
@app.route("/you-have-call",methods=['POST'])
def hello():
    # Received JSON CDR from TeleCMI Platform
    cdr = request.get_json()
    print(cdr)

    print(cdr['type'])
    print(cdr['time'])
    print(cdr['direction'])
    return "got it"



if __name__ == "__main__":
    app.run(debug=True, port=5000)

