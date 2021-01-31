import os


class Config:
    def __init__(self):
        self.mugi_ml_model_path = os.getenv(
            "MUGI_ML_MODEL_PATH", "ml_model/mugi.joblib")

    @classmethod
    def instance(cls):
        return cls()
