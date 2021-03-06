import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

data = open("appledata.csv","r")
reader = csv.reader(data)

X = []
y = []
Xtest = []
ytest = []
count = 0
threshold = int(773 * .7)
for line in reader:
	if (line[1] != "close"):
		t = [float(line[1]), int(line[2])]
		label = line[3]
		if (count < threshold):
			y.append(int(label))
			X.append(t)
		else:
			Xtest.append(t)
			ytest.append(int(label))
		count+=1
		
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X, y)

ypred = []
for k in Xtest:
	ypred.append(clf.predict(k))

print confusion_matrix(ytest, ypred)

print(clf.score(Xtest, ytest))		
		


	
	

