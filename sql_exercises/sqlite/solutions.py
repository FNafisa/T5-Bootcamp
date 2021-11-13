#%%
from sqlalchemy import create_engine
import pandas as pd
# %%
engine= create_engine("sqlite:///baby_names.db")
#%%
all_tables = engine.table_names()
# %%
all_tables
# %%

# %%
