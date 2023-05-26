import pandas as pd

# READ CSV FILES
df = pd.read_csv("data/survey_results_public.csv")
schema_df = pd.read_csv("data/survey_results_schema.csv")

# VIEW ALL ROWS AND COLUMNS TO ITS HIGHEST NUMBER
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

df.head()