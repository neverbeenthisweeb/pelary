from abc import ABC, abstractmethod


class PredictorInterface(ABC):

    @abstractmethod
    def predict(self):
        pass
