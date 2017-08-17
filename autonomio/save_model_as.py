def save_model_as(X_num, columns, model, save_model):


    model_json = model.to_json()
    with open(save_model+".json", "w") as json_file:
        json_file.write(model_json)

    model.save_weights(save_model+".h5")
    print("Model" + " " + save_model + " " + "have been saved.")

    k = ""

    f = open(save_model+".x", "w+")


    if type(X_num) is list:
        if type(X_num[0]) is int:
            for x in X_num:
                k = k+columns[x]+" "
        elif type(X_num[0]) is str:
            for x in X_num:
                k = k+str(x)+" "

    elif type(X_num) == int:
        k = str(X_num)
        
    else:
        k = X_num

    f.write(k)
    f.close()
