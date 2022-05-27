cur_scene = None
inventory = []

class Scene:
    text = None
    opts = None

    @classmethod
    def exec(cls):
        print(cls.text)
        keys = cls.opts.keys()
        print("You can: " + ', '.join(keys))
        cmd = input("What do you do? ").strip()
        while cmd not in keys:
            cmd = input("That is not an option. What do you do? ").strip()
        fn = cls.opts.get(cmd)
        fn()
        print()

class Introduction(Scene):
    text = "You find yourself trapped in a dungeon inside a castle which seems to be owned by YOUR MOM. How do you escape?"
    
    def open_door():
        global cur_scene, inventory
        if 'key' in inventory:
            cur_scene = None
            print("you escaped!")
        else:
            print("the door was locked you stoopid")
    
    def search_cabinet():
        global inventory
        inventory.append('key')
        print("found key!")
        
    def commit_die():
        global cur_scene
        cur_scene = None
        print("ok")

    opts = {
        'open door': open_door,
        'search cabinet': search_cabinet,
        'commit die': commit_die
    }

cur_scene = Introduction

while cur_scene is not None:
    cur_scene.exec()
