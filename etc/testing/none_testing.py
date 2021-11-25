import pandas as pd

test = pd.DataFrame({"a":[1,2,3,4,5], "b":[5,4,None,2,1]})

test["test"] = test["a"] / test["b"]

print(test.head())