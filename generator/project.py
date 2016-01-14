from model.project import Project
import random
import string
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 10
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

status_values = ["development", "release", "stable", "obsolete"]
view_status_values = ["public", "private"]
inherit_global_categories_values = ["True", "False"]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(project_name=random_string("project_name", 10),
                    status=random.choice(status_values),
                    inheriting=random.choice(inherit_global_categories_values),
                    view_status=random.choice(view_status_values),
                    description=random_string("description", 10)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
