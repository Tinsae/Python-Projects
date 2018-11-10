    
import pandas as pd
import numpy as np 
    
data = pd.read_csv("breast_cancer.csv")
        
data1 = data['radius_mean'].values.reshape(len(data),1)
data2 = data['texture_mean'].values.reshape(len(data),1)
data3 = data['area_mean'].values.reshape(len(data),1)
data4 = data['smoothness_mean'].values.reshape(len(data),1)
data5 = data['perimeter_mean'].values.reshape(len(data),1)

def z_score(X, x):
    return (x-X.mean())/X.std()
    
data1_new = [z_score(data1,data1[i]) for i in range(len(data1))]
##data2_new = [z_score(data1,data1[i]) for i in range(len(data2))]
##data3_new = [z_score(data1,data1[i]) for i in range(len(data3))]
##data4_new = [z_score(data1,data1[i]) for i in range(len(data4))]
##data5_new = [z_score(data1,data1[i]) for i in range(len(data5))]

##dataset = np.hstack((data1_new, data2_new, data3_new, data4_new, data5_new))
                    
def mydistance(v1, v2):
    d = 0 
    for i in range(len(v1)):
        d += (v1[i]-v2[i])**2
    return np.sqrt(d)
    
str_arr = input("Please enter the values, seperated by commas, ofthe vector") 
str_arr = str_arr.split(',')
topredict = np.array([int(num) for num in str_arr])
predict = [z_score(topredict, topredict[i]) for i in range(len(topredict))]
print(predict)
