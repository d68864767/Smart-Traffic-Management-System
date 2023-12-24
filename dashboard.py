```python
# Import necessary libraries
from google.cloud import pubsub_v1
from flask import Flask, render_template, jsonify
import os
import json
from google.cloud import datastore
from googlemaps import Client as GoogleMaps

# Set Google Cloud Pub/Sub settings
project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
topic_name = 'optimized_traffic_data'
subscription_name = 'optimized_traffic_data_subscription'

# Create a Publisher and Subscriber client
publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

# Create a Topic and Subscription
topic_path = publisher.topic_path(project_id, topic_name)
subscription_path = subscriber.subscription_path(project_id, subscription_name)

# Create a Datastore client
datastore_client = datastore.Client()

# Create a Google Maps client
gmaps = GoogleMaps(os.getenv('GOOGLE_MAPS_API_KEY'))

# Create a Flask app
app = Flask(__name__)

# Callback function to process the messages
def callback(message):
    print('Received message: {}'.format(message))
    data = json.loads(message.data)
    store_data(data)
    message.ack()

# Function to store the data in Datastore
def store_data(data):
    # Create a new entity
    entity = datastore.Entity(key=datastore_client.key('TrafficData'))
    entity.update(data)

    # Save the entity
    datastore_client.put(entity)

# Subscribe to the topic
subscriber.subscribe(subscription_path, callback=callback)

# Route to render the dashboard
@app.route('/')
def dashboard():
    # Query the latest traffic data
    query = datastore_client.query(kind='TrafficData')
    query.order = ['-timestamp']
    results = list(query.fetch(limit=10))

    # Get the geolocation of the traffic data
    geolocations = [gmaps.geocode(result['location']) for result in results]

    # Render the dashboard template
    return render_template('dashboard.html', data=results, geolocations=geolocations)

# Route to get the latest traffic data
@app.route('/data')
def data():
    # Query the latest traffic data
    query = datastore_client.query(kind='TrafficData')
    query.order = ['-timestamp']
    results = list(query.fetch(limit=10))

    # Return the data as JSON
    return jsonify(results)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
```
