
class HDFC:

    def withDraw(self):
        print("You can withdraw upto 40k per day......")

# if we execute this as a seperate file then the current code is called __main__ module.
# if we are importing this file into another file as a module then the module name will be
# the file name that we have saved it with

print("Module Name :", __name__)

if __name__ == '__main__':
    hdfc = HDFC()
    hdfc.withDraw()