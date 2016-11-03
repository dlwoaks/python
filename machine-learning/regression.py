import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low'])/df['Adj. Close'] * 100
df['PCT_Change'] = (df['Adj. Open'] - df['Adj. Close'])/df['Adj. Close'] * 100

df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

# change forecast_col to whatever you want it to be in the future
forecast_col = 'Adj. Close'
# you cant work with NaN data, fill NaN with invalid data rather than getting rid of data
df.fillna(-99999, inplace=True)
# suppose 0.1*len(df) returns 0.2, math.ceil returns 1.0, cast to int
# trying to predict out 10% of the data frame
forecast_out = int(math.ceil(0.01*len(df)))
# we have our features, now we need labels

#shifting the columns negatively [up the spreadsheet]
#so label column for each row will be adj. close price 10 percent into the future
df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)
'''
X = features, y = label/forecasts.
df.drop(['label'],1) takes the data of every column except for label
df['label'] data of label column
'''
X = np.array(df.drop(['label'],1))
y = np.array(df['label'])
# need to scale X
# however need to scale new values alongside other values (would skip this step with
# high frequency trading)
X = preprocessing.scale(X)



# only using 20% of our testing data
# take our features and labels, shuffle them up (keeping x and y connected)
# and outputs for X_train, y_train, X_test, y_test
# X_train, y_train used to fit or train our classifiers
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
clf = LinearRegression()
'''
LinearRegression() === LinearRegression(n_jobs=1). means it trains dataset 1 time, making
our accuracy vary more.
n_jobs=10 trains 10 times
n_jobs=-1 trains as many times as possible
'''
clf.fit(X_train, y_train)
# score is synonymous with test
clf.score(X_test, y_test)
# why do u wanna train and test on seperate data?
# X is data machine has already seen (machine already knows answers to X
accuracy = clf.score(X_test, y_test)
# accuracy/confidence of/in score
print(accuracy)
# accuracy = (error)^2
# doesn't mean complete accuracy, more like directionally accurate

''' now what if we wanted to use a different algorithm?
replace clf = LinearRegression() with 
clf = svm.SVR()... THAT SIMPLE
{can use clf = svm.SVR(kernel='poly')} what's a kernel??
svm.SVR() returns 50%~65% accuracy.. clearly not the algorithm to use
'''
