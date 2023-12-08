class GameInfo:

    def __init__(self):
        self._game_id = None
        self._draws = None

    @property
    def game_id(self):
        return self._game_id
    
    @game_id.setter
    def game_id(self, id):
        self._game_id = id

    @property
    def draws(self):
        return self._draws
    
    @draws.setter
    def draws(self, draws):
        self._draws = draws