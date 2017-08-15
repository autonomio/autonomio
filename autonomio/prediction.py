import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
from vectorize_text import vectorize_text
from transform_data import transform_data

def load_model(saved_model):

	json_file = open(saved_model + ".json", 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
	loaded_model.load_weights(saved_model + '.h5')
	print("Loaded model from disk")

	f = open(saved_model+".x", 'r')
	temp = f.read()
	temp = temp.split(",")

	f.close()

	try:
	    X = map(int, temp[0].split())
	except ValueError:
		X = temp[0].split()

	try:
		flatten = int(temp[1])
	except ValueError:
		flatten = temp[1]

	Y_unique = int(temp[2])

	if type(X) == list and len(X) == 1:
		X = X[0]

	return loaded_model, X, flatten, Y_unique

def make_prediction(data, saved_model,  name=False, 
                                        validation=False):

	loaded_model, X, flatten, Y_unique = load_model(saved_model)


	signals = transform_data(data, flatten, X)

	if validation == False:

		predict = loaded_model.predict(signals)

		if name != False:
			name = data[name]

			l = []
			i = 0

			for x in predict:
				l.append([x[0], name[i:i+1].values[0]])
				i += 1

			predict = pd.DataFrame(l)
			predict.columns = ['Value', 'Name']

		else:
			predict = pd.DataFrame(predict)

		if Y_unique == 2 or Y_unique == 1:
			for i in range(len(signals)):
				predict.Value[i] = predict.Value[i] >= .5

			predict.Value.astype(int)

		check = []
		for i in range(len(predict)):
			check.append(round(predict.Value[i], 2))

		predict = predict.sort_values('Value', ascending=False)	

		print predict.head(10)
		print ""
		print predict.tail(10)

		if len(set(check)) == 1:
			print "\n NB! All predictions have the same value \n"

		return predict

	if validation != False:

		if validation == True:
		    n = len(signals) * .5
		else:
		    n = len(signals) * validation

		n = int(n)

		signals = signals[n:]

		predict = loaded_model.predict(signals)

		if Y_unique == 2 or Y_unique == 1:
			for i in range(len(signals)):
				predict[i] = predict[i] >= .5

		check = []
		for i in range(len(predict)):
			check.append(round(predict[i], 2))

		if len(set(check)) == 1:
			print "\n NB! All predictions have the same value \n"

		return predict

