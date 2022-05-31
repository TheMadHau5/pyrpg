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

