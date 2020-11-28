import pandas as pd

time_sentences = [
    "Monday: The doctor's appointment is at 2:45pm.",
    "Tuesday: The dentist's appointment is at 11:30 am.",
    "Wednesday: At 7:00pm, there is a basketball game!",
    "Thursday: Be back home by 11:15 pm at the latest.",
    "Friday: Take the train at 08:10 am, arrive at 09:00am.",
]

df = pd.DataFrame(time_sentences, columns=["text"])
print(df)

"""
                                                text
0     Monday: The doctor's appointment is at 2:45pm.
1  Tuesday: The dentist's appointment is at 11:30...
2  Wednesday: At 7:00pm, there is a basketball game!
3  Thursday: Be back home by 11:15 pm at the latest.
4  Friday: Take the train at 08:10 am, arrive at ...
"""
# find the number of caracters for each string in df['text']
number = df["text"].str.len()
print(number)
"""
0    46
1    50
2    49
3    49
4    54
Name: text, dtype: int64
"""

# find the number of tokens foreach string in df['text']
num_tokens = df["text"].str.split().str.len()
print(num_tokens)
"""
0     7
1     8
2     8
3    10
4    10
Name: text, dtype: int64
"""

# find which entries conatin the word 'appointment'
appointment = df["text"].str.contains("appointment")
print(appointment)
"""
0     True
1     True
2    False
3    False
4    False
Name: text, dtype: bool
"""

# find all occurances of the digits
digits = df["text"].str.findall(r"\d")
print(digits)
"""
0                   [2, 4, 5]
1                [1, 1, 3, 0]
2                   [7, 0, 0]
3                [1, 1, 1, 5]
4    [0, 8, 1, 0, 0, 9, 0, 0]
Name: text, dtype: object
"""
# group and find the hours and minutes
hr_mins = df["text"].str.findall(r"(\d?\d):(\d\d)")
print(hr_mins)

"""
0               [(2, 45)]
1              [(11, 30)]
2               [(7, 00)]
3              [(11, 15)]
4    [(08, 10), (09, 00)]
Name: text, dtype: object
"""
# replace weekdays with '???
weekdays = df["text"].str.replace(r"\w+day\b", "???")
print(weekdays)

"""
0          ???: The doctor's appointment is at 2:45pm.
1       ???: The dentist's appointment is at 11:30 am.
2          ???: At 7:00pm, there is a basketball game!
3         ???: Be back home by 11:15 pm at the latest.
4    ???: Take the train at 08:10 am, arrive at 09:...
Name: text, dtype: object
"""
# replace weekdays with 3 letter abbrevations
abr_weekdays = df["text"].str.replace(r"(\w+day\b)", lambda x: x.groups()[0][:3])
print(abr_weekdays)

"""
0          Mon: The doctor's appointment is at 2:45pm.
1       Tue: The dentist's appointment is at 11:30 am.
2          Wed: At 7:00pm, there is a basketball game!
3         Thu: Be back home by 11:15 pm at the latest.
4    Fri: Take the train at 08:10 am, arrive at 09:...
Name: text, dtype: object
"""

# create new columns from fiest match of extracted groups
columns = df["text"].str.extract(r"(\d?\d):(\d\d)")
print(columns)
"""
    0   1
0   2  45
1  11  30
2   7  00
3  11  15
4  08  10
"""

# extradct the entire time, the hours, the minutes, adn teh period

time = df["text"].str.extractall(r"((\d?\d):(\d\d) ?([ap]m))")
print(time)
"""
                0   1   2   3
  match                      
0 0        2:45pm   2  45  pm
1 0      11:30 am  11  30  am
2 0        7:00pm   7  00  pm
3 0      11:15 pm  11  15  pm
4 0      08:10 am  08  10  am
  1       09:00am  09  00  am
"""

time_groups = df["text"].str.extractall(
    r"(?P<time>(?P<hour>\d?\d):(?P<minute>\d\d) ?(?P<period>[ap]m))"
)
print(time_groups)
"""
             time hour minute period
  match                             
0 0        2:45pm    2     45     pm
1 0      11:30 am   11     30     am
2 0        7:00pm    7     00     pm
3 0      11:15 pm   11     15     pm
4 0      08:10 am   08     10     am
  1       09:00am   09     00     am
"""
