import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Optional seaborn import with fallback
try:
    import seaborn as sns
    SEABORN_AVAILABLE = True
except ImportError:
    SEABORN_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="Univariate EDA - Mobile App Usage",
    page_icon="📊",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">📊 Univariate Exploratory Data Analysis</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Mobile App Usage Behavior Analysis</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📁 Data Source")
data_option = st.sidebar.radio(
    "Choose data source:",
    ["Use Default Dataset", "Upload Custom CSV"]
)

# Load data
df = None

if data_option == "Use Default Dataset":
    try:
        df = pd.read_csv("data/mobile_app_usage.csv")
        st.sidebar.success("✅ Default dataset loaded successfully!")
    except FileNotFoundError:
        st.sidebar.error("❌ Default dataset not found. Please upload a CSV file.")
else:
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("✅ Custom dataset loaded successfully!")

# Main content
if df is not None:
    # Dataset Overview Section
    st.header("📋 Dataset Overview")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rows", df.shape[0])
    with col2:
        st.metric("Total Columns", df.shape[1])
    with col3:
        st.metric("Numerical Columns", len(df.select_dtypes(include=[np.number]).columns))
    
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)
    
    # Get numerical columns only
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numerical_cols) == 0:
        st.error("❌ No numerical columns found in the dataset. Please upload a dataset with numerical data.")
    else:
        st.markdown("---")
        
        # Column Selection
        st.header("🔍 Select Column for Univariate Analysis")
        selected_column = st.selectbox(
            "Choose a numerical column:",
            numerical_cols,
            help="Select one column at a time for univariate analysis"
        )
        
        if selected_column:
            st.markdown("---")
            
            # Get the selected column data
            data = df[selected_column].dropna()
            
            # Summary Statistics Section
            st.header(f"📈 Summary Statistics: {selected_column}")
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.metric("Mean", f"{data.mean():.2f}")
            with col2:
                st.metric("Median", f"{data.median():.2f}")
            with col3:
                st.metric("Std Dev", f"{data.std():.2f}")
            with col4:
                st.metric("Min", f"{data.min():.2f}")
            with col5:
                st.metric("Max", f"{data.max():.2f}")
            
            # Additional statistics
            st.subheader("Detailed Statistics")
            stats_df = pd.DataFrame({
                'Statistic': ['Count', 'Mean', 'Median', 'Mode', 'Standard Deviation', 
                              'Variance', 'Range', 'Q1 (25%)', 'Q2 (50%)', 'Q3 (75%)', 
                              'IQR', 'Skewness', 'Kurtosis'],
                'Value': [
                    data.count(),
                    data.mean(),
                    data.median(),
                    data.mode()[0] if len(data.mode()) > 0 else np.nan,
                    data.std(),
                    data.var(),
                    data.max() - data.min(),
                    data.quantile(0.25),
                    data.quantile(0.50),
                    data.quantile(0.75),
                    data.quantile(0.75) - data.quantile(0.25),
                    data.skew(),
                    data.kurtosis()
                ]
            })
            st.dataframe(stats_df, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            
            # Visualizations Section
            st.header(f"📊 Visualizations: {selected_column}")
            
            # Set style for plots (only if seaborn is available)
            if SEABORN_AVAILABLE:
                sns.set_style("whitegrid")
            
            # Histogram
            st.subheader("1️⃣ Histogram")
            st.write("Shows the frequency distribution of the data")
            
            fig1, ax1 = plt.subplots(figsize=(10, 5))
            ax1.hist(data, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
            ax1.set_xlabel(selected_column, fontsize=12)
            ax1.set_ylabel('Frequency', fontsize=12)
            ax1.set_title(f'Histogram of {selected_column}', fontsize=14, fontweight='bold')
            ax1.grid(axis='y', alpha=0.3)
            st.pyplot(fig1)
            plt.close()
            
            # Box Plot
            st.subheader("2️⃣ Box Plot")
            st.write("Displays the distribution, median, quartiles, and outliers")
            
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            box = ax2.boxplot(data, vert=False, patch_artist=True, 
                             boxprops=dict(facecolor='lightgreen', alpha=0.7),
                             medianprops=dict(color='red', linewidth=2),
                             whiskerprops=dict(color='black', linewidth=1.5),
                             capprops=dict(color='black', linewidth=1.5))
            ax2.set_xlabel(selected_column, fontsize=12)
            ax2.set_title(f'Box Plot of {selected_column}', fontsize=14, fontweight='bold')
            ax2.grid(axis='x', alpha=0.3)
            st.pyplot(fig2)
            plt.close()
            
            # Density Plot (KDE)
            st.subheader("3️⃣ Density Plot (KDE)")
            st.write("Shows the probability density function of the data")
            
            # Show warning if seaborn is not available
            if not SEABORN_AVAILABLE:
                st.warning("⚠️ Seaborn not installed. Using matplotlib for density plot.")
            
            fig3, ax3 = plt.subplots(figsize=(10, 5))
            
            if SEABORN_AVAILABLE:
                # Use pandas built-in density plot (which uses scipy KDE)
                data.plot(kind='density', ax=ax3, color='purple', linewidth=2)
                ax3.fill_between(ax3.lines[0].get_xdata(), ax3.lines[0].get_ydata(), alpha=0.3, color='purple')
            else:
                # Fallback to matplotlib histogram with density=True
                ax3.hist(data, bins=30, density=True, color='purple', alpha=0.5, edgecolor='black')
                # Add a simple line overlay using histogram
                counts, bins = np.histogram(data, bins=30, density=True)
                bin_centers = (bins[:-1] + bins[1:]) / 2
                ax3.plot(bin_centers, counts, color='purple', linewidth=2)
            
            ax3.set_xlabel(selected_column, fontsize=12)
            ax3.set_ylabel('Density', fontsize=12)
            ax3.set_title(f'Density Plot of {selected_column}', fontsize=14, fontweight='bold')
            ax3.grid(alpha=0.3)
            st.pyplot(fig3)
            plt.close()
            
            st.markdown("---")
            
            # Insights Section
            st.header("💡 Key Insights")
            
            # Distribution shape
            skewness = data.skew()
            if abs(skewness) < 0.5:
                distribution_shape = "approximately symmetric"
            elif skewness > 0:
                distribution_shape = "positively skewed (right-skewed)"
            else:
                distribution_shape = "negatively skewed (left-skewed)"
            
            # Outlier detection using IQR method
            Q1 = data.quantile(0.25)
            Q3 = data.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = data[(data < lower_bound) | (data > upper_bound)]
            
            st.write(f"**Distribution Shape:** The data is {distribution_shape} (Skewness: {skewness:.2f})")
            st.write(f"**Spread:** The data ranges from {data.min():.2f} to {data.max():.2f} with a standard deviation of {data.std():.2f}")
            st.write(f"**Central Tendency:** Mean = {data.mean():.2f}, Median = {data.median():.2f}")
            st.write(f"**Outliers:** {len(outliers)} potential outliers detected using IQR method")
            
            if len(outliers) > 0:
                st.write(f"**Outlier Values:** {sorted(outliers.values.tolist())}")

else:
    # Welcome message when no data is loaded
    st.info("👈 Please select a data source from the sidebar to begin analysis")
    
    st.markdown("---")
    st.subheader("📖 About This Application")
    st.write("""
    This application performs **Univariate Exploratory Data Analysis (EDA)** on mobile app usage data.
    
    **Features:**
    - 📊 Summary statistics (mean, median, standard deviation, etc.)
    - 📈 Histogram for frequency distribution
    - 📦 Box plot for quartiles and outliers
    - 📉 Density plot for probability distribution
    - 💡 Automated insights and outlier detection
    
    **How to Use:**
    1. Select a data source (default dataset or upload custom CSV)
    2. Choose a numerical column for analysis
    3. Explore the statistics and visualizations
    
    **Note:** This tool focuses strictly on univariate analysis (one variable at a time).
    """)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with Streamlit | Univariate EDA Project</p>",
    unsafe_allow_html=True
)
