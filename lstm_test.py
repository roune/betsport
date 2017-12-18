import tflearn

num_atributes = 90

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