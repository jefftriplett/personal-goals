from invoke import run, task


@task
def push():
    run('cd /Users/jefftriplett/.virtualenvs/personal-goals/src/personal-goals-git')
    run('git checkout master')
    run('git add -A')
    run('git cia -m "push from terminal"')
    run('git push origin master')
    run('open https://github.com/jefftriplett/personal-goals')
