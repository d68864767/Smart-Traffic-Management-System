```python
# Import necessary libraries
from google.cloud import pubsub_v1
import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set Google Cloud Pub/Sub settings
project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
topic_name = 'processed_traffic_data'
subscription_name = 'processed_traffic_data_subscription'

# Create a Publisher and Subscriber client
publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

# Create a Topic and Subscription
topic_path = publisher.topic_path(project_id, topic_name)
subscription_path = subscriber.subscription_path(project_id, subscription_name)

# Email settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_user = os.getenv('EMAIL_USER')
email_password = os.getenv('EMAIL_PASSWORD')

# Callback function to process the messages
def callback(message):
    print('Received message: {}'.format(message))
    data = json.loads(message.data)
    send_alert(data)
    message.ack()

# Function to send an email alert
def send_alert(data):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = ', '.join(data['recipients'])
    msg['Subject'] = 'Traffic Alert'

    # Create the email body
    body = 'Dear User,\n\n'
    body += 'There is a traffic alert for your area.\n\n'
    body += 'Location: {}\n'.format(data['location'])
    body += 'Volume: {}\n'.format(data['volume'])
    body += 'Speed: {}\n'.format(data['speed'])
    body += 'Occupancy: {}\n'.format(data['occupancy'])
    body += 'Quality: {}\n'.format(data['quality'])
    body += '\nBest,\nSmart Traffic Management System'

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_user, email_password)
    text = msg.as_string()
    server.sendmail(email_user, data['recipients'], text)
    server.quit()

# Subscribe to the topic
subscriber.subscribe(subscription_path, callback=callback)

print('Listening for messages on {}'.format(subscription_path))
```
