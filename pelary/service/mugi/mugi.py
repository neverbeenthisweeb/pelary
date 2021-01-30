from pelary.service.predictor import PredictorInterface


class Mugi(PredictorInterface):
    """
    A predictor that relies on years of experience.

    Attributes:
        yoe (float)
    """

    def __init__(self, yoe: float) -> None:
        self.yoe = yoe

    def predict(self) -> float:
        # TODO: Improve Mugi implementation.
        predicted_salary = float(0)
        return predicted_salary
