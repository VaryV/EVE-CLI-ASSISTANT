import click

# from eve.service import svc_github
import pyttsx3
import os
import requests
from pprint import pprint


def female_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    engine.setProperty("volume", 1)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()


@click.group()
def cli():
    """- Github commands"""


@cli.command()
@click.argument("name", type=str)
@click.option("-p", "--private", type=bool, help="is a provate repo?", default=False)
def create(name, private):
    """- Create a Github repository"""
    API_URL = "https://api.github.com"

    if private == True:
        payload = '{"name": "' + name + '", "private": "True"}'
    if private == False:
        payload = '{"name": "' + name + '"}'
    click.echo(payload)
    headers = {
        "Authorization": "token " + os.environ.get("GITHUB_TOKEN"),
        "Accept": "application/vnd.github.v3+json",
    }
    click.echo(headers)
    try:
        r = requests.post(API_URL + "/user/repos", data=payload, headers=headers)
        # pprint(r.json())
        click.echo(
            f"Repository has been created in the name of '{name}' at 'https://github.com/VaryV/{name}'"
        )
        click.echo("Run the below command to add the remote repository as origin")
        click.echo(f"git remote add origin git@github.com/VaryV/{name}.git")
        female_speak(f"Repository has been created in the name of {name}")
    except requests.exceptions.RequestException as error:
        click.echo(f"Encountered {error}")
        female_speak(f"Encountered {error}")


@cli.command()
@click.argument("name", type=str)
def delete(name):
    """- Delete a Github repository"""
    API_URL = "https://api.github.com"
    payload = '{"name": "' + name + '"}'
    headers = {
        "Authorization": "token " + os.environ.get("GITHUB_TOKEN"),
        "Accept": "application/vnd.github.v3+json",
    }
    try:
        r = requests.delete(
            API_URL + "/repos/VaryV/" + name, data=payload, headers=headers
        )
        # pprint(r.json())
        click.echo(f"Deleted repository in the name of {name}")
        female_speak(f"Deleted repository in the name of {name}")
    except requests.exceptions.RequestException as error:
        click.echo(f"Encountered {error}")
        female_speak(f"Encountered {error}")


# class Context:
#     def __init__(self):
#         self.github = svc_github.GithubUtility()


# @click.group()
# @click.pass_context
# def cli(ctx):
#     """- Github commands"""
#     ctx.obj = Context()


# @cli.command()
# @click.argument("name", type=str)
# @click.option("-p", "--private", type=bool, help="is a provate repo?", default=False)
# @click.pass_context
# def create(ctx, name, private):
#     """- create a github repository"""
#     repo = ctx.obj.github.create_repo(name, private=private)
#     click.echo(f"Created {repo.name} at {repo.html_url}")
#     female_speak(f"Created {repo.name} at the given url")
#     click.echo(f"Run the below command to add repo as a remote...")
#     female_speak(f"Run the below command to add repository as a remote...")
#     click.echo(f"git remote add origin {repo.clone_url}")


# @cli.command()
# @click.argument("name", type=str)
# @click.pass_context
# def delete(ctx, name):
#     """- delete a github repository"""
#     repo = ctx.obj.github.get_repo(name)
#     ctx.obj.github.delete_repo(repo.name)
#     click.echo(f"Deleted {repo.name} ")
#     female_speak(f"Deleted {repo.name} ")
