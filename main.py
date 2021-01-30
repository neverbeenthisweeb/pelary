import click

from pelary.cmd.mugi import mugi_group


@click.group()
def main_group():
    pass


main_group.add_command(mugi_group)

if __name__ == "__main__":
    main_group()
