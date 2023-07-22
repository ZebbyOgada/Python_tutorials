#A match statement takes an expression and compares its value to successive patterns given as one or more case blocks

#this code compares subject values to one or more literals

#define a function of possible errors
def http_error(status):
    
    #match the status
    match status:

        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I am a teapot"
        case _:
            return "Something is wrong with the internet"

#match statement for greetings commmand

salutation = input("Enter a salutation\n")
lower_case_salutation = salutation.lower()
print(lower_case_salutation)

match lower_case_salutation:
    case 'hello':
        print('Hello to you too')
    case 'how are you':
        print('Im fine, thank you')
    case other:
        print('Try another command')

    

    

         
        

