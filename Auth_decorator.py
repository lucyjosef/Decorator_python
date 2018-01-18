#!/home/apprenant/PycharmProject/Decorateur/venv/bin/python3.5

import sys

try:
    user = sys.argv[1]
except IndexError as err:
    print("Error")
    print(err)
    exit(1)

right = (
    ['Michel', 'Marion'],
    ['Paul', 'Cassandre', 'Olivier'],
    ['Lucy']
)

def right_to_int():
    if right == 'user':
        return 0
    elif right == 'admin':
        return 1
    else:
        return 2

def show_error():
    echo("error page")

@auth_decorator("user")
def say_hello():
    echo("Hello")

@auth_decorator("admin")
def show_page():
    echo("pages")

@auth_decorator('root')
def show_root():
    echo("root")



"""
def auth(func_display_page, user):
    print("Entering fdecorator")
    print(func_display_page)

    def fdecorate(user):
        print('Entering fdecorate')
        return func_display_page(user)

    print("outgoing auth")
    return fdecorate



def display_page(page):
    print("Entering display_page")
    print(page)


display_page('OK')
"""
