import pandas as pd
import sys

ko_table=sys.argv[1]
ko2path=sys.argv[2]
outfile=sys.argv[3]

ko = pd.read_csv(ko_table, sep="\t", index_col=0)
ko = (ko > 0).astype(int)
ko = ko.reset_index()
ko = ko.rename(columns={ko.columns[0]:"KO"})
sample_cols=ko.columns.tolist()

ko["KO"]=ko["KO"].str.replace("^ko", "K", regex=True)

map_df=pd.read_csv(ko2path, sep="\t", header = None, names=["KO","Pathway"])

map_df["KO"]=map_df["KO"].str.replace("^ko:", "", regex=True)
map_df["Pathway"]=map_df["Pathway"].str.replace("^path:","",regex=True)

pathway_sizes= (map_df.groupby("Pathway")["KO"].nunique())

merged = map_df.merge(ko,on="KO", how="inner"
                      )

if merged.empty:
  raise ValueError(
    "merged file is empty, check table match"
  )

present = (merged.groupby("Pathway")[sample_cols].sum()
           )

completeness=present.div(pathway_sizes, axis=0)
completeness.to_csv(outfile, sep="\t")
