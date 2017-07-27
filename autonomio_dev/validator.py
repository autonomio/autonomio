import numpy as np
import pandas as pd

from keras.models import model_from_json

def validate(	X, Y, 
				X_validate, 
				Y_validate, 
				loss, 
				optimizer,
				verbose):


	json_file = open('saved_model.json', 'r')
	loaded_model = json_file.read()
	json_file.close()

	model = model_from_json(loaded_model)
	model.load_weights('saved_model.h5')

	print "Model is loaded"

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
    
	predictions = model.predict(X_validate)
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
