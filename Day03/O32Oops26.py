
import O31Oops25

def withDraw(self):
    print("You can with draw upto 4k per day......")

O31Oops25.HDFC.withDraw = withDraw              # monkey patching
hdfc = O31Oops25.HDFC()
hdfc.withDraw()


"""
a
===
x = 10

b
===
y = 5

a.x = y
print(a.x)
"""