from numpy import array

class Agent:

    def __init__(self, nnet, training = False):
        self.nnet = nnet
        self.training = training
        self.records = []
    
    def make_move(self, state):
        X = array(state)
        if self.training:
            # record the game state for traininig
            self.records.append(X)
        values = self.nnet.eval(X)
        return values.argmax()
    
    def clear(self):
        self.records = []
