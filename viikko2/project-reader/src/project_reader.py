from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)
        tomdeps = parsed_toml['tool']['poetry']['dependencies']
        tomdevdeps = parsed_toml['tool']['poetry']['dev-dependencies']

        dependencies = []
        for t in tomdeps:
            dependencies.append(t)
        devDependencies = []    
        for t in tomdevdeps:
            devDependencies.append(t)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parsed_toml['tool']['poetry']['name'], parsed_toml['tool']['poetry']['description'], dependencies, devDependencies)
