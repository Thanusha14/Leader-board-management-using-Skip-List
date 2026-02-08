import csv
import random
import time
from PlayerClass import Player


class Leaderboard:
    def __init__(self, game, maxLevel = 16):
        self.game = game
        self.maxLevel = maxLevel
        self.level = 1
        self.head = Player("__HEAD__", float("inf"), self.maxLevel, 0)
        self.nameMap = {}
        self.size = 0
        self.joinCounter = 0


    def _isBetter(self, scoreA, tieBreakerA, scoreB, tieBreakerB):
        if scoreA != scoreB:
            return scoreA > scoreB
        
        return tieBreakerA < tieBreakerB


    def _probabilisticLevel(self):
        lvl = 1

        while random.random() < 0.5 and lvl < self.maxLevel:
            lvl += 1

        return lvl
        

    def _findPredecessorsAndRanks(self, score, tieBreaker):
        update = [None] * self.maxLevel
        ranks = [0] * self.maxLevel
        current = self.head

        for i in range(self.level - 1, -1, -1):
            
            if i < self.level - 1:
                ranks[i] = ranks[i + 1]
            
            while (current.forwards[i] and self._isBetter(current.forwards[i].score, current.forwards[i].tieBreaker, score, tieBreaker)):

                ranks[i] += current.span[i]
                current = current.forwards[i]

            update[i] = current
        
        return update, ranks


    def _addPlayer(self, name, score, tieBreaker = None):

        if tieBreaker is None:

            self.joinCounter += 1
            tieBreaker = self.joinCounter
            
        update, ranks = self._findPredecessorsAndRanks(score, tieBreaker)

        lvl = self._probabilisticLevel()
        
        if lvl > self.level:

            for i in range(self.level, lvl):
                update[i] = self.head
                update[i].span[i] = self.size
            
            self.level = lvl
        
        node = Player(name, score, lvl, tieBreaker)

        for i in range(lvl):
            node.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = node
            
            node.span[i] = update[i].span[i] - (ranks[0] - ranks[i])
            update[i].span[i] = (ranks[0] - ranks[i]) + 1
        
        for i in range(lvl, self.level):
            update[i].span[i] += 1
            
        self.nameMap[name] = (score, tieBreaker)
        self.size += 1


    def addOrUpdateScore(self, name, newScore):
        
        if name not in self.nameMap:
            self._addPlayer(name, newScore)
        
        else:
            _, originalTieBreaker = self.nameMap[name]
            self.deletePlayer(name)
            self._addPlayer(name, newScore, originalTieBreaker)


    def deletePlayer(self, name):
        if name not in self.nameMap:
            return False

        score, tieBreaker = self.nameMap[name]
        update, _ = self._findPredecessorsAndRanks(score, tieBreaker)

        target = update[0].forwards[0]

        if not target or target.name != name or target.tieBreaker != tieBreaker:
            return False
            
        for i in range(self.level):
            
            if update[i].forwards[i] == target:
                update[i].span[i] += target.span[i] - 1
                update[i].forwards[i] = target.forwards[i]
            
            else:
                update[i].span[i] -= 1
        
        while self.level > 1 and not self.head.forwards[self.level - 1]:
            self.level -= 1
        
        del self.nameMap[name]
        self.size -= 1
        return True


    def search(self, name):
        if name not in self.nameMap:
            return None, None
        
        score, tieBreaker = self.nameMap[name]
        _, ranks = self._findPredecessorsAndRanks(score, tieBreaker)
        return score, ranks[0] + 1


    def topN(self, n):
        out = []
        cur = self.head.forwards[0]
        rank = 0

        while cur and len(out) < n:
            rank += 1
            out.append((rank, cur.name, cur.score))
            cur = cur.forwards[0]
        
        return out


    def loadFromCSV(self, filepath):
        
        with open(filepath, newline = "") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                name = row["name"]
                score = int(row["score"])
                self.addOrUpdateScore(name, score)


    def displayStructure(self):
        lines = []
        
        for lvl in range(self.level - 1, -1, -1):
            entries = []
            cur = self.head.forwards[lvl]
            
            while cur:
                entries.append(f"{cur.name}({cur.score})")
                cur = cur.forwards[lvl]
            
            lines.append(f"Level {lvl}: " + " -> ".join(entries))
        
        structure = "\n".join(lines)
        print(f"Leaderboard structure for game: {self.game}\n{structure}")


if __name__ == "__main__":
    
    lb = Leaderboard("MyGame", maxLevel = 100)
    
    # lb.loadFromCSV("players1000000.csv")
    # lb.loadFromCSV("players500000.csv")
    lb.loadFromCSV("players250000.csv")
    
    print(f"Total players: {lb.size}")
    print("-" * 20)

    print("Top 5:")
    print(lb.topN(5))
    print("-" * 20)
    
    s = "player347"
    print(f"Searching for {s}:")
    result = lb.search(s)

    if result:
        print(f"{s} found with score {result[0]} at rank {result[1]}")
    
    else:
        print(f"{s} not found")
    
    print("-" * 20)

    # start = time.perf_counter()
    
    # lb.displayStructure()

    # end = time.perf_counter()
    
    print(f"Updating {s}'s score to 5000:")
    lb.addOrUpdateScore(f"{s}", 5000)
    
    print("Top 5 after update:")
    print(lb.topN(5))
    print("-" * 20)
    
    print(f"Searching for {s}:")
    print(lb.search(s), "\n")
    
    
    a = "player2"
    print(f"Deleting {a}:")
    lb.deletePlayer(f"{a}")
    
    print(f"Total players now: {lb.size}")
    print("Top 5 after delete:")
    
    print(lb.topN(20))
    print("-" * 20)

    print(f"Searching for {s}:")
    result = lb.search(s)
    
    if result:
        print(f"{s} found with score {result[0]} at rank {result[1]}")
    
    else:
        print(f"{s} not found")
    
    print("-" * 20)

    # print("\nFinal Structure:")
    # lb.displayStructure()

    # print(f"The time taken was {(end - start)} seconds")
    # print(f"The time taken was {(end - start) * 1000000} microseconds")