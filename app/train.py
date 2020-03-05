numIters = 100
numEps = 10
competeEps = 1000
threshold = 0.55
height = 11
width = 11
player_cnt = 8

from AlphaNNet import AlphaNNet
from game import Game
from agent import Agent

# https://web.stanford.edu/~surag/posts/alphazero.html
def train(nnet):
    # for training, all agents uses the same nnet
    # unless we want to use a evolution algorithm
    agents = [Agent(nnet, training = True) for _ in range(player_cnt)]
    for i in range(numIters):
        X = []
        Y = []
        # the loop below can use distributed computing
        for e in range(numEps):
            # collect examples from a new game
            g = Game(height, width, player_cnt)
            winner_id = g.run(agents)
            for i in range(len(agents)):
                X += agent.record
                if i == winner_id:
                    base = 1/len(agent.record)
                    Y += [base*gamma for gamma in range(1, len(agent.record) + 1)]
                else:
                    base = -1/len(agent.record)
                    Y += [base*gamma for gamma in range(1, len(agent.record) + 1)]
                agent.clear()
        new_nnet = nnet.copy()
        new_nnet.fit(X, Y)
        # compare new net with previous net
        frac_win = compete(new_nnet, nnet)
        if frac_win > threshold:
            # replace with new net
            nnet = new_nnet
            print("Iteration", i, "is now the new champion!")
        else:
            print("Iteration", i, "failed to beat the previouse one.")
    return nnet

def compete(nnet1, nnet2):
    agents = [None] * player_cnt
    sep = player_cnt//2
    for i in range(sep):
        agents[i] = Agent(nnet1)
    for i in range(sep, player_cnt):
        agents[i] = Agent(nnet2)
    wins = 0
    for _ in range(competeEps):
        g = Game(height, width, player_cnt)
        if g.run(agents) < sep:
            wins += 1
    return win/competeEps

if __name__ == '__main__':
    nnet = AlphaNNet()
    num = 0
    while 1:
        num += 1
        nnet = train(nnet)
        # need to store the nnet
        nnet.save("Network No." + str(num))
