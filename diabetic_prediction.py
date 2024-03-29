import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df=pd.read_csv('/content/diabetes.csv')
df.head()

df.describe()

df.shape

df['Outcome'].value_counts()

df.groupby('Outcome').mean()

x=df.drop(columns='Outcome',axis=1)

y=df['Outcome']

print(x)
print(y)

scaler=StandardScaler()
scaler.fit(x)

standardized_data=scaler.transform(x)

print(standardized_data)

x=standardized_data
y= df['Outcome']
print(x)
print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)

print(x.shape,x_train.shape,x_test.shape)

classifier = svm.SVC(kernel='linear')

classifier.fit(x_train,y_train)

x_train_prediction=classifier.predict(x_train)

xtrainscore=accuracy_score(x_train_prediction,y_train)

print(xtrainscore)

xtestp=classifier.predict(x_test)

xtestscore=accuracy_score(xtestp,y_test)

print(xtestscore)

input_data = (8,99,84,0,0,35.4,0.388,50)
id_as_array=np.asarray(input_data)
input_data_reshaped=id_as_array.reshape(1,-1)
std_data = scaler.transform(input_data_reshaped)
print(std_data)
predict=classifier.predict(std_data)
print(predict)
if(predict==0):
  print("not diabetic")
else:
  print(" diabetic")

