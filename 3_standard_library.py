#%% import the entire library
import datetime

current_moment = datetime.datetime.now()

#%% only import specific parts from the library
from datetime import datetime, timedelta

current_moment = datetime.now()
print(current_moment)
later_moment   = current_moment + timedelta(hours=3)
print(later_moment)

# %% import a library as an alias
import datetime as dt

current_moment = dt.datetime().now()


# %% import a specific part of a library as an alias
from datetime import datetime as dt, timedelta as td

current_moment = dt.now()
print(current_moment)
later_moment   = current_moment + td(hours=3)
print(later_moment)
# %%
import math

math.exp(1)
# %%
