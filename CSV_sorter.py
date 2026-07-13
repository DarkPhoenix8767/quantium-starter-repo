import pandas as pd
import glob

files = glob.glob(r"C:\Users\james\oneDrive\Documents\programming\python\quantium-starter-repo\data\*.csv")

print(files)

df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

df = df[df["product"] == "pink morsel"]

df["price"] = df["price"].str.replace("$", "").astype(float)

df["Sales"] = df["quantity"] * df["price"]

output = df[["Sales", "date", "region"]]

output.to_csv("quantium-starter-repo/output.csv", index=False)