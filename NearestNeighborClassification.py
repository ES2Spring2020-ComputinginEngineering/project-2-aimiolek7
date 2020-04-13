# Project 1 --- ES2
# Steps 2 and 3: Nearest Neighbor Classification

#*****************************************
#
# YOUR NAME:Abigail Imiolek
#
#*****************************************

# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
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
    
def createTestCase():
#This function takes no arguments
#This function randomly generates a test case point
#This function returns a floating point number for the new hemoglobin point, and an integer for the new glucose point
    newhemoglobin=round(random.uniform(3.1,17.8), 1)
    newglucose=random.randint(70,490)
    print(newhemoglobin)
    print(newglucose)
    return newhemoglobin, newglucose

def normalizeTestCase(newglucose, newhemoglobin):
#This function takes two arguments: the randomly generate glucose and hemoglobin values.
#This function normalizes the randomly generated points, so they fit in the 0-1 data range.
#This function returns a floating point number for the scaled hemoglobin point, and an integer for the scaled glucose point.
    newhemoglobin_scaled=(newhemoglobin-3.1)/(17.8-3.1)
    newglucose_scaled=(newglucose-70)/(490-70)
    print(newhemoglobin_scaled)
    print(newglucose_scaled)
    return newhemoglobin_scaled, newglucose_scaled

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
#This function takes two arguments: the randomly generate glucose and hemoglobin values, and the hemoglobin and glucose values.
#This function calculates the distance of every (hemoglobin,glucose) point in the arrays to the newly generated points.
#This funcction returns an array of the distances.
    for i in glucose: 
        change_in_glucose=(glucose-newglucose)**2
    for j in hemoglobin:
        change_in_hemoglobin=(hemoglobin-newhemoglobin)**2
    distance=np.sqrt(change_in_glucose+change_in_hemoglobin)
    return distance

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
#This function takes five arguments: the new (emoglobin, glucose) point, and the classification, glucose, and hemoglobin data arrays.
#The normalized arrays should be called.
#This function calls the calculateDistanceArray function, and the organizes the data to find the class of the data nearest to the new point.
#The function returns the value of the new point's class.
    distance=calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    min_index = np.argmin(distance)
    nearest_class = classification[min_index]
    return nearest_class
    
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
#This function takes six arguments: an integer, the new (emoglobin, glucose) point, and the classification, glucose, and hemoglobin data arrays.
#The normalized arrays should be called, and k should be odd.
#This function calls the calculateDistanceArray function, and the organizes the data to find the class of the data of the k points nearest to the new point.
#This function calculates the new point's classification, based on which classification appears the most in the k nearest points.
#The function returns the value of the new point's class.
    distance=calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    sorted_indices = np.argsort(distance)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    class_1=0
    class_0=0
    for i in k_classifications:
        if i==0:
            class_0=class_0+1
        else:
            class_1=class_1+1
    if class_1<class_0:
        return 0
    else:
        return 1
    
def graphData(glucose, hemoglobin, classification):
#This function has three arguments: the glucose, hemoglobin, and classification arrays.
#This function graphs each (hemoglobin,glucose) point, showing its classification.
#This function has no return value.
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1, CKD Negative")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0, CKD Positive")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

def graphTestCase (newglucose, newhemoglobin, glucose, hemoglobin, classification, nearest_class):
#This function takes five arguments: new hemoglobin and glucose point, and the glucose, hemoglobin, and classification arrays.
#This function graphs each (hemoglobin,glucose) point, showing its classification, including the new point.
#This function has no return value.
    if nearest_class==0:
        identity="r."
    else:
        identity="k."
    plt.figure()
    plt.plot(newhemoglobin, newglucose,  identity, marker="D",label="Test Case")
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1, CKD Negative")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0, CKD Positive")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    


# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
hemoglobin_scaled, glucose_scaled, classification= normalizeData(glucose, hemoglobin, classification)
newhemoglobin, newglucose=createTestCase()
newhemoglobin_scaled, newglucose_scaled=normalizeTestCase(newglucose, newhemoglobin)

#calls and graphs the nearestNeighborClassifier function for a random point.
nearest_class=nearestNeighborClassifier(newglucose_scaled, newhemoglobin_scaled, glucose_scaled, hemoglobin_scaled, classification)
graphTestCase (newglucose, newhemoglobin, glucose, hemoglobin, classification, nearest_class)

#calls and graphs the kNearestNeighborClassifier function for the same random point.
nearest_class=kNearestNeighborClassifier(3,newglucose_scaled, newhemoglobin_scaled, glucose_scaled, hemoglobin_scaled, classification)
graphTestCase (newglucose, newhemoglobin, glucose, hemoglobin, classification, nearest_class)
