import numpy as np
import pandas as pd
from random import shuffle

from keras.models import model_from_json

from transform_data import transform_data
from prediction import make_prediction, load_model

def validate(	Y,
				data,
				validation,
				loss,
				optimizer,
				verbose,
				save_model,
				flatten,
				dims):

	model, X = load_model(save_model)
	X,Y = transform_data(X,Y,data,flatten,dims)

	shuffle(X)

	if validation != True:
		n = len(X) * validation
		n = int(n)

	if validation == True:
		n = len(X) * .5
		n = int(n)

	X_validate = X[n:]
	Y_validate = Y[n:]
	X = X[:n]
	Y = Y[:n]

	a = len(X)
	b = len(X_validate)

	#separating data for train 67% and test 33%
	s = int(round(.67 * a))

	X_train = X[:s]
	Y_train = Y[:s]

	X_test = X[s:]
	Y_test = Y[s:]

	model.compile(  loss=loss, 
                	optimizer=optimizer, 
                    metrics=['accuracy'])

	#getting scores and predictions
	train_scores = model.evaluate(X_train, Y_train, verbose=verbose)
	test_scores = model.evaluate(X_test, Y_test, verbose=verbose)
    
	predictions = make_prediction(data, save_model, dims, validation)
	rounded = [round(x[0]) for x in predictions]

	df1 = pd.DataFrame(rounded)
	df2 = pd.DataFrame(Y_validate)

	#0 or 1 if the prediction mathes with output
	l = np.array(df1 == df2)
	l = l.astype(int)

	x = 0

	for i in range(b):
		if l[i] == 1:
			x += 1.0

	p = x / len(rounded)

	return train_scores, test_scores, p
