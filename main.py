import streamlit as st
import pandas as pd

df = pd.read_csv('bundesliga_top7_offensive.csv')

st.write('# Bundesliga Top 7 Teams Offensive Stats 2020/2021')

option = st.selectbox(
    'Choose club?',
    (df.Club.unique()))

st.write('You selected:', option)

if option == 'All':
    df
else:
    df_option = df[df.Club == option].reset_index(drop=True)
    df_option

st.write('## All Goals and Assists by Top 7 Bundesliga Teams')
df_goals_assists = df.groupby(['Club']).sum()[['Goals', 'Assists']].sort_values('Goals', ascending=False)
st.table(df_goals_assists)

st.write('## Penalty Goals and Penalty Attempted by Top 7 Bundesliga Teams')
df_penalty = df.groupby(['Club']).sum()[['Penalty_Goals', 'Penalty_Attempted']].sort_values('Penalty_Goals', ascending=False)
df_penalty['Success Percentage (%)'] = (df_penalty['Penalty_Goals'] / df_penalty['Penalty_Attempted']) * 100
st.table(df_penalty)

st.write('## Top Scorers')
df_top_scorer = df.nlargest(5, 'Goals')[['Name', 'Club', 'Matches', 'Goals']].reset_index(drop=True)
df_top_scorer['Goal per Match (Mean)'] = df_top_scorer['Goals'] / df_top_scorer['Matches']
st.table(df_top_scorer)

st.write('## Most Assists by Player')
df_most_assists = df.nlargest(5, 'Assists')[['Name', 'Club', 'Position', 'Matches', 'Assists']].reset_index(drop=True)
st.table(df_most_assists)

st.write('## Most Minutes Played')
df_most_minuted = df.nlargest(5, 'Mins')[['Name', 'Club', 'Position', 'Matches', 'Mins']].reset_index(drop=True)
st.table(df_most_minuted)

st.write('## Youngest Player')
df_youngest = df.nsmallest(5, 'Age')[['Name', 'Club', 'Age', 'Goals', 'Assists']].reset_index(drop=True)
st.table(df_youngest)

st.write('## Oldest Player')
df_oldest = df.nlargest(5, 'Age')[['Name', 'Club', 'Age']].reset_index(drop=True)
st.table(df_oldest)
