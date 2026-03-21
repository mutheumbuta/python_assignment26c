def simple_division():
    try:
        #handling a dangerous code
        number=int(input('please enter a number to divide by 10'))
        print()
        
        result= 10/number
        print(f'the answer is the result{result}')
    except ZeroDivisionError:
        #handle the errors
        print('Oops! cannot divide the number')
    except ValueError:
        #handle the errors
        print(f"Error:'{number}' is not valid")

    except Exception as e:
        print(f'something went wrong:{e}')
simple_division()
