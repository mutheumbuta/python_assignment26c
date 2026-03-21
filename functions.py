first_name=''
last_name=''

def register(first_name,last_name):
    """ this is a function"""
    input('please enter your first name...\n:')
    print()
    input('please enter your last name..\n:')
    print(f'you sre now registered', first_name, last_name)
    return first_name,last_name
register(first_name,last_name)#call the function