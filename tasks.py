import click
import frontmatter
import jinja2
import maya

from click_default_group import DefaultGroup
from datetime import date, datetime
from math import ceil
from pathlib import Path
from yaml import load


ACCOMPLISHMENT_TEMPLATE = Path('templates', 'accomplishments', 'weekly.md')
DEFAULT_COMMAND = 'accomplishment'
OUTPUT_FOLDER = Path('accomplishments', '{year}')
TASKS_DATA = Path('data', 'tasks.yml')


@click.group(cls=DefaultGroup, default=DEFAULT_COMMAND, default_if_no_args=True)
@click.version_option()
def cli():
    """
    Screenshot!
    """


@cli.command()
def add(name):
    pass


@cli.command()
@click.argument('date')
@click.argument('theme')
@click.option('--overwrite/--no-overwrite', default=False)
def accomplishment(date, theme, overwrite):
    parsed_date = maya.when(date, timezone='US/Central').datetime(naive=True)

    day_of_month = parsed_date.day
    week_number = (day_of_month - 1) // 7 + 1

    output_filename = '{year}-{month:02}-week{week_number}.md'.format(
        year=parsed_date.year,
        month=parsed_date.month,
        week_number=week_number)

    output_filename = Path(str(OUTPUT_FOLDER.joinpath(output_filename)).format(
        year=parsed_date.year
    ))

    click.echo(str(output_filename))

    if not output_filename.parent.exists():
        output_filename.parent.mkdir()

    with open(TASKS_DATA) as input_yaml:
        data = load(input_yaml.read())

    context_data = data.copy()
    context_data['date'] = parsed_date
    context_data['theme'] = theme

    intput_filename = ACCOMPLISHMENT_TEMPLATE

    with open(intput_filename) as input_buffer:
        post = frontmatter.load(input_buffer)

    t = jinja2.Template(post.content)
    contents = t.render(context_data)

    if not output_filename.exists() or overwrite:
        output_filename.write_text(contents)


@cli.command()
def post():
    now = datetime.now()
    click.echo(now)

    dt = datetime.now()
    first_day = dt.replace(day=1)
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()

    day_of_week = now.weekday()
    if day_of_week == 0:
        # do nothing
        pass
    else:
        pass

    click.echo(day_of_week)
    click.echo(7 - day_of_week)
    click.echo(int(ceil(adjusted_dom / 7.0)))
    click.echo(date.strftime(now, '%Y-%m-week'))


@cli.command()
def push():
    pass

    """
    run('cd /Users/jefftriplett/.virtualenvs/personal-goals/src/personal-goals-git')
    run('git checkout master')
    run('git add -A')
    run('git cia -m "push from terminal"')
    run('git push origin master')
    run('open https://github.com/jefftriplett/personal-goals')
    """


if __name__ == '__main__':
    cli()
