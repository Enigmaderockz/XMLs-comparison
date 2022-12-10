filename = 'com.txt'

def check_errors(filename):  
  with open(filename, 'r') as file_:
      text = file_.read()  
  last_section = text.split('bring it on')[-1]  
  errors = [line for line in last_section.split('\n') if 'err' in line]  
  if errors == []:
    print("no errors")
    return True
  else:
    for error in errors:
      print(error)
    return False

def print_error(filename):
  is_err = check_errors(filename)
  print(is_err)

print_error(filename)
