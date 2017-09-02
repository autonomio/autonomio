def save_model_as(X, columns, model, save_model, flatten):

    '''Model Saver

    WHAT: Saves a trained model so it can be loaded later
    for predictions by predictor().
    '''

    model_json = model.to_json()
    with open(save_model+".json", "w") as json_file:
        json_file.write(model_json)

    model.save_weights(save_model+".h5")
    print("Model" + " " + save_model + " " + "have been saved.")

    temp = ""

    f = open(save_model+".x", "w+")

    # for a range of columns (two ints)
    if type(X) == list:
        if len(X) == 2:
            if type(X[0]) == int:

                for i in range(X[0], X[1]):
                    try:
                        temp += columns[i] + " "
                    except:
                        pass

    # for multiple column index
    if type(X) == list:
        if len(X) > 2:
            if type(X[0]) == int:

                for i in X:
                    temp += columns[i] + " "


    # for multiple column labels
    if type(X) == list:
        if type(X[0]) == str:

            for i in X:
                temp += i+" "

    temp = temp[:-1]

    # for an integer as column name (int)
    if type(X) == int:

        temp = columns[X]

    # for a single column label which contains string values
    if type(X) == str:

        temp = X

    temp += " "+str(flatten)

    f.write(temp)
    f.close()
