# Personal Goals

Personal goals made open source.

Why? Spending the time to get shit done. I'm open sourcing these goals for accessibility across computers I use, transparency, accountability, and versioning.

## Overarching Goals
{% for task in overarching_goals %}
1. {{ task.name }}{% endfor %}

## {{ date.strftime('%B %d, %Y') }}

### Things I'll Do This Week ([Resources](resources.md))
{% for task in this_week %}
- [ ] {{ task.name }}{% endfor %}

### Daily Goals (Repeat)
{% for task in daily %}
- [ ] {{ task.name }}{% endfor %}

### Weekly Goals (Repeat)
{% for task in weekly %}
- [ ] {{ task.name }}{% endfor %}

### Monthly Goals (Repeat)
{% for task in monthly %}
- [ ] {{ task.name }}{% endfor %}

### Quarterly Goals (Repeat)
{% for task in quarterly %}
- [ ] {{ task.name }}{% endfor %}

### Next Week's Focus: :grey_question:

### Things I'll Do In The Future

- [ ] :coffee: Morning :email: and time boxing
- [ ] :guitar: Work through a daily [Ukulele Aerobics](https://www.amazon.com/Ukulele-Aerobics-Levels-Beginner-Advanced/dp/147681306X/?tag=webology0b-20) exercises
- [ ] :mortar_board: [Learn new things](goals/learning.md)
- [ ] :package: [Give Back Box](https://givebackbox.com/index)

## Side Projects & Ideas

- :pencil: [Blog Post Ideas](ideas/blog/README.md)
- :calendar: [Events](content-list/events.md)
- :mortar_board: [Today I Learned (TIL)](til/README.md)
- :movie_camera: [Movies](content-list/movies.md)
- :musical_note: [Music](content-list/music/README.md)
- :open_file_folder: [Apps & Other Projects](ideas/app-ideas.md)
- :thought_balloon: [Ideas](ideas/README.md)
- :tv: [Television](content-list/television.md)

## Inspiration

- Inspired by [Una's](https://github.com/una) [Personal Goals project](https://github.com/una/personal-goals) and her [Una Kravets: Open Sourcing Your Life - Beyond Conf 2015](https://www.youtube.com/watch?v=xQEU0ZsvXYI) talk :muscle: 
- [Katherine's](https://github.com/KatherineMichel) [Personal Goals project](https://github.com/KatherineMichel/personal-goals)
- [Lacey's](https://github.com/williln) [Personal Goals project](https://github.com/williln/personal-goals)
- [Josh Branchaud's TIL](https://github.com/jbranchaud/til) which was inspired by [thoughtbot's TIL project](https://github.com/thoughtbot/til)
