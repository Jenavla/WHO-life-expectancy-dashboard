import streamlit as st
from Case2 import scatterplot_machinelearning, customizable_scatter_plot, world_map, boxplot, correlation_matrix, missing_values

# Set up the Streamlit app title and theme
st.set_page_config(page_title="WHO Life Expectancy Dashboard", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for enhanced theming and professional look
st.markdown(
    """
    <style>
    /* Background of the main app container */
    .reportview-container {
        background-color: #f4f4f9;
        padding: 10px;
    }

    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
        padding: 10px;
    }

    /* Main title styling */
    h1 {
        font-family: 'Arial', sans-serif;
        color: #2c3e50;
        font-weight: bold;
        text-align: center;
        font-size: 40px;
    }

    /* Section Header styling */
    h2, h3 {
        font-family: 'Arial', sans-serif;
        color: #2c3e50;
        font-weight: bold;
    }

    /* Styling the box and correlation matrices headers */
    .header-style {
        font-size: 24px;
        color: #2c3e50;
        font-weight: 600;
        margin-top: 40px;
        margin-bottom: 20px;
    }

    /* Footer styling */
    .footer {
        text-align: center;
        padding: 20px;
        font-size: 14px;
        color: #7f8c8d;
        border-top: 1px solid #dcdcdc;
        margin-top: 50px;
    }

    /* Hover effect for interactive elements */
    .element-container:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: 0.3s ease;
    }

    </style>
    """, 
    unsafe_allow_html=True
)

# App Title
st.markdown(
    """
    <h1>WHO Life Expectancy Dashboard</h1>
    """, 
    unsafe_allow_html=True
)

# Introduction Section
st.write("## Introduction")
st.write("""
Life expectancy is a critical indicator of a population's health and social progress. This dashboard explores how various socioeconomic, health-related, and demographic factors impact life expectancy globally using data from the World Health Organization (WHO). The dataset includes variables such as income, education, healthcare expenditure, and mortality rates to assess these relationships.
""")

# Data Description
with st.expander('### Dashboard Data Description'):
    """
    The dashboard uses a dataset from the WHO, detailing health metrics across countries, covering:

    - **Country**: The country name.
    - **Year**: Year of data collection.
    - **Status**: Developed or developing classification.
    - **Life Expectancy**: Average life expectancy at birth (in years).
    - **Adult Mortality**: Death probability between ages 15 and 60 (per 1000 population).
    - **Infant Deaths**: Infant deaths per 1000 live births.
    - **Alcohol**: Alcohol consumption per capita (liters).
    - **Percentage Expenditure**: Healthcare expenditure as a percentage of GDP per capita.
    - **Hepatitis B**: Immunization coverage for Hepatitis B (% of 1-year-olds).
    - **Measles**: Reported measles cases per 1000 population.
    - **BMI**: Average Body Mass Index.
    - **Under-Five Deaths**: Deaths under five years per 1000 live births.
    - **Polio**: Immunization coverage for Polio (% of 1-year-olds).
    - **Total Expenditure**: Government health expenditure (% of total expenditure).
    - **Diphtheria**: Immunization coverage for Diphtheria (% of 1-year-olds).
    - **HIV/AIDS**: Deaths due to HIV/AIDS (0-4 years).
    - **GDP**: Gross Domestic Product per capita (USD).
    - **Population**: Total population.
    - **Thinness (1-19 years)**: Prevalence of thinness (%).
    - **Thinness (5-9 years)**: Prevalence of thinness (%).
    - **Income Composition of Resources**: Human Development Index reflecting income.
    - **Schooling**: Average schooling years.

    Use the visualizations below to explore relationships between these variables.
    """

# Side-by-side layout
col1, col2 = st.columns(2)

# Life expectancy box plot
with col1:
    st.markdown('<div class="header-style">Life Expectancy Boxplot by Continent</div>', unsafe_allow_html=True)
    st.write("""
    The boxplot illustrates the variations in life expectancy across continents. European countries generally show higher life expectancy with less variability, while African nations exhibit the lowest and most varied values. The spread across Asia, America, and Oceania also highlights regional disparities.
    """)
    boxplot()

# Missing values plot
with col2:
    st.markdown('<div class="header-style">Percentage of Missing Data</div>', unsafe_allow_html=True)
    st.write("""
    This plot displays the percentage of missing data for each column. Columns like Hepatitis B and GDP have significant gaps, leading us to exclude them. Missing values in other columns were filled using the median value for each continent.
    """)
    missing_values()

# Correlation matrix
st.markdown('<div class="header-style">Correlation Matrix</div>', unsafe_allow_html=True)
st.write("""
The correlation matrix reveals the relationships between life expectancy and various factors. Strong positive correlations were found between schooling (0.75), income composition (0.72), and life expectancy. On the contrary, high adult mortality (-0.70) and HIV/AIDS prevalence (-0.56) show strong negative correlations with life expectancy.
""")
correlation_matrix()

# Global Life Expectancy Map
st.markdown('<div class="header-style">Global Life Expectancy Map</div>', unsafe_allow_html=True)
st.write("""
This map visualizes life expectancy globally. Developed regions like Europe, North America, and East Asia tend to have higher life expectancies, while many countries in Sub-Saharan Africa have significantly lower values.
""")
world_map()

# Side-by-side layout for scatter plots
col3, col4 = st.columns(2)

# Machine Learning Scatter Plot
with col3:
    st.markdown('<div class="header-style">Machine Learning Scatter Plot</div>', unsafe_allow_html=True)
    st.write("""
    This scatterplot compares predicted life expectancy values to actual values using a machine learning model. The closer the points are to the diagonal line, the more accurate the model. The model performs reasonably well, though there are a few outliers.
    """)
    scatterplot_machinelearning()

# Customizable Scatter Plot
with col4:
    st.markdown('<div class="header-style">Customizable Scatter Plot</div>', unsafe_allow_html=True)
    st.write("""
    Adjust this scatterplot using the dropdown menu to explore how life expectancy relates to various factors, such as income, schooling, and healthcare expenditure.
    """)
    customizable_scatter_plot()

# Footer
st.markdown('<div class="footer">© 2024 Nathan Isaac | Data Source: World Health Organization</div>', unsafe_allow_html=True)
