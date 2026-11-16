def func():
    try:
        selection = int(input('Select a development lifecycle >\n-> 1 - Waterfall\n-> 2 - RAD\n>> '))
        if selection == 1:
            
    except:
        print('>> We have ran into an error please try again! <<')
        func()
func()