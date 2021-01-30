import click
from pelary.service.predictor.mugi import Mugi


@click.command()
@click.option('--job-title', required=True)
@click.option('--industry', required=True)
def predict(job_title, industry):
    mugi = Mugi(job_title, industry)
    predicted_salary = mugi.predict()
    print(predicted_salary)


@click.group("mugi")
def mugi_group():
    pass


mugi_group.add_command(predict)
