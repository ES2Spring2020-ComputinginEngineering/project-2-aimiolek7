
import KMeansClustering_functions as kmc #Use kmc to call your functions
k=2


glucose, hemoglobin, classification=kmc.openckdfile()
hemoglobin_scaled, glucose_scaled, classification=kmc.normalizeData(glucose, hemoglobin, classification)
centroid_glucose, centroid_hemoglobin=kmc.select_k (hemoglobin_scaled, glucose_scaled,k)

centroid_glucose, centroid_hemoglobin, cluster=kmc.cluster(hemoglobin_scaled, glucose_scaled, centroid_glucose, centroid_hemoglobin, k)
centroid_hemo_unscaled, centroid_glucose_unscaled=kmc.unnormalize(centroid_glucose, centroid_hemoglobin)
kmc.graphingKMeans(glucose, hemoglobin, cluster, centroid_hemo_unscaled, centroid_glucose_unscaled,k)

if k==2:   
    print(kmc.true_Positives (cluster,classification))
    print(kmc.false_Positives (cluster, classification))
    print(kmc.true_Negatives (cluster, classification))
    print(kmc.false_Negatives (cluster, classification))
else:
    pass
    