
from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
        #A can be knight or knave but cant be both at the same time
        And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
        #If A is a knight, she is right and both
        Implication(AKnight, And(AKnight, AKnave)),
        #If A is knave she's lying and she is not knave and knight at the same time
        Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
       
        And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
        And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

        Implication(AKnight, And(AKnave, BKnave)),
        Implication(AKnave, Not(And(AKnave, BKnave)))
)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
        And(Or(AKnight,AKnave),Not(And(AKnight, AKnave))),
        And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

        Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
        Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
        
        Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
        Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
        
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
"""knowledge3 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    
    Implication(BKnight, And(CKnave, AKnave)),
    Implication(BKnave, Not(And(CKnave, AKnave))),
    
    Implication(CKnight, And(CKnight, AKnight)),
    Implication(CKnight, Not(And(CKnight, AKnight)))
    
    
"""
knowledge3 = And(
    # A, B and C are knights or knaves but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    # If B is a knight, A said 'I am a knave', and C is a knave:
    Implication(BKnight, CKnave),
    Implication(BKnight, And(
      # A then said 'I am a Knave', A may be a Knight or a Knave:
      Implication(AKnight, AKnave),
      Implication(AKnave, Not(AKnave)),
    )),
    # If B is a knave, A said 'I am a knight' C is not a knave:
    Implication(BKnave, Not(CKnave)),
    Implication(BKnave, And(
      # A then said 'I am a Knight', A may be a Knight or a Knave:
      Implication(AKnight, AKnight),
      Implication(AKnave, Not(AKnight))
    )),
    # If C is a knight, A is a knight:
    Implication(CKnight, AKnight),
    # If C is a knave, A is not a knight:
    Implication(CKnave, Not(AKnight))
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
