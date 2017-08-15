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

	try:
	    X = map(int, temp[0].split())
	except ValueError:
		X = temp[0].split()

	try:
		flatten = int(temp[1])
	except ValueError:
		flatten = temp[1]

	f.close()

	if type(X) == list and len(X) == 1:
		X = X[0]

	return loaded_model, X, flatten

def make_prediction(data, saved_model,  name=False, 
                                        validation=False):

	loaded_model, X, flatten = load_model(saved_model)

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

		predict = predict.sort_values('Value', ascending=False)

		print predict.head(10)
		print ""
		print predict.tail(10)
        
		return predict

	if validation != False:

		if validation == True:
		    n = len(signals) * .5
		else:
		    n = len(signals) * validation

		n = int(n)

		signals = signals[n:]

		predictions = loaded_model.predict(signals)

		return predictions

