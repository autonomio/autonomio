## Autonomio

EXAMPLE USE: 

	predictions = kuubio(
		             X='text',             # features
		             Y='quality_score',    # indepedent variable
		             data=tweets.head(1000),  # name of dataframe
		             dims=300,             # number of features
		             epoch=20,             # no of training cycles
		             flatten=.3,           # conversion to binary
		             layers=4,             # number of layers in the model
		             dropout=.6,           # rate of dropout for first round
		             neuron_first='auto',  # number of neurons on first layer
		             neuron_last=1,        # number of neurons on last layer
		             batch_size=14,        # numper of samples pass through
		             model='train',        # option to load model
		             loss='binary_crossentropy',  # which model to use
		             save_model=True,      # option to save model
		             verbose=0)            # set 0 for only showing final results
