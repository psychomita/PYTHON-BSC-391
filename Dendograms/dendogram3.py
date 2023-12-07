import pandas as pd
from scipy.spatial import distance_matrix
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
data = [[1, 1], [2, 3], [3, 5],[4,5],[6,6],[7,5]]
points=["A","B","C","D","E","F"]
df = pd.DataFrame(data, columns=['xcord', 'ycord'],index=points)
ytdist=pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
linkage_matrix = linkage(ytdist, "single")
dendrogram(linkage_matrix, labels=["A", "B", "C","D","E","F"])
plt.title("Dendrogram Using Single Linkage")
plt.show()
