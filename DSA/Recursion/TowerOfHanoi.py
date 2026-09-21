class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # code here
        if n == 1:
            # print(f"move disk {n} from rod {fromm} to rod {to}")
            return 1
        moves = 0
        moves += self.towerOfHanoi(n - 1, fromm, aux, to)
        # print(f"move disk {n} from rod {fromm} to rod {to}")
        moves += 1
        moves += self.towerOfHanoi(n - 1, aux, to, fromm)
        return moves