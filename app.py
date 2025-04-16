import streamlit as st
from optimizer import generate_best_team

def main():
    st.title("Fantasy Premier League Optimizer")
    
    # Fetch and display the best team
    team = generate_best_team()
    
    st.header("Your Best Fantasy Premier League Team")
    st.dataframe(team)

if __name__ == "__main__":
    main()
