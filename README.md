# 📊 Univariate Exploratory Data Analysis of Mobile App Usage Behavior

---

## 1. Project Overview
This project implements **Univariate Exploratory Data Analysis (EDA)** to analyze mobile app usage behavior using graphical visualization techniques.  
The application is developed using **Streamlit**, providing an interactive and user-friendly interface to study individual numerical variables.

---

## 2. Problem Statement
Raw mobile app usage data is difficult to interpret without proper visualization.  
There is a need to analyze individual usage metrics to understand their distribution, spread, and patterns using graphical methods.

---

## 3. Objectives of the Project
The main objectives of this project are:
- To perform **univariate exploratory data analysis**
- To visualize data using graphical techniques
- To study distribution, central tendency, and variability
- To identify potential outliers in mobile usage data
- To build an interactive and user-friendly EDA application

---

## 4. Dataset Description
- The dataset used is **synthetic but realistic**
- Created purely for academic analysis
- Contains **only numerical attributes**
- Represents daily mobile app usage behavior

### Dataset Columns:
- `daily_screen_time_minutes`
- `app_opens_per_day`
- `notifications_received`
- `time_spent_on_social_apps`
- `time_spent_on_educational_apps`

Dataset location:
data/mobile_app_usage.csv


---

## 5. Methodology
This project strictly follows **Univariate EDA**, where one variable is analyzed at a time.

### Steps followed:
1. Load dataset (default or uploaded CSV)
2. Select a single numerical column
3. Compute summary statistics
4. Generate graphical visualizations
5. Interpret results

---

## 6. Graphical Techniques Used
The following univariate graphical methods are applied:

- **Histogram**
  - Displays frequency distribution of data
- **Box Plot**
  - Shows data spread and potential outliers
- **Density Plot**
  - Represents smooth distribution of values

Note: No multivariate or correlation analysis is performed.

---

## 7. Application Features
- Interactive Streamlit user interface
- Sidebar-based dataset and column selection
- Automatic statistical summary
- Dynamic plot generation
- One-command execution

---

## 8. Tools and Technologies Used
- **Python** – Programming language
- **Streamlit** – Frontend and backend integration
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Git & GitHub** – Version control and hosting

---

## 9. Project File Structure
```
univariate-eda-mobile-usage/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│ └── mobile_app_usage.csv
│
└── images/
└── screenshots/
```


---

## 10. How to Run the Project

### Step 1: Install dependencies
pip install -r requirements.txt


### Step 2: Run the Streamlit application
streamlit run app.py


---

## 11. Key Observations
- The histogram helps understand frequency distribution
- The box plot highlights data spread and outliers
- The density plot shows distribution shape
- Summary statistics provide insights into central tendency and variability
