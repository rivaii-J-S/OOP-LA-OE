print("SUMAYLO-BSIT2B-OE3")

class SMA:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def login(self):
        pass
    def post(self):
        pass
class Insta(SMA):
    def __init__(self, username, password, num_follow):
        super().__init__(username, password)
        self.num_follw = num_follow
    
    def shr_story(self):
        pass
class Twitter(SMA):
    def __init__(self, username, password, num_twi):
        super().__init__(username, password)
        self.num_twi = num_twi
        

    def tweet(self):
        pass


