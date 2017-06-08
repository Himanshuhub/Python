# Assignment: Dictionary in, tuples out
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
# #function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def DicToTuple(dict):
  print dict.items()

    # for i in enumerate(dict):
    #     print i

DicToTuple(my_dict)
