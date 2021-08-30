import os
import click
import requests
import json
from pprint import pprint
import pyttsx3


def female_speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',200)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


@click.command()
@click.argument("project_name", type=str, required=True)
@click.argument("text_editor", type=str, default="vsc")
def cli(project_name, text_editor):
    '''- Create your Project'''
    click.echo(f"Navigating to your projects directory {os.environ.get('ProjectsDir')} ...")
    os.chdir(f'{os.environ.get("ProjectsDir")}')
    click.echo(f"Changed working directory to {os.getcwd()}")
    click.echo(f"Creating project folder '{project_name}' ...")
    try:
        os.mkdir(f'{project_name}')
        click.echo("Project directory created.")
        click.echo(f"Navigating to '{os.getcwd()}\\{project_name}' ...")
        os.chdir(f"{os.getcwd()}\\{project_name}")        
        click.echo("Initializing Git Repository...")
        os.system("git init")
        click.echo("Created Git Repository")
        API_URL = "https://api.github.com"
        payload = '{"name": "' + project_name + '", "private": "True"}'
        headers = {
            "Authorization": "token " + os.environ.get("GITHUB_TOKEN"),
            "Accept": "application/vnd.github.v3+json"
        }
        try:
            r = requests.post(API_URL + "/user/repos", data=payload, headers=headers)
            # pprint(r.json())
            click.echo(f"Repository has been created on Github in the name of {project_name}")
            click.echo("Copying remote...")
            os.system(f"git remote add origin git@github.com:VaryV/{project_name}.git")
            click.echo("Added remote")
            click.echo("Creating README.md ...")
            os.system("touch README.md")
            click.echo("Created README.md file")
            click.echo("Performing first add and commit")
            os.system("git add .")
            os.system('git commit -m "Initial Commit"')
            if text_editor == "vsc":
                click.echo(f"{project_name} has been created successfully. Opening up project in Visual Studio Code")
                female_speak(f"{project_name} has been created successfully. Opening up project in Visual Studio Code")
                os.system("code .")
            if text_editor == "sub":
                click.echo(f"{project_name} has been created successfully. Opening up project in Sublime Text 3")
                female_speak(f"{project_name} has been created successfully. Opening up project in Sublime Text 3")
                os.system("Sublime3 .")
            if text_editor == "atom":
                click.echo(f"{project_name} has been created successfully. Opening up project in Atom")
                female_speak(f"{project_name} has been created successfully. Opening up project in Atom")
                os.system("atom .")
            

        except requests.exceptions.RequestException as error:
            click.echo(f"Encountered: {error}")
            female_speak(f"Encountered {error}")
        
        
        
    except FileExistsError as error:
        click.echo(f"Encountered: {error}")
        female_speak(f"Encountered: {error}")