import boto3
from flask import Flask
from flask import Flask,jsonify,request,render_template

client = boto3.client("sns")

response = client.create_topic(Name="joth")
topic_arn = response["TopicArn"]

app = Flask(__name__)

def subuser(email):
    response = client.subscribe(TopicArn=topic_arn, Protocol="Email", Endpoint=email)
    subscription_arn = response["SubscriptionArn"]

@app.route('/')
def my_form():
    return render_template('site.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    subuser(processed_text)
    return "addded"


@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }

        return jsonify(data)

@app.route('/rhino', methods = ['GET'])
def ReturnRhino():
    return "rhino"




if __name__ == '__main__':
     app.run (host="0.0.0.0", port=8080)