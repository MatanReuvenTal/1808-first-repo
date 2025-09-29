try:
    f = int(input("enter a number: "))
    r = 5/0
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("ValueError")
except BaseException as e:
    print(e.args)