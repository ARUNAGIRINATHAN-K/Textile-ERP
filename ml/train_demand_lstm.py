"""
Simple LSTM demand forecast training script.
Assumes you have a CSV with columns: date, demand
Saves model to ml/models/demand_lstm.h5 and scaler to ml/models/demand_scaler.pkl
"""
import os
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
import joblib

DATA_PATH = "ml/data/demand.csv"
MODEL_DIR = "ml/models"
os.makedirs(MODEL_DIR, exist_ok=True)

def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=['date'])
    df = df.sort_values('date')
    series = df['demand'].astype(float).values
    return series

def create_sequences(data, seq_len=30):
    X, y = [], []
    for i in range(len(data) - seq_len):
        X.append(data[i:i+seq_len])
        y.append(data[i+seq_len])
    X = np.array(X)
    y = np.array(y)
    return X, y

def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(64, input_shape=input_shape, return_sequences=False))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def main():
    seq_len = 30
    data = load_data().reshape(-1,1)
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data).flatten()

    X, y = create_sequences(data_scaled, seq_len)

    X = X.reshape((X.shape[0], X.shape[1], 1))

    model = build_model((seq_len, 1))
    es = EarlyStopping(patience=5, restore_best_weights=True)

    model.fit(X, y, epochs=100, batch_size=16, validation_split=0.1, callbacks=[es])

    model.save(os.path.join(MODEL_DIR, 'demand_lstm.h5'))
    joblib.dump(scaler, os.path.join(MODEL_DIR, 'demand_scaler.pkl'))
    print("Saved model and scaler to", MODEL_DIR)

if __name__ == '__main__':
    main()
