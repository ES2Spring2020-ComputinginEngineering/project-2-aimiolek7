# Project 1 --- ES2
# Step 4: K Means Clustering (functions)

#*****************************************
#
# YOUR NAME:Abigail Imiolek
#
#*****************************************

# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import random


def openckdfile():
#This function takes no arguments
#This function opens the ckd file, and loads the data into three array.
#This function returns 3 arrays; one for each of the types of data glucose: hemoglobin, classification
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
#This function takes three arguments: the arrays of the imported data
#This function normalizes the data, and changes the range for the hemoglobin and glucose data from 0-1
#This function returns three arrays: two containing the normalized glucose and hemoglobin arrays, and the initial classification array.
    hemoglobin_scaled=(hemoglobin-3.1)/(17.8-3.1)
    glucose_scaled=(glucose-70)/(490-70)
    return hemoglobin_scaled, glucose_scaled, classification

def select_k (hemoglobin, glucose, k):
#This function takes three arguments, the hemoglobin and glucose data arrays, and an integer,k.
#This function takes the hemoglobin and glucose arrays, orders them to find the highest and lowest points, and randomly generate k clusters within the data.
#This function  returns two arrays: centroid_glucose, centroid_hemoglobin, which contain the glucose and hemoglobin data for each centroid's location.
    sorted_hemoglobin=np.sort(hemoglobin)
    sorted_glucose=np.sort(glucose)
    low_h=sorted_hemoglobin[0]
    high_h=sorted_hemoglobin[-1]
    low_g=sorted_glucose[0]
    high_g=sorted_glucose[-1]
    centroid_glucose=np.array([])
    centroid_hemoglobin=np.array([])
    counter=0
    while counter<k:
        random_hemoglobin=round(random.uniform(low_h, high_h), 2)
        random_glucose=round(random.uniform(low_g, high_g), 2)
        centroid_glucose=np.append(centroid_glucose,random_glucose)
        centroid_hemoglobin=np.append(centroid_hemoglobin,random_hemoglobin)
        counter=counter+1
    return centroid_glucose, centroid_hemoglobin

def assign (hemoglobin, glucose, centroid_glucose, centroid_hemoglobin, k):
#This function has five arguments: the hemoglobin and glucose data arrays, and an integer,k, and the centroids' glucose and hemoglobin arrays.
#This function calculates the distance from the centroids to every point in the data set and creates an array which classifies each data point, depending on which centroid it's closest to
#This function has one return value, an array named cluster, which lists the classification of each data point.
    counter=0
    lines=0
    for i in glucose:
        lines=lines+1
    distance=np.empty(lines)
    while counter<k:
        for i in glucose:
            change_in_glucose=(glucose-centroid_glucose[counter])**2
        for j in hemoglobin:
            change_in_hemoglobin=(hemoglobin-centroid_hemoglobin[counter])**2
        dist=np.sqrt(change_in_glucose+change_in_hemoglobin)
        distance=np.vstack((distance,dist))
        counter=counter+1
    distance = np.delete(distance, 0, 0)
    counter2=0
    cluster=np.array([])
    for i in glucose:
        row=distance[:,counter2]
        distance_sort=np.sort(distance[:, counter2])
        if distance_sort[0] in row:
            lowest = np.where(row == distance_sort[0])
            cluster=np.append(cluster,lowest)
        else:
            pass
        counter2=counter2+1
    return cluster

