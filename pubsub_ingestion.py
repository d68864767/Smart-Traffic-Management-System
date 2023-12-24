```python
# Import necessary libraries
from google.cloud import pubsub_v1
import os
import json

# Set Google Cloud Pub/Sub settings
project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
topic_name = 'traffic_data_topic'
subscription_name = 'traffic_data_subscription'

# Create a Publisher and Subscriber client
publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

# Create a Topic and Subscription
topic_path = publisher.topic_path(project_id, topic_name)
subscription_path = subscriber.subscription_path(project_id, subscription_name)

# Create the topic if it doesn't exist
try:
    publisher.get_topic(topic_path)
except:
    publisher.create_topic(topic_path)

# Create the subscription if it doesn't exist
try:
    subscriber.get_subscription(subscription_path)
except:
    subscriber.create_subscription(subscription_path, topic_path)

# Callback function to process the messages
def callback(message):
    print('Received message: {}'.format(message))
    data = json.loads(message.data)
    # TODO: Process the data
    message.ack()

# Subscribe to the topic
subscriber.subscribe(subscription_path, callback=callback)

print('Listening for messages on {}'.format(subscription_path))
```
