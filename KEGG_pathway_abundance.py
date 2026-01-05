import pandas as pd
ko = pd.read_csv(
        "KO_by_sample.tsv",
        sep="\t",
        index_col=0
)

map_df = pd.read_csv(
        "ko2pathway.txt",
        sep="\t",
        header=None,
        names=["KO", "Pathway"]
)

map_df["Pathway"] = map_df["Pathway"].str.replace("path:","")
merged = map_df.merge(
        ko.reset_index(),
        on="KO",
        how="inner"
)
pathway_abundance=(
        merged.groupby("Pathway").sum(numeric_only=True)
)

pathway_abundance.to_csv(
        "pathway_by_sample.tsv", sep="\t"
)
