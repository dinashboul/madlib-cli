
from importlib.resources import contents
import re

''' 
  read_template function read a content from file that passing from the main and 
  >>> then read it and return the content that read it
  >>> close the file anway
'''
def read_template(filepath) :
 with open(filepath) as file:
  try:

   
    content = file.read()
    return content

  finally:
    file.close()   
  
   
'''
    parse_template function its parsing the content that come from read_template function to the parts
    >>> first part: the string inside {}
    >>> second part(stripped part) : the lines without the string that inside {}
    >>> return the first part as tuple
'''
def parse_template(content):
        # for line in content:
            expected_parts = re.findall(r'\{(.*?)\}', content)
            expected_stripped = re.sub(r'\{(.*?)\}', '{}', content)
            
            return  expected_stripped,tuple (expected_parts)
            
            
    
'''
    merge function its merging the content that user inputing from the main inside the stripped part
'''    
def merge(stripped,list):
   newLine= stripped.format(*list)
   if stripped =="It was a {} and {} {}.":
       write_func('assets/response.txt',newLine) 
   return(newLine)      
 

'''
    input_func function :this function responsible about the content of user input and 
    >>> return a list that saving the content
'''
def input_func(parts):
     list=[]
     for x in parts:
            word=input(f"please enter the {x}=>")
            list.append(word)
     return(list)

'''
    write_func function its write the final content that passing from merge function on the response.txt file after open it

'''
            
def write_func(file_path,new_content):
    with open(file_path,'w') as file:
        content=file.write(new_content)
        
        return content
        
'''
    game_madlib its responsible about open the make_me_a_video_game_template.txt' and read it then parsing its content 
    >>> input new strings 
    >>> merging with the stripped part
    >>> write the final content on the response.txt
    >>> by calling previos functions


'''
def game_madlib ():
    content=read_template('assets/make_me_a_video_game_template.txt')      
    stripped,parts=parse_template(content)
    # print(stripped,parts)
    list=[]
    for x in parts:
     word=input(f"please enter the {x}=>")
     list.append(word)
    
    print(merge(stripped,list))
    write_func('assets/response.txt',merge(stripped,list))

'''
  welcome_message functon : its a function that print the introductory text how its the game work   
'''

def welcome_message():
     wellcome = '''
**************************************
**    Welcome to the MadLib game!   **
**   Madlib is a game where you     **
**  decide the parts of the story   **
**   
**    Add your  words to            **
**    create a funny story by       **
**    answering the question        **
**    and press enter...            **
**************************************
''' 
     print(wellcome)
    

if __name__=="__main__":
    welcome_message()
    game_madlib()
