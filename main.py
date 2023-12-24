```python
# Import necessary libraries
import os
import threading
import pubsub_ingestion
import dataflow_processing
import ai_model
import optimization_algorithm
import dashboard
import alert_system

# Set Google Cloud Pub/Sub settings
project_id = os.getenv('GOOGLE_CLOUD_PROJECT')

# Topics and Subscriptions
topics_subscriptions = {
    'traffic_data_topic': 'traffic_data_subscription',
    'processed_traffic_data': 'processed_traffic_data_subscription',
    'optimized_traffic_data': 'optimized_traffic_data_subscription'
}

# Create a Publisher and Subscriber client
publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

# Create Topics and Subscriptions
for topic, subscription in topics_subscriptions.items():
    topic_path = publisher.topic_path(project_id, topic)
    subscription_path = subscriber.subscription_path(project_id, subscription)

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

# Start the Pub/Sub ingestion
threading.Thread(target=pubsub_ingestion.start).start()

# Start the Dataflow processing
threading.Thread(target=dataflow_processing.start).start()

# Start the AI model training and prediction
threading.Thread(target=ai_model.start).start()

# Start the optimization algorithm
threading.Thread(target=optimization_algorithm.start).start()

# Start the dashboard
threading.Thread(target=dashboard.start).start()

# Start the alert system
threading.Thread(target=alert_system.start).start()
```
