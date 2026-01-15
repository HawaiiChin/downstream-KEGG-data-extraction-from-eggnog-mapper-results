import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("pathway_by_sample.tsv", sep="\t", index_col=0)
df = np.log10(df + 1)

df_z = df.sub(df.mean(axis=1), axis=0)
df_z = df_z.div(df.std(axis=1), axis=0)

sns.clustermap(df_z,
               cmap="vlag",
               figsize=(10, 8),
               linewidths=0.2,
               xticklabels=True,
               yticklabels=True,
               method="average",
               metric="euclidean"
)

plt.savefig("kegg_clustered_heatmap.png", dpi=300)
plt.show()

top=df.var(axis=1).sort_values(ascending=False).head(30).index
df_top=df.loc[top]
