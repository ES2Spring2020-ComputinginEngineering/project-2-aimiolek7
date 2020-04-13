This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Abigail Imiolek, Project 2
This project contain four files:
ckd.csv
NearestNeighborClassification.py
KMeansClustering_functions.py
KMeansClustering_driver.py



ckd.csv contains the hemoglobin, glucose, and classification data, which is used in the three python files.



NearestNeighborClassification.py contains code that will classify a random test point in the hemoglobin
and glucose sets using the nearest neighbors and k nearest neighbor methods.
Currently, the main script is set up to classify and graph the same random point using both methods, 
and k=3 for k nearest neighbors.
The functions, openckdfile(), normalizeData(), createTestCase(), and normalizeTestCase must be called before
nearestNeighborClassifier() or kNearestNeighborClassifier().



KMeansClustering_functions.py contains all the functions needed to classify a data set, in this case, 
the hemoglobin, glucose, and classification data using k clusters.
 	My custom functions are:
select_k (hemoglobin, glucose, k)
	This function takes three arguments, the hemoglobin and glucose data arrays, and an integer,k.
	This function takes the hemoglobin and glucose arrays, orders them to find the highest and lowest points, and randomly generate k clusters within the data.
	This function returns two arrays: centroid_glucose, centroid_hemoglobin, which contain the glucose and hemoglobin data for each centroid's location.

assign (hemoglobin, glucose, centroid_glucose, centroid_hemoglobin, k)
	This function has five arguments: the hemoglobin and glucose data arrays, and an integer,k, and the centroids' glucose and hemoglobin arrays.
	This function calculates the distance from the centroids to every point in the data set and creates an array which classifies each data point, depending on which centroid it's closest to
	This function has one return value, an array named cluster, which lists the classification of each data point.

update (glucose, hemoglobin, cluster, k)
	This function has four arguments: the hemoglobin, glucose, and classification data arrays, and an integer, k.
	This function finds the mean of the glucose and hemoglobin for each classification, and repositions the centroid at the mean (hemoglobin, glucose) point.
	This function returns two  arrays: new_glucose_centroids, new_hemoglobin_centroids which contain the glucose and hemoglobin data for each new centroid's location.

centroid_check (new_glucose_centroids, new_hemoglobin_centroids, centroid_glucose, centroid_hemoglobin)
	This function takes four arguments: the centroids' old and new glucose and hemoglobin arrays
	This functions will find the change in position of the two centroids
	This function will return two arrays for the changes in the hemoglobin and glucose values for the centroids: glucose_change, hemoglobin_change

centroid_rename (new_glucose_centroids, new_hemoglobin_centroids)
	This function takes two arguments: the centroids' new glucose and hemoglobin arrays.
	This function renames the “new” functions without the name “new”.
	This function returns two arrays: centroid_glucose, centroid_hemoglobin, which contain the glucose and hemoglobin data for each centroid's location.

cluster (hemoglobin, glucose, centroid_glucose, centroid_hemoglobin, k)
	This function takes five arguments: the hemoglobin and glucose data arrays, and an integer, k, and the centroids' glucose and hemoglobin arrays.
	This function calls the assign, update, centroid_check, and  centroid_rename in a while loop until all the centroid is in the center, and has stopped changing location
	This function returns three arrays: centroid_glucose, centroid_hemoglobin, cluster, which contain the centroids’ glucose and hemoglobin locations and the classification.

unnormalize (centroid_glucose, centroid_hemoglobin):
	This function takes two arrays which contain the centroids’ glucose and hemoglobin locations.
	This function un-normalizes the data, so the centroids fit in with the initial data set
	This function returns two arrays: centroid_hemo_unscaled, centroid_glucose_unscaled, which contain the centroids’ glucose and hemoglobin locations, on the scale of the original data.

true_Positives (cluster, classification):  
	This function takes two arguments: the original classifaction array and the cluster classifiaction array.
	This function calculates what percentage of CKD patients were correctly labeled.
	This function returns a floating point value of the percent correctly labeled

false_Positives (cluster, classification):
	This function takes two arguments: the original classifaction array and the cluster classifiaction array.
	This function calculates what percentage of non-CKD patients were incorrectly labeled.
	This function returns a floating point value of the percent incorrectly labeled

true_Negatives(cluster, classification):
	This function takes two arguments: the original classifaction array and the cluster classifiaction array.
	This function calculates what percentage of non-CKD patients were correctly labeled.
	This function returns a floating point value of the percent correctly labeled

false_Negatives (cluster, classification):
	This function takes two arguments: the original classifaction array and the cluster classifiaction array.
	This function calculates what percentage of CKD patients were incorrectly labeled.
	This function returns a floating point value of the percent correctly labeled.



KMeansClustering_driver.py calls all the functions in KMeansClustering_functions.py in order to find a set number 
of clusters and graph the set results.
Currently, the driver is set up, so a user just needs to set k, and the driver will calcute that many clusters in
the (hemoglobin, glucose) dataset.
Furthermore, if the user sets k=2, the driver will also calculate how accurate the formed clusters are based on the
classification data. 
