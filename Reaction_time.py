# =============Only this much space needed=============== #
# You can Align with Hash at last of upper line
# Problem in Closing The program
import time
import random


# Average Program
def avg(*value):
    sum1 = 0
    if tup == []:  # |if not tup| also possible
        pass
    else:
        n = len(value)
        for i in range(n):
            sum1 = value[i] + sum1
        av = sum1 / n
        print("Average reaction speed is \n", av, "ms")


def react_test():
    while True:
        # From -------Here--------
        # To
        print(10 * "-", "READY", 10 * "-")
        time.sleep(random.randrange(2, 4))
        print(10 * "-", "GO", 10 * "-")
        t1 = time.time()
        input()  # this activates before line 23 IDK why
        t2 = time.time()
        tim = t2 - t1
        t_im = int(tim * 1000)
        if t_im <= 60:
            print("You clicked too early \nTry Again")
        # -------Here------
        # while loop is to avoid error of 0ms because
        # it takes input before time module starts
        # in line 26
        else:
            print("Reaction speed is\n", t_im, "ms")
            tup.append(t_im)
            break


# =============================Main=========================== #
tup = []
print(10 * "=", "Reaction Speed Test", 10 * "=")
print("Wait till said\n      GO\n Press any key to start")
while True:
    print("Press zero to exit | Enter to continue")
    # Using try except to make program easy to access
    # A little trick
    y = input()
    try:
        y = int(y)
        if y == 0:
            avg(*tup)
            break
        else:
            print("Sorry I did not Understand")
            continue
    except:
        react_test()
        continue
