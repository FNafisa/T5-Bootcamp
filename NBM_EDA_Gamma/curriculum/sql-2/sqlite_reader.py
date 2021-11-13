#%%
import sqlite3
# %%
con= sqlite3.connect("Northwind_large.sqlite")
#%%
cur = con.cursor()
x=cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# %%
for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table';"):
    print(row)
# %%
con.close()
# %%
