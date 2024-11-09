import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data_path = 'movies_2024.csv'
df = pd.read_csv(data_path)

# Title for the Streamlit app
st.title("Budget vs Revenue Analysis")

# Display the dataframe
st.write("### Movie Dataset Overview")
st.dataframe(df.head())

# Check if the required columns exist in the data
if 'budget' in df.columns and 'revenue' in df.columns:
    # Drop rows with missing budget or revenue data
    df_filtered = df.dropna(subset=['budget', 'revenue'])
    
    # Plot budget vs revenue
    st.write("### Budget vs Revenue Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(df_filtered['budget'], df_filtered['revenue'], alpha=0.5)
    ax.set_xlabel('Budget')
    ax.set_ylabel('Revenue')
    ax.set_title('Budget vs Revenue')
    
    # Show the plot in the Streamlit app
    st.pyplot(fig)
else:
    st.error("The dataset does not contain 'budget' and 'revenue' columns.")
