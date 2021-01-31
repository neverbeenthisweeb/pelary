import joblib
from pelary.config import Config
from pelary.service.predictor import PredictorInterface


class Mugi(PredictorInterface):
    """
    A predictor that relies on years of experience.

    Attributes:
        yoe (float)
    """

    def __init__(self, config: Config):
        self.ml_model = joblib.load(filename=config.mugi_ml_model_path)

    def set_features(self, yoe: float):
        self.yoe = yoe

    def predict(self) -> float:
        predicted_salary = self.ml_model.predict([[self.yoe]])
        return predicted_salary[0]
