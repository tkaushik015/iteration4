import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache
def load_bowling_data():
    return pd.read_csv('2023_bowling.csv')

@st.cache
def load_batting_data():
    return pd.read_csv('2023_batting.csv')

bowling_df = load_bowling_data()
batting_df = load_batting_data()

# Sidebar filters
st.sidebar.header('Filters')
analysis_option = st.sidebar.selectbox('Analysis Option', ['Bowling Stats', 'Batting Stats'])

country_list = list(batting_df['Country'].unique())

country = st.sidebar.selectbox("Select Country",country_list)

# Function to filter bowling data
def filter_bowling_data(df):
    if country:
        df2 = df[df['Country'].str.contains(country, case=False)]
    return df2

# Function to filter batting data
def filter_batting_data(df):
    if country:
        df2 = df[df['Country'].str.contains(country, case=False)]
    return df2

if st.sidebar.button('Submit'):
    if analysis_option == 'Bowling Stats':
        filtered_bowling_df = filter_bowling_data(bowling_df)
        st.write(filtered_bowling_df)

        # Visualizations for Bowling Stats
        st.subheader('Bowling Statistics Visualizations')
        
        # Bar plot of Wickets by Country
        st.write("Bar plot of Wickets by Country:")
        fig = px.bar(filtered_bowling_df, x='Country', y='Wickets', title='Wickets by Country')
        st.plotly_chart(fig)

        # Heatmap of Correlation Matrix
        st.write("Heatmap of Correlation Matrix for Bowling Statistics:")
        corr_matrix = filtered_bowling_df.corr()
        fig = px.imshow(corr_matrix, labels=dict(x="Features", y="Features", color="Correlation"))
        st.plotly_chart(fig)

    elif analysis_option == 'Batting Stats':
        filtered_batting_df = filter_batting_data(batting_df)
        st.write(filtered_batting_df)

        # Visualizations for Batting Stats
        st.subheader('Batting Statistics Visualizations')
        
        # Pie chart of Hundred's distribution by Country
        st.write("Pie chart of Hundred's distribution by Country:")
        hundreds_by_country = filtered_batting_df.groupby("Country")["Hundreds"].sum().reset_index()
        fig = px.pie(hundreds_by_country, values='Hundreds', names='Country', title='Hundred\'s distribution by Country')
        st.plotly_chart(fig)

        # Scatter plot of Strike Rate vs Fifties
        st.write("Scatter plot of Strike Rate vs Fifties:")
        fig = px.scatter(filtered_batting_df, x='Strike_rate', y='Fifties', title='Strike Rate vs Fifties')
        st.plotly_chart(fig)

        # Line plot of Runs vs Innings
        st.write("Line plot of Runs vs Innings:")
        fig = px.line(filtered_batting_df, x='Innings', y='Runs', color='Country', title='Runs vs Innings')
        st.plotly_chart(fig)

        # Box plot of Average by Country
        st.write("Box plot of Average by Country:")
        fig = px.box(filtered_batting_df, x='Country', y='Average', title='Average by Country')
        st.plotly_chart(fig)

else:
    if analysis_option == 'Bowling Stats':
        st.write(bowling_df)

    elif analysis_option == 'Batting Stats':
        st.write(batting_df)
