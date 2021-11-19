import prompt

def welcome_user():
    username_question = 'May I have your name? '
    username = prompt.string(username_question)
    print('Hello, {}!'.format(username))

def main():
    welcome_user()

if __name__ == '__main__':
    main()