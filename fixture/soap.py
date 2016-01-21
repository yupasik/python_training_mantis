from suds.client import Client
from suds import WebFault
from fixture.project import Project


class SoapHelper:

    project_cache = None

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        self.project_cache =[]
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible(self.app.config["webadmin"]["username"],
                                                                  self.app.config["webadmin"]["password"])
        for project in projects:
            self.project_cache.append(Project(project_name=project["name"],
                                              status=project["status"]["name"],
                                              view_status=project["view_state"]["name"],
                                              description=project["description"]))
        return list(self.project_cache)