
import mypackage.mymodule as m
from mypackage.mymodule import Player, greet

greet("Rahul Dravid")

ply1 = Player("Virat Kholi", 34)
print(ply1)

m.greet(m.gname)

print("-" * 40)
import sys
for path in sys.path:
    print(path)
