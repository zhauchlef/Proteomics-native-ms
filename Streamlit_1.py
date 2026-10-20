import streamlit as st
from bokeh.plotting import figure
from streamlit_bokeh import streamlit_bokeh
import pandas as pd

st.title('Streamlit Test') 

ms = pd.read_csv('bradykinin_ms2_cid10.tsv', sep='\t')

p = figure( title="Bradykinin Mass Spectra", x_axis_label="m/z value", y_axis_label="Relative Intensity")

p.line(ms['m/z'],ms['intensity'])
streamlit_bokeh(p, use_container_width=True)
