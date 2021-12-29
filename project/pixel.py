import pandas as pd
df= pd.read_csv("projects/data.csv")
student_df= df.loc[df["student_id"]=="TRL_xsl"]
print(df.groupby("level")["attempt"].mean())

import plotly.graph_objects as go
fig= go.Figure(go.Bar(
    x= student_df.groupby("level")["attempt"].mean() ,
    y= ['level1','level2','level3','level4'],
    orientation='h'
))
fig.show()

