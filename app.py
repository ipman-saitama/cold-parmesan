import streamlit as st
from optimizer import generate_best_team

def main():
    st.title("Fantasy Premier League Optimizer")
    
    # Display the best team
    team = generate_best_team()
    
    st.header("Your Best Fantasy Premier League Team")
    st.write(team)
    
if __name__ == "__main__":
    main()
