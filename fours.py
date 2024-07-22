def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Index out of range. Please provide valid input."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def remove_contact(args):
    name = args.split()[0]
    del contacts[name]
    return "Contact removed."

@input_error
def get_phone(args):
    name = args.split()[0]
    return f"{name}'s phone number is {contacts[name]}."

@input_error
def list_contacts(args):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def unknown_command(args):
    return "Unknown command. Please try again."

def main():
    commands = {
        "add": add_contact,
        "remove": remove_contact,
        "phone": get_phone,
        "list": list_contacts
    }
    
    while True:
        user_input = input("Enter command: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        command, *args = user_input.split(maxsplit=1)
        args = args[0] if args else ""
        
        handler = commands.get(command, unknown_command)
        print(handler(args))

if __name__ == "__main__":
    main()
