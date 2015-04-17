import provmodified as prov
import docker
import json
from pprint import pprint


docker.bind_ns("test", "http://tw.rpi.edu/ns/test#")

image = docker.Image("test:image")
image.set_label("example image")

#activity = prov.Activity("test:activity")
#activity.set_label("example activity")

print(docker.serialize(format="turtle"))

with open('centos.json') as data_file:    
    data = json.load(data_file)
pprint(data)
