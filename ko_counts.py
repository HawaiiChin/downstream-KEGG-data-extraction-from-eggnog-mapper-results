import pandas as pd
import sys

infile = sys.argv[1]
outfile = sys.argv[2]
df = pd.read_csv(infile, sep='\t', names=["sample", "gene", "KO"])
ko_counts = (
        df.groupby(["sample","KO"])
        .size()
        .reset_index(name="count")
)
ko_counts.to_csv(outfile, sep="\t", index=False)
