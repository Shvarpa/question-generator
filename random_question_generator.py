import sys
import random
import re

class Randomizer():
    @staticmethod
    def sample(spread, count):
        return random.sample(range(spread[0], spread[1] + 1), count)

    @staticmethod
    def flatten(collection):
        collection = list(x for y in collection for x in y)
        collection.sort()
        return collection

    @staticmethod    
    def purgeSeed(seed):
        """
        removes white spaces or other symbols from the seed and returns purged seed
        """
        matches = re.compile(r'\d{9}').search(seed)
        if matches:
            seed = matches[0]
        return seed

    def questions(self, seed):
        seed = Randomizer.purgeSeed(seed)
        random.seed(seed)
        spreads = {
            (1,5): 1,
            (6,13): 2,
            (14,17): 1,
            (18,25): 2
        }
        return Randomizer.flatten(Randomizer.sample(*spread) for spread in spreads.items())

if __name__ == "__main__":
    if len(sys.argv)>1:
        id = sys.argv[1]
    else:
        id = input('Please enter your ID number: ')
    print('You were assigned the following questions: {}'.format(
        Randomizer().questions(id)
    ))
    input("Press 'Enter' to close\n")
