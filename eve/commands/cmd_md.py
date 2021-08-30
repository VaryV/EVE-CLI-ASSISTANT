import click
import webbrowser
from eve.config import physics_md, chemistry_md, english_md, cs_md, maths_md

@click.command()
@click.argument("sub", type=str, required=True)
def cli(sub):
    """- Open master drive"""
    if sub.lower() == "phy":
        url = physics_md
    elif sub.lower() == "chem":
        url = chemistry_md
    elif sub.lower() == "maths":
        url = maths_md
    elif sub.lower() == "cs":
        url = cs_md
    elif sub.lower() == "eng":
        url = english_md

    webbrowser.open(url)