def update (glucose, hemoglobin, cluster, k):
#This function has four arguments: the hemoglobin, glucose, and classification data arrays, and an integer, k.
#This function finds the mean of the glucose and hemoglobin for each classification, and repositions the centroid at the mean (hemoglobin, glucose) point.
#This function returns two  arrays: new_glucose_centroids, new_hemoglobin_centroids which contain the glucose and hemoglobin data for each new centroid's location.
    kcount=0
    new_glucose_centroids=[]
    new_hemoglobin_centroids=[]
    while kcount<k:
        gsumming=[]
        hsumming=[]
        sum_count=0
        counter=0
        for i in glucose:
            if cluster[counter]==kcount:
                gsumming=np.append(gsumming,glucose[counter])
                counter=counter+1
                sum_count=sum_count+1
            else:
                counter=counter+1
        mean=np.sum(gsumming)/sum_count
        new_glucose_centroids=np.append(new_glucose_centroids, mean)
        counter=0
        sum_count=0
        for i in hemoglobin:
            if cluster[counter]==kcount:
                hsumming=np.append(hsumming,hemoglobin[counter])
                counter=counter+1
                sum_count=sum_count+1
            else:
                counter=counter+1
        mean=np.sum(hsumming)/sum_count
        new_hemoglobin_centroids=np.append(new_hemoglobin_centroids, mean)
        kcount=kcount+1
    return (new_glucose_centroids, new_hemoglobin_centroids)
            
def centroid_check (new_glucose_centroids, new_hemoglobin_centroids,centroid_glucose, centroid_hemoglobin):
#This function takes four arguments: the centroids' old and new glucose and hemoglobin arrays
#This functions will find the change in position of the two centroids
#This function will return two arrays for the changes in the hemoglobin and glucose values for the centroids: glucose_change, hemoglobin_change
    glucose_change=new_glucose_centroids-centroid_glucose
    hemoglobin_change=new_hemoglobin_centroids-centroid_hemoglobin
    return glucose_change, hemoglobin_change

def centroid_rename (new_glucose_centroids, new_hemoglobin_centroids):
#This function takes two arguments: the centroids' new glucose and hemoglobin arrays.
#This function renames the “new” functions without the name “new”.
#This function returns two arrays: centroid_glucose, centroid_hemoglobin, which contain the glucose and hemoglobin data for each centroid's location.
    centroid_glucose=new_glucose_centroids
    centroid_hemoglobin=new_hemoglobin_centroids
    return centroid_glucose, centroid_hemoglobin

def cluster (hemoglobin, glucose, centroid_glucose, centroid_hemoglobin, k):
#This function takes five arguments: the hemoglobin and glucose data arrays, and an integer, k, and the centroids' glucose and hemoglobin arrays.
#This function calls the assign, update, centroid_check, and  centroid_rename in a while loop until all the centroid is in the center, and has stopped changing location
#This function returns three arrays: centroid_glucose, centroid_hemoglobin, cluster, which contain the centroids’ glucose and hemoglobin locations and the classification.
    not_set=False
    while not_set==False:
        cluster=assign (hemoglobin, glucose, centroid_glucose, centroid_hemoglobin, k)
        new_glucose_centroids, new_hemoglobin_centroids=update (glucose, hemoglobin, cluster,k)
        glucose_change, hemoglobin_change=centroid_check (new_glucose_centroids, new_hemoglobin_centroids,centroid_glucose, centroid_hemoglobin)
        centroid_glucose, centroid_hemoglobin=centroid_rename (new_glucose_centroids, new_hemoglobin_centroids)
        ginternal_count=0
        hinternal_count=0
        gzero_count=0
        hzero_count=0
        for i in glucose_change:
            if glucose_change[ginternal_count]>0:
                ginternal_count=ginternal_count+1
            else:
                ginternal_count=ginternal_count+1
                gzero_count=gzero_count+1
        for i in hemoglobin_change:
            if hemoglobin_change[hinternal_count]>0:
                hinternal_count=hinternal_count+1
            else:
                hinternal_count=hinternal_count+1
                hzero_count=hzero_count+1
        if hzero_count==k and gzero_count==k:
            not_set=True
        else:
            not_set=False
    return centroid_glucose, centroid_hemoglobin, cluster

