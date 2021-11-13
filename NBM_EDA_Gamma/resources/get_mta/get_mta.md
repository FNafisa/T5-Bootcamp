# Using *get_mta.py*

### Step 1

Save the *get_mta.py* file wherever you'd like to put your SQLite database (it will be called **mta_data**).

### Step 2

In that directory, run 

```
python get_mta.py <pat>
```

where `<pat>` is a regex pattern representing the weeks you'd like to grab from the [mta website](http://web.mta.info/developers/turnstile.html). If you don't type any `<pat>`, and just run `python get_mta.py`, it will default to pull data from the current month. So, you may run

```
python get_mta.py 2105
```

Possible `<pat>` strings:

* (default) the current month = `  `
* the 5th month of 2021 = `2105`
* just the year 2021 = `21`
* the 1st month of each year* = `[0-9][0-9]01`
* the last few years = `(21|20|19)`

**Why might this be a bad idea?*

### Step 3

Access the saved *mta_data.db* file, and start working on your project.

**Only run this once!!** Otherwise, you may have data duplicated, and you'll have to delete the *mta_data.db* file, and run this again.
