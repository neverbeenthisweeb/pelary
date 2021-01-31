import click
from pelary.config import Config
from pelary.service.mugi.mugi import Mugi
from pelary.usecase.predictor import Predictor


@click.command()
@click.option('--yoe', required=True, type=float)
def predict(yoe):
    config = Config.instance()

    mugi = Mugi(config)
    mugi.set_features(yoe)

    predictor_use_case = Predictor(mugi)

    predicted_salary = predictor_use_case.predict()

    print(f"Predicted salary: $ {predicted_salary}")


@click.group("mugi")
def mugi_group():
    pass


mugi_group.add_command(predict)
