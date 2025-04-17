import pandas as pd


Data=[
    {"name":"nsloni-1", "age":21, "city":"bangalore"},
    {"name":"ns-loni", "age":22, "city":"mumbai"},
    {"name":"ns-2", "age":23, "city":"delhi"},
    {"name":"loni-3", "age":24, "city":"pune"}
]



Data = pd.DataFrame(Data)


Data.to_csv("data/data.csv", index=False)