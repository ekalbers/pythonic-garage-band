class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    @staticmethod
    def to_list():
        return Band.instances

    def play_solos(self):
        solos = ()
        for memb in self.members:
            solos += (memb.play_solo(),)
        return solos


class Musician:
    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'{self.role} instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self.role = 'Guitarist'
        self.instrument = 'guitar'
        self.solo = 'face melting guitar solo'


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.role = 'Bassist'
        self.instrument = 'bass'
        self.solo = 'bom bom buh bom'


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.role = 'Drummer'
        self.instrument = 'drums'
        self.solo = 'rattle boom crash'

