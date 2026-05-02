def collect_basic_info():
    """Collect basic user information from standard input."""
    info = {}
    info['name'] = input('Enter your name: ').strip()
    info['age'] = input('Enter your age: ').strip()
    info['email'] = input('Enter your email: ').strip()
    info['phone'] = input('Enter your phone number: ').strip()
    return info


if __name__ == '__main__':
    basic_info = collect_basic_info()
    print('\nCollected basic information:')
    for key, value in basic_info.items():
        print(f'{key.capitalize()}: {value}')
