import boto3
import requests

client = boto3.client("sns")

response = client.create_topic(Name="joth")
topic_arn = response["TopicArn"]


joke = requests.get("https://v2.jokeapi.dev/joke/any")
if (joke.json()["type"] == "twopart"):
    jokecontents = joke.json()["setup"] + " " + joke.json()["delivery"]
else:
    jokecontents = joke.json()["joke"]


# Publish to topic
client.publish(TopicArn=topic_arn,
            Message=jokecontents,
            Subject="Ten second Joke")




# List all subscriptions
response = client.list_subscriptions()
subscriptions = response["Subscriptions"]
print ( subscriptions )



topics = client.list_topics().get('Topics')

for topic in topics:
    subscriptions = client.list_subscriptions_by_topic(TopicArn=topic.get('TopicArn')).get('Subscriptions')
    for subscription in subscriptions:
        print(subscription.get('SubscriptionArn'))
        print(subscription.get('Endpoint'))