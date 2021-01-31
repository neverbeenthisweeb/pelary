from abc import ABC, abstractmethod


class PredictorInterface(ABC):

    @abstractmethod
    def set_features(self):
        pass

    @abstractmethod
    def predict(self) -> float:
        pass
