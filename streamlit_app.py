import streamlit as st
import pandas as pd

st.write("## Dashboard Tutorial") # ## für Ueberschrift Anzeige 

df = pd.read_csv("Boardgame.csv", sep=";", index_col= 1)

Top_ten = df.head(10)

text = st.text_input("Spielname: ", value="")
st.write("**" + text + "**")


Treffer = df[df.index.str.contains(text)]
st.write(Treffer)

# Filtern nach Spieler anzahl
options = ["2", "3", "4", "5", "6"] # Auswahl Möglichkeiten in der Dropdown Liste
col_name = st.selectbox("Wähle eine Maximale Spieleranzahl", options)  
#st.write(col_name) # schreibt es auf dem Schirm 

tab1, tab2 = st.tabs(["Bar Chart", "Scatter Chart"])

show_plots = st.toggle('Show some plots')
if show_plots:
    df = df[df["Max Players"] == int(col_name)]
    st.write(df.shape) # Anzahl Zeilen + Spalten
    
    Top_ten = df.head(10)
    st.write(Top_ten)
    with tab1:
        st.bar_chart(Top_ten["Owned Users"])
    with tab2:
        st.scatter_chart(
        data=df, 
        x="Year Published", 
        y=["Min Players", "Max Players"], # Eckige Klammern, damit mehrere Linien angezeigt werden
        color=["#00008B", "#CD3333"],       # Größe in Pixeln (0= defualt)
        width=0, height=0,
        use_container_width=True)
    
else:
    st.write("Kein Plot vorhanden")
