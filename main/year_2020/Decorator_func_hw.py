import sys
sys.stdout = open('test.html',"w")
def dec_func(func):
    def wrapper():
        print(f'<!DOCTYPE HTML>')
        print(f'<html>')
        print(f' <head>')
        print(f' <meta charset="utf-8">')
        print(f' <title> </title>')
        print(f' </head>')
        print(f' <body>')
        func()
        print(f' </body>')
        print(f'</html>')
    return wrapper
@dec_func
def main_txt():
    print("<p>TEXT</p>")
main_txt()


