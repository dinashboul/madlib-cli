
from importlib.resources import contents
import re


def read_template(filepath) :
 with open(filepath) as file:
  try:

   
    content = file.read()
    return content

  finally:
    file.close()   
  
   

def parse_template(content):
        # for line in content:
            expected_parts = re.findall(r'\{(.*?)\}', content)
            expected_stripped = re.sub(r'\{(.*?)\}', '{}', content)
            
            return  expected_stripped,tuple (expected_parts)
            
            
    
    
def merge(stripped,list):
   newLine= stripped.format(*list)
   if stripped =="It was a {} and {} {}.":
       write_func('assets/response.txt',newLine) 
   return(newLine)      

def input_func(parts):
     list=[]
     for x in parts:
            word=input(f"please enter the {x}=>")
            list.append(word)
     return(list)


            
def write_func(file_path,new_content):
    with open(file_path,'w') as file:
        content=file.write(new_content)
        
        return content
        

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


if __name__=="__main__":
    game_madlib()
