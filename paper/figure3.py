import sys

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

colors = sns.color_palette("Set2")

df = pd.read_csv(sys.argv[1], sep="\t") # 1kg.pairs.tsv

s = 25
if df.shape[0] > 1000:
    s = 10

print(s)


for i, ex_rel in enumerate(df.expected_relatedness.unique()):
    sub = df.loc[df.expected_relatedness == ex_rel, :]
    plt.scatter(sub.ibs0, sub.ibs2, label="unrelated" if ex_rel == -1 else
            "identical", ec="none", c=colors[i], s=s)

sub = df.loc[df.ibs0 < 600]
plt.scatter(sub.ibs0, sub.ibs2, label="unexpected relatedness",
        ec="k", c=colors[0], s=s+4)

plt.xlabel("Number of IBS0 sites")
plt.ylabel("Number of IBS2 sites")

sns.despine()
plt.legend(title="expected relatedness")
plt.savefig("somalier-figure3.eps")
plt.show()
