import itertools
from collections import defaultdict

class Program(object):
    def __init__(self, pid, program_file, input):
        self.P = defaultdict(int)
        for i,x in enumerate(open(program_file).read().split(',')):
            self.P[i] = int(x)
        self.input = input
        self.ip = 0
        self.pid = pid
        self.rel_base = 0
    def idx(self, i, I):
        mode = (0 if i>=len(I) else I[i])
        val = self.P[self.ip+1+i]
        if mode == 0:
            pass # no-op
        elif mode == 2:
            val = val+self.rel_base
        else:
            assert False, mode
        return val
    def val(self, i, I):
        mode = (0 if i>=len(I) else I[i])
        val = self.P[self.ip+1+i]
        if mode == 0:
            val = self.P[val]
        elif mode == 2:
            val = self.P[val+self.rel_base]
        return val
    def run_all(self):
        ans = []
        while True:
            val = self.run()
            if val == None:
                return ans
            ans.append(val)

    def run(self):
        """Return next output"""
        while True:
            cmd = str(self.P[self.ip])
            opcode = int(cmd[-2:])
            print(cmd, self.ip)
            I = list(reversed([int(x) for x in cmd[:-2]]))
            if opcode == 1:
                i1,i2 = self.val(0,I),self.val(1,I)
                self.P[self.idx(2, I)] = self.val(0, I) + self.val(1, I)
                self.ip += 4
            elif opcode == 2:
                i1,i2 = self.val(0,I),self.val(1,I)
                self.P[self.idx(2, I)] = self.val(0, I) * self.val(1, I)
                self.ip += 4
            elif opcode == 3:
                inp = self.input()
                self.P[self.idx(0, I)] = inp #self.Q[0]
                #self.Q.pop(0)
                self.ip += 2
            elif opcode == 4:
                ans = self.val(0, I)
                self.ip += 2
                return ans
            elif opcode == 5:
                self.ip = self.val(1, I) if self.val(0, I)!=0 else self.ip+3
            elif opcode == 6:
                self.ip = self.val(1, I) if self.val(0, I)==0 else self.ip+3
            elif opcode == 7:
                self.P[self.idx(2, I)] = (1 if self.val(0,I) < self.val(1,I) else 0)
                self.ip += 4
            elif opcode == 8:
                self.P[self.idx(2, I)] = (1 if self.val(0,I) == self.val(1,I) else 0)
                self.ip += 4
            elif opcode == 9:
                self.rel_base += self.val(0, I)
                self.ip += 2
            else:
                assert opcode == 99, opcode
                return None

R = 30
C = 100
G = [[0 for _ in range(C)] for _ in range(R)]
r,c = R//2,C//2
G[r][c] = 1
d = 0
DR = [-1,0,1,0]
DC = [0,1,0,-1]
def get_color():
    return G[r][c]

painted = set()
P = Program('0', '11.in', get_color)
cn = 0
while True:
    color = P.run()
    if color == None:
        break
    print(color)
    cn += 1
    if cn == 3:
        exit(-1)
    assert r>=0
    assert c>=0
    G[r][c] = color
    painted.add((r,c))
    turn = P.run()
    if turn == 0:
        d = (d+3)%4
    else:
        d = (d+1)%4
    r += DR[d]
    c += DC[d]

for r in range(R):
    for c in range(C):
        print('X' if G[r][c]==1 else ' ', end='')
    print()
print(len(painted))
	
