import click
from .collision_count import count_collisions_csv


@click.group()
def main():
    """ISCC Benchmarking."""
    pass

@click.command()
@click.argument('reader', required=False)
@click.argument('skip', required=False)
def check_meta_collisions(reader, skip):
    """Calculate collisions in given file."""
    count_collisions_csv()

main.add_command(check_meta_collisions)