#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists

def read_file(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError :
        print("file is not found")
    except Exception as e:
        print(f"error:{e}")
    finally:
        print(" file is created")

read_file("demo.txt")

def write_file(filename,a):
     try:
          with open (filename,"w")as f:
              f.write(a)
     except TypeError :
          print("file type is wrong")
     except Exception as e:
         print(f"error:{e}")
     finally:
         print(" write method is finished")

write_file("demo.text","hi")


def append_file(filename,a):
    try:
          with open (filename,"a") as file:
                file.write(a)
    except AttributeError:
          print("append is not a function")
      
    finally:
          print("append function ends")

append_file("demo.txt","go")

read_file("demofile")

def delete_file(filename):
    import os
    try:
        os.remove(filename)
        print("file is deleted")
    except FileNotFoundError :
         print("file is not found")
    finally:
         print("delete function ends")

delete_file("lgesh.py")

def create_file(filename):
     try:
          with open(filename,"x")as f:
               print("the file is created")
     except FileExistsError:
          print("File exists")
          
     finally:
          print("create function ends")

create_file("demo.text")

