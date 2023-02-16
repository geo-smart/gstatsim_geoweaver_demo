from plot_utilities import *
from install_dependencies import *

df_bed = pd.read_csv('https://github.com/GatorGlaciology/GStatSim/raw/main/demos/data/greenland_test_data.csv')
df_bed = df_bed[df_bed['Bed'] <= 700]
df_bed.head()
splot2D(df=df_bed, title='Subglacial topography data')
