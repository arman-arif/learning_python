# Car Game

command = ""
started = False

while command.lower() != 'quit':
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started!')
            continue
        print('Car started...')
        started = True
    elif command == 'stop':
        if not started:
            print('Car is already stopped!')
            continue
        print('Car stopped.')
        started = False
    elif command == 'help':
        print('''
            \rstart - to start the car
            \rstop - to stop the car
            \rquit - to quit
        ''')
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understant that!")
    
