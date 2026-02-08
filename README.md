📊 Univariate Exploratory Data Analysis of Mobile App Usage Behavior
```
📌 Project Overview

This project focuses on Univariate Exploratory Data Analysis (EDA) to understand mobile app usage behavior using graphical visualization techniques. The application is built using Streamlit, providing an interactive and user-friendly interface to explore the distribution, spread, and patterns of individual usage metrics.

The project strictly follows univariate analysis concepts, making it fully aligned with the Exploratory Data Analysis and Visualization syllabus.

❓ Problem Statement

With the increasing use of smartphones, understanding mobile app usage patterns is important to analyze user behavior. Raw usage data alone is difficult to interpret without proper visualization. This project aims to analyze mobile app usage data using univariate graphical methods to extract meaningful insights from individual variables.

🎯 Objective of the Project

To perform univariate exploratory data analysis on mobile app usage data

To visualize data distribution using graphical techniques

To identify central tendency, spread, and potential outliers

To provide an interactive and easy-to-use analysis interface

To demonstrate practical application of EDA concepts

📂 Dataset Description

The dataset used in this project is a synthetic but realistic mobile app usage dataset, created for academic analysis purposes.

Dataset Characteristics:

Contains only numerical variables

Represents daily mobile usage behavior

Free from real user data (privacy-safe)

Columns Used:

daily_screen_time_minutes

app_opens_per_day

notifications_received

time_spent_on_social_apps

time_spent_on_educational_apps

The dataset is stored in the data folder as a CSV file.

🧪 Methodology

This project applies Univariate Exploratory Data Analysis, where one variable is analyzed at a time.

The following steps are performed:

Load dataset (default or user-uploaded CSV)

Select a single numerical variable

Compute summary statistics

Visualize data using graphical methods

Interpret distribution and patterns

Graphical Techniques Used:

Histogram – to observe frequency distribution

Box Plot – to analyze spread and detect outliers

Density Plot – to understand data distribution shape

All analysis is strictly univariate, without correlation or multivariate methods.

🖥️ Application Features

Interactive Streamlit UI

CSV upload support

Dropdown selection for numerical columns

Dataset preview

Automatic statistical summary

Dynamic visualization updates

Single-command execution

🛠️ Tools and Technologies Used

Python – Programming language

Streamlit – Frontend and backend integration

Pandas – Data handling and analysis

NumPy – Numerical operations

Matplotlib – Data visualization

Git & GitHub – Version control and project hosting

📁 Project File Structure
univariate-eda-mobile-usage/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── mobile_app_usage.csv
│
└── images/
    └── screenshots/

▶️ How to Run the Project
Step 1: Install Dependencies
pip install -r requirements.txt

Step 2: Run the Application
streamlit run app.py


The application will open automatically in your browser.

🔍 Key Observations and Insights

The histogram helps visualize how mobile usage values are distributed

The box plot highlights data spread and identifies potential outliers```

The density plot shows the overall shape and symmetry of the data

Summary statistics provide clear insights into central tendency and variability

These observations help in understanding individual mobile usage patterns effectively.
