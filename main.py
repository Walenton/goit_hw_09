from contacts import generate_contacts


contacts = generate_contacts(10)


def get_command(user_input):
    for i in COMMANDS:
        if user_input.startswith(i):
            return COMMANDS[i]


def input_error_name(func):
    def wrapper (list_input):
        try:
            list_input[1]
        except IndexError:
            return 'enter name and phone'     
        return func (list_input)
    return wrapper


def input_error_phone(func):
    def wrapper (list_input):
        try:
            int (list_input[2])
        except ValueError:
            return 'invalid phone number'
        except IndexError:
            return 'enter phone number'
        return func (list_input)
    return wrapper


def input_error_existing_phone(func):
    def wrapper(list_input):
        name = list_input[1].capitalize()
        try:
            phone = contacts[name]
            print (phone)
            return f'contact {name} already exists with number {phone}'
        except KeyError:
            return func(list_input)
    return wrapper


def input_error_not_existing_phone(func):
    def wrapper(list_input):
        name = list_input[1].capitalize()
        try:
            contacts[name]
            return func(list_input)
        except KeyError:
            return f'no contact with name {name} in your phonebook'
    return wrapper


def command_hello(list_input):
    return 'How can I help you?'


@input_error_name
@input_error_phone
@input_error_existing_phone
def command_add(list_input):
    name = list_input[1].capitalize()
    phone = list_input[2]
    contacts[name]=phone
    return f'contact {name} successfully added to your phonebook'
    

@input_error_name
@input_error_phone
@input_error_not_existing_phone
def command_change(list_input):
    name = list_input[1].capitalize()
    phone = list_input[2]
    contacts[name]=phone
    return f'contact {name} successfully changed in your phonebook'


@input_error_name
@input_error_not_existing_phone
def command_phone(list_input):
    name = list_input[1].capitalize()
    phone = contacts[name]
    return f'phone number {name}: {phone}'


def command_show_all(list_input):  
    return contacts


def command_exit(list_input):
    exit()


COMMANDS ={
    'hello' : command_hello,
    'add' : command_add, 
    'change' : command_change,
    'phone' : command_phone,
    'show all' : command_show_all,
    'good bye' : command_exit,
    'close' : command_exit,
    'exit' : command_exit,                
}

def main():
    while True:
        user_input = input('input command: ').strip().casefold()
        list_input = user_input.split(' ')
        command = get_command(user_input)

        if command:
            print (command(list_input))
        else:
            print ('unknown command')    
    
    
if __name__ == '__main__':
    print (main())   






