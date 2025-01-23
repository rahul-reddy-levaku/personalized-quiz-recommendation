Project: Quiz Data Analysis

Overview

This project will fetch, analyze, and visualize quiz-related data from two API endpoints, one for the current quiz data and another for historical data. It provides insight into quiz trends, user performance, and historical comparisons. The purpose is to demonstrate how to deal with API data, process it with Python, and create meaningful visualizations to guide decisions or further analysis.

Features

Fetch quiz data from APIs with error handling.

Analyze quiz data to calculate average scores and trends.

Visualize quiz trends using line plots for comparison between current and historical data.

Modular structure for easy expansion or updates.

Setup Instructions

Prerequisites

Python 3.8 or higher: Make sure you have Python installed. You can do that by running:

python --version

Required Libraries: Install the required libraries using pip:

pip install requests pandas matplotlib

API Endpoints: Replace the sample URLs in the script with the actual API endpoints.

Steps to Run

Clone or download the repository to your local machine.

Go to the project directory.

Run the script by executing the following command:

python main.py

Follow the instructions printed and check out the visualizations.

Project Approach

Data Fetching

The fetch_data function takes care of the communication between the APIs. It has a good error-handling mechanism that takes care of timeouts, connection errors, and bad HTTP responses.

Data Analysis

Goal: Obtain meaningful insights from both current and historical quiz data.

Implementation:

Computes average quiz scores (if score column exists).

Prepares the data for visualization.

Visualization

Library Used: matplotlib

Graph Type: Line plots to depict quiz counts over time.

Details: The visualize_data function creates plots that compare the current and historical trends of quizzes, with proper labeling and formatting to make it easily readable.

Modular Design

The project is designed with reusable functions to maintain clarity and update it easily. Each function executes only a single task, such as fetching data, analyzing data, or visualizing data.

Future Enhancements

Provide support for additional data visualizations, such as category-wise performance through a bar chart.

Implement data preprocessing steps to address missing or inconsistent data.

Expand the analysis to offer user-specific trends or performance tracking.

Schedule the automated process of fetching and visualizing the data.
Troubleshooting
Connection Problems: Your internet connection is unstable.

Invalid API URLs : Check the validity of the supplied API endpoints

Missing Libraries: Reinstall Libraries using pip command listed on the prerequisites section.
