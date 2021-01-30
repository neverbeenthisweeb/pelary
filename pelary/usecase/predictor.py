from pelary.service.predictor import PredictorInterface


class Predictor():
    def __init__(self, predictor: PredictorInterface):
        self.predictor = predictor

    def predict(self) -> float:
        return self.predictor.predict()
