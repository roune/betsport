import tflearn
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split

y_df = data['HTR']
x_df = data.loc[:,data.columns != 'HTR']
y_preprocessed = lenc.fit_transform(np.array(y_df))
X = np.array(x_df.loc[:,[True if c not in  ['Div','Date','HomeTeam','AwayTeam','HTTeam','ATTeam'] else False for c in x_df.columns]])

#parsear y
Y = []
for y in y_preprocessed:
	if y == 0:
		Y.append([1,0,0])
	elif y == 1:
		Y.append([0,1,0])
	else:
		Y.append([0,0,1])
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=10)

num_atributes = X_train.shape[1]

net = tflearn.input_data(shape=[None, 5, num_atributes])
net = tflearn.lstm(net, 512, activation= "leakyrelu", return_seq=False, dropout=0.5)
net = tflearn.fully_connected(net, 3, activation="leakyrelu")
net = tflearn.regression(net, optimizer= "Adam",
                         loss= "categorical_crossentropy", name="output1")
model = tflearn.DNN(net, tensorboard_verbose=2)

# Aqui conseguir la info

model.fit(X_train, Y_train, n_epoch=20, validation_set=0.1, show_metric=True, snapshot_step=100) 

preds = model.predict(X_test)

error = 0.0
for p,y in zip(preds, Y_test):
	if p != y:
		error += 1

print ("Error total = " + str(error / len(Y_test)))