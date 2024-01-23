"""
    Day 23: Context Managers
        Learn about context managers and create your own context manager using the with statement.
"""

# Custom Context Manager Example
class TimerContext:
    def __init__(self):
        print("init method called")

    def __enter__(self):
        import time
        print("Enter method called, time starts")
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        import time
        print("Exit method called")
        elapsed_time = time.time() - self.start_time
        print(f"Time elapsed: {elapsed_time} seconds")

# Usage of the Custom Context Manager
if __name__ == "__main__":
    # The 'with' statement is used to create a context for the TimerContext
    # This ensures that the TimerContext is properly set up and cleaned up
    with TimerContext() as timer:
        # Code block where you want to measure the time
        import time
        print("With statement + 2s cooldown")
        time.sleep(2)  # Simulating some time-consuming operation

    # Outside the 'with' block, the __exit__ method is automatically called
    # The total time elapsed during the 'with' block is printed


"""
Example of file manager in python:

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
         
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
 
# loading a file 
with FileManager('test.txt', 'w') as f:
    f.write('Test')
 
print(f.closed)
"""