def unnormalize(centroid_glucose, centroid_hemoglobin):
#This function takes two arrays which contain the centroids’ glucose and hemoglobin locations.
#This function un-normalizes the data, so the centroids fit in with the initial data set
#This function returns two arrays: centroid_hemo_unscaled, centroid_glucose_unscaled, which contain the centroids’ glucose and hemoglobin locations, on the scale of the original data.
    centroid_hemo_unscaled=(17.8-3.1)*(centroid_hemoglobin)+3.1
    centroid_glucose_unscaled=(490-70)*(centroid_glucose)+70
    return centroid_hemo_unscaled, centroid_glucose_unscaled

def graphingKMeans(glucose, hemoglobin, cluster, centroid_hemo_unscaled, centroid_glucose_unscaled,k):
    plt.figure()
#This function takes five arguments: the hemoglobin and glucose data arrays, the classification array, and the centroids' un-normalized glucose and hemoglobin arrays.
#This function graphs each (hemoglobin, glucose) point, showing its array.
#This function also graphs each centroid.
#This function has no return value.
    for i in range(k):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[cluster==i],glucose[cluster==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroid_hemo_unscaled[i], centroid_glucose_unscaled[i], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
#The following functions only apply when k=2.
def true_Positives (cluster, classification):  
#This function takes two arguments: the original classifaction array and the cluster classifiaction array.
#This function calculates what percentage of CKD patients were correctly labeled.
#This function returns a floating point value of the percent correctly labeled
    counter=0
    correct_counter=0
    div_counter=0
    for i in cluster:
        if int(cluster[counter])==0 and classification[counter]==0: 
            correct_counter=correct_counter+1
            counter=counter+1
            div_counter=div_counter+1
        elif int(cluster[counter])==1 and classification[counter]==0:
            counter=counter+1
            div_counter=div_counter+1
        else:
            counter=counter+1
    correct_labeled=correct_counter/div_counter*100
    return correct_labeled

def false_Positives (cluster, classification):
#This function takes two arguments: the original classifaction array and the cluster classifiaction array.
#This function calculates what percentage of non-CKD patients were incorrectly labeled.
#This function returns a floating point value of the percent incorrectly labeled
    counter=0
    incorrect_counter=0
    div_counter=0
    for i in cluster:
        if int(cluster[counter])==0 and classification[counter]==1: 
            incorrect_counter=incorrect_counter+1
            counter=counter+1
            div_counter=div_counter+1
        elif int(cluster[counter])==1 and classification[counter]==1:
            counter=counter+1
            div_counter=div_counter+1
        else:
            counter=counter+1
    incorrect_labeled=incorrect_counter/div_counter*100
    return incorrect_labeled

def true_Negatives(cluster, classification):
#This function takes two arguments: the original classifaction array and the cluster classifiaction array.
#This function calculates what percentage of non-CKD patients were correctly labeled.
#This function returns a floating point value of the percent correctly labeled
    counter=0
    correct_counter=0
    div_counter=0
    for i in cluster:
        if int(cluster[counter])==1 and classification[counter]==1: 
            correct_counter=correct_counter+1
            counter=counter+1
            div_counter=div_counter+1
        elif int(cluster[counter])==0 and classification[counter]==1:
            counter=counter+1
            div_counter=div_counter+1
        else:
            counter=counter+1
    correct_labeled=correct_counter/div_counter*100
    return correct_labeled

def false_Negatives (cluster, classification):
#This function takes two arguments: the original classifaction array and the cluster classifiaction array.
#This function calculates what percentage of CKD patients were incorrectly labeled.
#This function returns a floating point value of the percent correctly labeled
    counter=0
    incorrect_counter=0
    div_counter=0
    for i in cluster:
        if int(cluster[counter])==1 and classification[counter]==0: 
            incorrect_counter=incorrect_counter+1
            counter=counter+1
            div_counter=div_counter+1
        elif int(cluster[counter])==0 and classification[counter]==0:
            counter=counter+1
            div_counter=div_counter+1
        else:
            counter=counter+1
    incorrect_labeled=incorrect_counter/div_counter*100
    return incorrect_labeled