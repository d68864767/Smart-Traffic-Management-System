```python
# Import necessary libraries
from google.cloud import pubsub_v1
from google.cloud import dataflow
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

# Create a Dataflow client
dataflow_client = dataflow.DataflowClient()

# Callback function to process the messages
def callback(message):
    print('Received message: {}'.format(message))
    data = json.loads(message.data)
    process_data(data)
    message.ack()

# Function to process the data using Dataflow
def process_data(data):
    # Define the pipeline
    p = dataflow.Pipeline()

    # Create a PCollection from the data
    pcoll = p | dataflow.Create([data])

    # Apply transformations to the PCollection
    processed_data = pcoll | 'Process Data' >> dataflow.Map(lambda x: {
        'timestamp': x['timestamp'],
        'location': x['location'],
        'speed': x['speed'],
        'volume': x['volume'],
        'occupancy': x['occupancy'],
        'quality': x['quality']
    })

    # Write the processed data to a new topic
    processed_data | 'Write to PubSub' >> dataflow.io.WriteToPubSub(topic='processed_traffic_data')

    # Run the pipeline
    p.run()

# Subscribe to the topic
subscriber.subscribe(subscription_path, callback=callback)

print('Listening for messages on {}'.format(subscription_path))
```
