# Smart Traffic Management System

This project is a dynamic traffic management system that uses Google Cloud’s AI and machine learning services to analyze traffic data in real-time and optimize traffic flow in urban areas to reduce congestion and travel time.

## Core Features

1. Real-Time Traffic Data Processing
2. Predictive Traffic Modeling
3. Traffic Optimization Recommendations
4. Interactive Dashboard for Traffic Monitoring
5. Automated Alert System

## Technologies Used

- Google Cloud Pub/Sub for real-time data ingestion.
- Google Cloud Dataflow for data processing.
- Google Cloud AI Platform for machine learning models.
- Google App Engine and Google Maps API for the dashboard.

## Project Structure

- `pubsub_ingestion.py`: This script is responsible for ingesting real-time traffic data from various sources like cameras, sensors, and GPS data using Google Cloud Pub/Sub.
- `dataflow_processing.py`: This script analyzes the ingested data using Google Cloud Dataflow to identify traffic patterns, congestion points, and potential causes of delays.
- `ai_model.py`: This script uses Google Cloud AI Platform to develop machine learning models that predict traffic conditions based on historical data and real-time inputs.
- `optimization_algorithm.py`: This script creates algorithms to recommend traffic signal changes, route diversions, or other interventions to optimize traffic flow.
- `dashboard.py`: This script develops a web-based dashboard using Google App Engine to visualize real-time traffic conditions and the impact of optimization strategies.
- `alert_system.py`: This script designs a notification system that alerts city traffic departments and the public about critical traffic updates and advisories.
- `main.py`: This is the main script that runs the entire system.
- `test.py`: This script is used for testing the system.
- `deployment_instructions.md`: This file contains the steps for deploying the system on Google Cloud Platform.

## How to Run

1. Clone the repository.
2. Install the necessary dependencies.
3. Set the necessary environment variables.
4. Run `main.py`.

## Testing

Run `test.py` to test the system.

## Deployment

Follow the instructions in `deployment_instructions.md` to deploy the system on Google Cloud Platform.

## License

This project is licensed under the MIT License.

