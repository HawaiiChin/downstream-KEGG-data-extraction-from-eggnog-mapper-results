import pandas as pd
import glob
import os
files = glob.glob("*.ko.counts.tsv")
dfs = []
for f in files:
    sample = os.path.basename(f).split(".")[0]
    df = pd.read_csv(f,sep="\t")
    df = df[["KO", "count"]].set_index("KO")
    df.columns=[sample]
    dfs.append(df)

matrix = pd.concat(dfs, axis=1).fillna(0).astype(int)
matrix.to_csv("KO_by_sample.tsv", sep="\t")

