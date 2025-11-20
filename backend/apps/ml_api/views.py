from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
import os
import numpy as np
from tensorflow.keras.models import load_model
import joblib

MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '..', 'ml', 'models')
MODEL_PATH = os.path.abspath(os.path.join(MODEL_DIR, 'demand_lstm.h5'))
SCALER_PATH = os.path.abspath(os.path.join(MODEL_DIR, 'demand_scaler.pkl'))

_model = None
_scaler = None

def load_resources():
    global _model, _scaler
    if _model is None:
        _model = load_model(MODEL_PATH)
    if _scaler is None:
        _scaler = joblib.load(SCALER_PATH)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def predict_demand(request):
    """
    Expect JSON:
    { "history": [list of last seq_len numeric values], "horizon": 7 }
    """
    data = request.data
    history = data.get('history')
    horizon = int(data.get('horizon', 7))
    if not history or not isinstance(history, list):
        return Response({"error":"provide history as list"}, status=400)

    load_resources()
    seq_len = len(history)
    h = np.array(history).reshape(-1,1)
    # scale using scaler
    scaled = _scaler.transform(h).flatten()
    preds = []
    cur = scaled.copy()
    for i in range(horizon):
        x = cur[-seq_len:].reshape(1, seq_len, 1)
        p = _model.predict(x)
        preds.append(float(p.flatten()[0]))
        cur = np.append(cur, p.flatten()[0])

    # inverse scale
    preds = np.array(preds).reshape(-1,1)
    inv = _scaler.inverse_transform(preds).flatten().tolist()
    return Response({"predictions": inv})
