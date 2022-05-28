'''Address book'''


book = {

    "Adam" : "Telephone 11231",
    "John" : "Telephone 2312312",
    "Crieg": "Telephone 31322",
    "Hanna": "Telephone 412312"
}

def add(name, no):
    book[name] = no
    menu()
def rem(delete):
    book.pop(delete)
def display(all):

    for key, value in book.items():
        print(key, ' - > ', value)
#
# def exit():
def menu():

    print('------------------------')
    print("Print all records - type \"ALL\"")
    print('------------------------')
    print("Enter new record - type \"NEW\"")
    print('------------------------')
    print("Remove specific record - type \"DEL\" followed by entering a NAME of the record")
    print('------------------------')
    print("Close the program - type \"STOP\"")
    print('------------------------')

def main():
    print('Welcome to address book v0.01\nTo start please choose one of the following commands:\n\n')
    menu()
    while True:
        prompt = input('Enter you choice')

        if prompt == 'ALL':
            all = prompt
            display(all)
            menu()
        if prompt == 'NEW':
            name = input('Enter name: ')
            no = input('Enter number:')
            add(name,no)
        if prompt == 'DEL':
            delete = input('Enter name: ')
            rem(delete)
        if prompt == 'STOP':
            break
        else:
            print('Try again')


main()