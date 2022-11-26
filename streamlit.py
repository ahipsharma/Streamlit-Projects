import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('images/dna-logo.jpg')
st.image(image, use_column_width=True)

st.write("""
         # Dna Nucleotide web app.
         This app counts the neucleotide composition of the query DNA!!!
         
         ***
         """)



st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nTAGCACGTCTGTCCGGGGTT\nACGTACGTGATGGGAACACT"
sequence = st.text_area("Sequence Input", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
         ***
         """)

# st.header('Input (DNA Query)')
# sequence

st.header('OUTPUT (DNA Nucleotide Count)')

## Print Dictionary
st.subheader('1 - Print Dictionary')

def DNA_Neucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d;

X = DNA_Neucleotide_count(sequence)
X
st.subheader('2. Print text')
st.write('There are ' +str(X['A']) + ' adenanine(A) in the sequence')
st.write('There are ' +str(X['T']) + ' adenanine(T) in the sequence')
st.write('There are ' +str(X['G']) + ' adenanine(G) in the sequence')
st.write('There are ' +str(X['C']) + ' adenanine(C) in the sequence')

st.subheader('2. Print Data Frame')

df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'neucleotide'})
st.write(df)

st.subheader('2. Print Bar graph')

p = alt.Chart(df).mark_bar().encode(
    x='neucleotide',
    y='count'
)
p=p.properties(
    width = alt.Step(80)
)
st.write(p)