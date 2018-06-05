def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)
        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []
    temp = []

    ### your code goes here
    numPredictions = len(predictions)

    for i in range(numPredictions):
		resError = (predictions[i] - net_worths[i])**2
		tup = (ages[i], net_worths[i], resError)
		temp.append(tup)

    temp.sort(key=lambda tup: tup[2],reverse=True)
    cleaned_data = temp[int(len(temp)*0.1):]

    return cleaned_data

