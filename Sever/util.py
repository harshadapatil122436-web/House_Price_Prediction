import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    X_input = np.zeros(len(__data_columns))
    X_input[0] = sqft
    X_input[1] = bath
    X_input[2] = bhk
    if loc_index >= 0:
        X_input[loc_index] = 1
    return round(__model.predict([X_input])[0])

def get_location_names():
    return __location

def load_saved_artifacts():
    print('Loading saved artifacts')
    global __location
    global __data_columns
    global __model

    with open('./artifact/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open('./artifact/House_Prediction.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading artifact saved..... done')
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))