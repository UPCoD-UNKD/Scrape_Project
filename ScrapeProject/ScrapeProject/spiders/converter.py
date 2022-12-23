import pandas as pd
df = pd.read_json('output.json')

data = pd.DataFrame()

Profes = []
Loc = []
Desc = []
Tag = []
Time = []

for col in df.columns:
    if col == 'profession':
        for one in df[col]:
            for row in one:
                Profes.append(row)
    if col == 'location':
        for one in df[col]:
            for row in one:
                Loc.append(row)
    if col == 'description':
        for one in df[col]:
            for row in one:
                Desc.append(row)
    if col == 'tag':
        for one in df[col]:
            for row in one:
                Tag.append(row)
    if col == 'date':
        for one in df[col]:
            for row in one:
                Time.append(row)

data['Professions'] = pd.Series(Profes)
data['Locations'] = pd.Series(Loc)
data['Descriptions'] = pd.Series(Desc)
data['Tags'] = pd.Series(Tag)
data['Dates'] = pd.Series(Time)
data.to_csv('output.csv',encoding='utf-8')