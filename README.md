# Road Accident Prediction and Prevention AI System

This project provides a multi-agent AI-based solution to predict, prevent, and respond to road accidents. By analyzing historical road crash data, traffic patterns, and environmental conditions, this solution identifies crash hotspots, generates executive briefs, suggests preventative measures, and proposes policy guidelines to improve road safety.

## Key Features

- **Crash Hotspot Identification**: Predict high-risk areas for road accidents using machine learning and geospatial data.
- **Executive Brief Generation**: Automatically generate summaries of key findings, insights, and recommendations.
- **Preventative Measure Suggestions**: Recommend infrastructure changes and traffic management measures to prevent future accidents.
- **Policy Guideline Recommendations**: Provide public policy solutions like improved signage, traffic signal timing, and public awareness campaigns.
- **Geospatial Visualization**: Visualize crash hotspots on an interactive map using the `folium` library.

## Project Structure

```plaintext
.
├── data/                           # Data directory with provided datasets
│   ├── ACCIDENT.csv
│   ├── ATMOSPHERIC_COND.csv
│   ├── ROAD_SURFACE_COND.csv
│   ├── VEHICLE.csv
│   ├── Traffic_Count_Locations.csv
│   ├── VICTORIAN_ROAD_CRASH_DATA.geojson
│   └── other_files.csv
├── src/                            # Source code directory
│   ├── data_preprocessing.py       # Script for cleaning and preprocessing the data
│   ├── hotspot_model.py            # Script for predicting crash hotspots
│   ├── executive_brief.py          # Script to generate executive briefs
│   ├── preventative_measures.py    # Script to suggest preventative measures
│   ├── policy_recommendations.py   # Script to recommend policy guidelines
├── notebooks/                      # Jupyter notebooks for sample use cases
│   └── sample_use_case.ipynb        # Notebook demonstrating a use case
├── app.py                          # Flask app to serve the models via APIs
├── crash_hotspots_map.html          # Interactive map of predicted crash hotspots
├── README.md                       # This file
└── requirements.txt                # Python dependencies file

# Urban Planning and Accident Prediction

This repository contains the code for predicting road accidents and urban growth using AI. It leverages historical data and machine learning models to provide insights for city planning and road safety.

## Project Structure:
- `src/`: Source code for data loading, preprocessing, model training, and API deployment.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model experimentation.

## How to Run:
1. Install dependencies: `pip install -r requirements.txt`
2. Run the dashboard: `python src/visualizations/dashboard.py`
3. API for predictions: `python src/api/prediction_api.py`

## Data Sources:
- Victorian Road Crash Data
- Planning Permit Data
- Traffic Volume and Environmental Data