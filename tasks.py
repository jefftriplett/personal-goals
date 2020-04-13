import frontmatter
import jinja2
import maya
import typer
import yaml

from datetime import date, datetime
from math import ceil
from pathlib import Path


ACCOMPLISHMENT_TEMPLATE = Path("templates", "weekly.md")
DEFAULT_COMMAND = "accomplishment"
OUTPUT_FOLDER = Path("accomplishments", "{year}")
TASKS_DATA = Path("data", "tasks.yml")


app = typer.Typer()


@app.command()
def accomplishment(date: str = "now", theme: str = "", overwrite: bool = False):
    parsed_date = maya.when(date, timezone="US/Central").datetime(naive=True)

    day_of_month = parsed_date.day
    week_number = (day_of_month - 1) // 7 + 1

    output_filename = f"{parsed_date.year}-{parsed_date.month:02}-week{week_number}.md"
    output_filename = Path(
        str(OUTPUT_FOLDER.joinpath(output_filename)).format(year=parsed_date.year)
    )

    typer.echo(str(output_filename))

    if not output_filename.parent.exists():
        output_filename.parent.mkdir()

    if TASKS_DATA.exists():
        data = yaml.load(TASKS_DATA.read_text(), Loader=yaml.FullLoader)
    else:
        data = dict()

    context_data = data.copy()
    context_data["date"] = parsed_date
    context_data["theme"] = theme

    post = frontmatter.loads(ACCOMPLISHMENT_TEMPLATE.read_text())

    t = jinja2.Template(post.content)
    contents = t.render(context_data)

    post["date"] = parsed_date
    post.content = contents

    if not output_filename.exists() or overwrite:
        output_filename.write_text(frontmatter.dumps(post))


if __name__ == "__main__":
    app()
