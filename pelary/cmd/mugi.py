import click
from pelary.service.mugi.mugi import Mugi
from pelary.usecase.predictor import Predictor


@click.command()
@click.option('--yoe', required=True)
def predict(yoe):
    mugi = Mugi(yoe)

    predictor_use_case = Predictor(mugi)

    predicted_salary = predictor_use_case.predict()

    print(f"Predicted salary: $ {predicted_salary}")


@click.group("mugi")
def mugi_group():
    pass


mugi_group.add_command(predict)
