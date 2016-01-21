from model.project import Project
import random


def test_del_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.add_new_project(Project(project_name="test"))
    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project)
    old_projects.remove(project)
    new_projects = app.soap.get_project_list()
    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)
