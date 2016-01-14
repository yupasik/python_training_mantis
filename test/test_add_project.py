from model.project import Project


def test_add_project(app, json_projects):
    project = json_projects
    old_projects = app.project.get_project_list()
    app.project.add_new_project(project)
    old_projects.append(project)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)
