
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('--csv')
args = parser.parse_args()

if (len(sys.argv) > 1):
#filepath = 'files/features_list.csv' #your path here
    data = np.genfromtxt(args.csv, delimiter=',', dtype='float64')

    scaler = MinMaxScaler(feature_range=[0, 1])
    data_rescaled = scaler.fit_transform(data[1:, 0:8])

    #Fitting the PCA algorithm with our Data
    pca = PCA().fit(data_rescaled)
    #Plotting the Cumulative Summation of the Explained Variance
    plt.figure()
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('Number of Components')
    plt.ylabel('Variance (%)') #for each component
    plt.title('Dataset Explained Variance')
    plt.show()
else:
    print("You must introduce a csv file.")
    print("Try $ python3 pca-components.py --csv='files/features_list.csv'")
