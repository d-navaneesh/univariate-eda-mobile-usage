# 📊 Univariate Exploratory Data Analysis of Mobile App Usage Behavior

## 📖 Project Overview

This project implements a **Streamlit-based web application** for performing **Univariate Exploratory Data Analysis (EDA)** on mobile app usage behavior data. The application provides an interactive interface to analyze individual numerical variables through statistical summaries and visualizations.

---

## 🎯 Problem Statement

Understanding mobile app usage patterns is crucial for app developers, UX designers, and researchers. However, analyzing raw usage data can be complex and time-consuming. This project addresses the need for a simple, interactive tool that allows users to:

- Quickly explore individual variables in mobile usage datasets
- Understand data distribution patterns
- Identify outliers and anomalies
- Generate statistical summaries without writing code

---

## 🎓 Objective

The primary objective of this project is to:

1. **Develop an interactive web application** using Streamlit for univariate data analysis
2. **Implement statistical analysis** including measures of central tendency, dispersion, and distribution shape
3. **Provide visual representations** through histograms, box plots, and density plots
4. **Enable data flexibility** by supporting both default and custom CSV datasets
5. **Deliver actionable insights** through automated outlier detection and distribution analysis

---

## 📊 Dataset Description

### Default Dataset: `mobile_app_usage.csv`

The dataset contains **40 observations** of mobile app usage behavior with the following **10 numerical variables**:

| Column Name | Description | Unit |
|------------|-------------|------|
| `user_id` | Unique identifier for each user | Integer |
| `age` | Age of the user | Years |
| `daily_screen_time_hours` | Average daily screen time | Hours |
| `app_opens_per_day` | Number of times apps are opened daily | Count |
| `notifications_received` | Daily notifications received | Count |
| `battery_drain_percent` | Average daily battery consumption | Percentage |
| `data_usage_mb` | Daily mobile data usage | Megabytes |
| `session_duration_minutes` | Average app session duration | Minutes |
| `apps_installed` | Total number of installed apps | Count |
| `weekly_usage_hours` | Total weekly screen time | Hours |

**Data Characteristics:**
- **Size:** 40 rows × 10 columns
- **Type:** All numerical (continuous and discrete)
- **Source:** Synthetic realistic data
- **Quality:** No missing values

---

## 🔬 Methodology

This project focuses exclusively on **Univariate Exploratory Data Analysis**, which involves analyzing one variable at a time. The methodology includes:

### 1. **Descriptive Statistics**
- **Central Tendency:** Mean, Median, Mode
- **Dispersion:** Standard Deviation, Variance, Range, IQR
- **Distribution Shape:** Skewness, Kurtosis
- **Quartiles:** Q1 (25%), Q2 (50%), Q3 (75%)

### 2. **Visual Analysis**
- **Histogram:** Displays frequency distribution across bins
- **Box Plot:** Shows quartiles, median, and outliers
- **Density Plot (KDE):** Illustrates probability density function

### 3. **Outlier Detection**
- **IQR Method:** Identifies values beyond 1.5 × IQR from quartiles
- **Visual Identification:** Box plot whiskers and points

### 4. **Distribution Analysis**
- **Symmetry Assessment:** Based on skewness coefficient
- **Spread Analysis:** Range and standard deviation interpretation

---

## 🛠️ Tools & Technologies

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Python** | Programming language | 3.8+ |
| **Streamlit** | Web application framework | 1.31.0 |
| **Pandas** | Data manipulation and analysis | 2.2.0 |
| **NumPy** | Numerical computations | 1.26.3 |
| **Matplotlib** | Static visualizations | 3.8.2 |
| **Seaborn** | Statistical data visualization | 0.13.1 |
| **SciPy** | Statistical functions | 1.12.0 |

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.8 or higher installed
- pip (Python package manager)

### Installation & Execution

1. **Navigate to the project directory:**
   ```bash
   cd univariate-eda-mobile-usage
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the application:**
   - The application will automatically open in your default web browser
   - If not, navigate to: `http://localhost:8501`

---

## 📁 Project Structure

```
univariate-eda-mobile-usage/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── data/
│   └── mobile_app_usage.csv       # Sample dataset
│
└── images/
    └── screenshots/                # UI and plot screenshots
        └── .gitkeep               # Git folder placeholder
```

---

## ✨ Features

- ✅ **Interactive UI:** Clean and beginner-friendly interface
- ✅ **Flexible Data Input:** Support for default and custom CSV files
- ✅ **Comprehensive Statistics:** 13+ statistical measures
- ✅ **Multiple Visualizations:** Histogram, Box Plot, Density Plot
- ✅ **Automated Insights:** Distribution shape and outlier detection
- ✅ **Single Column Focus:** Strict univariate analysis approach
- ✅ **Real-time Analysis:** Instant results upon column selection

---

## 📈 Use Cases

1. **Academic Projects:** Suitable for data science coursework and assignments
2. **Research:** Quick exploratory analysis for research datasets
3. **Data Quality Assessment:** Identify outliers and distribution patterns
4. **Learning Tool:** Understand statistical concepts through visualization
5. **Mobile Analytics:** Analyze user behavior patterns in mobile applications

---

## 🎓 Academic Context

This project is designed for:
- **Data Science Students** learning EDA fundamentals
- **Academic Submissions** requiring clean, documented code
- **Beginner-Level Projects** with minimal complexity
- **GitHub Portfolio** showcasing data analysis skills

**Key Academic Concepts Covered:**
- Univariate statistical analysis
- Data visualization techniques
- Descriptive statistics
- Distribution analysis
- Outlier detection methods

---

## 📝 Notes

- This project focuses **strictly on univariate analysis** (one variable at a time)
- **No multivariate analysis** (correlation, grouping, scaling) is included
- The application is designed for **educational purposes**
- All code is well-commented for easy understanding

---

## 👨‍💻 Author

**Project Type:** Academic Data Science Project  
**Framework:** Streamlit  
**Analysis Type:** Univariate EDA  
**Completion Time:** 1 Day

---

## 📄 License

This project is open-source and available for educational purposes.

---

## 🙏 Acknowledgments

- Dataset: Synthetic mobile app usage data
- Framework: Streamlit community
- Visualization: Matplotlib and Seaborn libraries

---

**For questions or issues, please refer to the code comments in `app.py`.**
