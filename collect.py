"""
Retrieve and process Emojis data.
"""
# Third-party library imports
# pylint: disable=no-value-for-parameter
import click

# Local imports
from helpers.helpers import (
    _start_from_scratch,
    do_maintenance,
    download_all_data,
)


@click.command()
@click.option("-d", "--download", is_flag=True, help="Only download data.")
@click.option("-r", "--reset", is_flag=True, help="Reset to clean slate.")
@do_maintenance
def run(download, reset):
    """Retrieve and process Emojis data."""
    if reset:
        _start_from_scratch()

    if download:
        download_all_data()
        return

    click.secho(
        "You are about to download and process your data.",
        fg="blue",
        bold=True,
    )
    if click.confirm(
        "Are you sure you want to continue?",
        default=False,
        abort=True,
        prompt_suffix=": ",
        show_default=True,
        err=False,
    ):
        if download:
            download_all_data()
        else:
            print("Skip downloading data. Run with `-d` to force download.")


if __name__ == "__main__":
    run()
