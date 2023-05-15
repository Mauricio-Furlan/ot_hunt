


from utils import move_and_click


class HandlerPoke:
    def __init__(self):
        self.count = 0
        self.list_poke = [(21, 799), (22, 838), (20, 886), (22, 922), (23, 966), (13,1012)]

    def check_poke_lenght(self):
        self.count = self.count % len(self.list_poke) # garante 0-5

    def next(self):
        self.count += 1
        self.check_poke_lenght()
        move_and_click(self.list_poke[self.count], 'right')

    def previous(self):
        self.count -= 1
        self.check_poke_lenght()
        move_and_click(self.list_poke[self.count], 'right')


