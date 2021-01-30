from pelary.service.predictor import PredictorInterface


class Mugi(PredictorInterface):
    """
    A predictor that relies on job's title and industry.

    Attributes:
        job_title (str)
        industry (str)
    """

    def __init__(self, job_title: str, industry: str) -> None:
        self.job_title = job_title
        self.industry = industry

    def predict(self) -> float:
        # TODO: Improve Mugi implementation.
        predicted_salary = float(0)
        return predicted_salary
