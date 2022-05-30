import json

class Scene:
	def __init__(self, text, opts):
		self.text = text
		self.opts = opts

	def exec(self):
		print(self.text)
		keys = self.opts.keys()
		print("You can: " + ', '.join(keys))
		cmd = input("What do you do? ").strip()
		while cmd not in keys:
			cmd = input("That is not an option. What do you do? ").strip()
		fn = self.opts.get(cmd)
		fn()
		print()

datafile = open("data.json", "r")
rawgamedata = json.loads(datafile.read())
datafile.close()

gamedata = {}
start_scene = rawgamedata.pop("start")
cur_scene = None

def open_scene(scene):
	global cur_scene, gamedata
	cur_scene = gamedata[scene]

for scene in rawgamedata:
	text = rawgamedata[scene]["text"]
	opts = rawgamedata[scene]["opts"]
	newopts = {}
	for opt in opts:
		newopts[opt] = lambda: open_scene(opts[opt])
	gamedata[scene] = Scene(text, newopts)

inventory = []

class Introduction(Scene):	
	def open_door(self):
		global cur_scene, inventory
		if 'key' in inventory:
			cur_scene = None
			print("you escaped!")
		else:
			print("the door was locked you stoopid")
	
	def search_cabinet(self):
		global inventory
		inventory.append('key')
		print("found key!")
	
	def commit_die(self):
		global cur_scene
		cur_scene = None
		print("ok")

	def __init__(self):
		self.text = "You find yourself trapped in a dungeon inside a castle which seems to be owned by YOUR MOM. How do you escape?"
		self.opts = {
			'open door': self.open_door,
			'search cabinet': self.search_cabinet,
			'commit die': self.commit_die
		}


open_scene(start_scene)

while cur_scene is not None:
	cur_scene.exec()
