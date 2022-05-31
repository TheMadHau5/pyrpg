import json

from scene import Scene

datafile = open("data.json", "r")
rawgamedata = json.loads(datafile.read())
datafile.close()

gamedata = {}
start_scene = rawgamedata.pop("start")
cur_scene = None

def open_scene(scene):
	global cur_scene, gamedata
	cur_scene = gamedata.get(scene)

for scene in rawgamedata:
	text = rawgamedata[scene]["text"]
	opts = rawgamedata[scene]["opts"]
	newopts = {}
	for opt in opts:
		newopts[opt] = (lambda sc: lambda: open_scene(sc))(opts[opt])
	gamedata[scene] = Scene(text, newopts)

inventory = []

open_scene(start_scene)

while cur_scene is not None:
	cur_scene.exec()
