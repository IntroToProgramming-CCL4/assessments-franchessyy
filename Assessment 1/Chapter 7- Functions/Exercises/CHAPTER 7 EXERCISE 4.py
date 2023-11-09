#print t shirt and its message but with different sizes!
def make_shirt(size='small', message='keep calm and love python'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('large', 'live,love,laugh.')
   