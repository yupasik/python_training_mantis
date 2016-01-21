from model.project import Project


class ProjectHelper:

    project_cache = None

    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_page(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.project_name)
        if project.status is not None:
            wd.find_element_by_name("status").send_keys(project.status)
        if project.inheriting is not None and project.inheriting == "False":
            wd.find_element_by_name("inherit_global").click()
        if project.view_status is not None:
            wd.find_element_by_name("status").send_keys(project.view_status)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_new_project(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        self.fill_project_page(project)
        wd.find_element_by_xpath("//div[3]/form/table/tbody/tr[7]/td/input").click()
        self.open_manage_project_page()
        self.project_cache = None

    def delete_project_by_name(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_link_text(project.project_name).click()
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_css_selector("input.button").click()
        self.project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cache = []
            for row in wd.find_elements_by_class_name("row-1"):
                cells = row.find_elements_by_tag_name("td")
                if len(cells) == 5:
                    project_name = cells[0].text
                    status = cells[1].text
                    view_status = cells[3].text
                    desription = cells[4].text
                    self.project_cache.append(Project(project_name=project_name, status=status,
                                                      view_status=view_status, description=desription))
            for row in wd.find_elements_by_class_name("row-2"):
                cells = row.find_elements_by_tag_name("td")
                if len(cells) == 5:
                    project_name = cells[0].text
                    status = cells[1].text
                    view_status = cells[3].text
                    desription = cells[4].text
                    self.project_cache.append(Project(project_name=project_name, status=status,
                                                      view_status=view_status, description=desription))
        return list(self.project_cache)
