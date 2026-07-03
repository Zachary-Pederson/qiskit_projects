import textwrap

def handle_discussion_response(*answers):
    
    '''
    Prints out response for discussion exercise code cells throughout Inspirit 
    AI's coding notebooks. 
    
    Parameters
    ----------
    answers : str
        The answers provided to the discussion exercise code cell
    '''
    RESPONSE_PRINT_WIDTH = 61

    # Ask for responses if not provided
    if all([not answer for answer in answers]):
        if len(answers) == 1: 
            print("Please input your response in the answer box above!")
        else:
            print("Please input your responses in the answer boxes above!")

    # Otherwise print out response(s)
    else: 
        print(f"Your answer{'s' if len(answers) > 1 else ''}:")
        print()

        if len(answers) == 1:
            print("-" * RESPONSE_PRINT_WIDTH)
            print(textwrap.fill(answers[0], width=RESPONSE_PRINT_WIDTH)) # Format string for better print
            print("-" * RESPONSE_PRINT_WIDTH)
            print()
        else: 
            for i, answer in enumerate(answers):
                print(("-" * (RESPONSE_PRINT_WIDTH // 2)) + str(i+1) + ("-" * (RESPONSE_PRINT_WIDTH // 2)))
                if not answer:
                    print("No response! Input your answer above.") 
                else:
                    print(textwrap.fill(answer, width=RESPONSE_PRINT_WIDTH)) 
                print("-" * RESPONSE_PRINT_WIDTH)
                print()

        print("If you haven't already, discuss with your classmates!")
    