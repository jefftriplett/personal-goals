from invoke import run, task


@task
def deploy():
    run('cd ~/.virtualenvs/presonal-goals/src/personal-goals')
    run('git checkout master')
    run('git add -A')
    run('git cia -m "push from terminal"')
    run('git push origin master')
    run('open https://github.com/jefftriplett/personal-goals')
