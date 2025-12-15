def predict_failure(engine_temp, rpm, battery):
    risk = 0
    if engine_temp > 95:
        risk += 30
    if rpm > 2800:
        risk += 30
    if battery < 12.0:
        risk += 20
    return min(risk + 20, 100)
