

class DockerContainerManager(object):

    def __init__(self, dockerClient):
        self.client = dockerClient
        self.containers = []
        self.containersToPrintOutputFor = []

    def __enter__(self):
        return self

    def __exit__(self, *_):
        try:
            for container in self.containersToPrintOutputFor:
                print(self.client.logs(container))
        except:
            raise
        finally:
            for container in self.containers:
                self.client.kill(container)
                self.client.remove_container(container)

    def add(self, container, printOutput=False):
        self.containers.append(container)
        if printOutput:
            self.containersToPrintOutputFor.append(container)