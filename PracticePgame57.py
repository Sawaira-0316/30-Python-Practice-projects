#try:
 #   num = int("abc")
#except ValueError:
    #print("Error: Invalid integer.")
def check_type(year):
    assert type(year)==int,'the type is not year '
    print('the type of yeat is valid .')
    return True