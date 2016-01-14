# -*- coding: utf-8 -*-
from sys import maxsize


class Project:

    def __init__(self, project_name=None, status=None, inheriting=None, view_status=None, description=None, id=None):
        self.project_name = project_name
        self.status = status
        self.inheriting = inheriting
        self.view_status = view_status
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.project_name,
                                   self.status, self.inheriting,
                                   self.view_status, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.project_name == other.project_name

    def name(self):
        return self.project_name

