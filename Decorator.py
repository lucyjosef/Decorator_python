def auth(func_display_page):
    print("Entering fdecorator")
    print(func_display_page)

    def fdecorate(user):
        print('Entering fdecorate')
        return func_display_page(user)

    print("outgoing auth")
    return fdecorate


@auth
def display_page(page):
    print("Entering display_page")
    print(page)


display_page('OK')
