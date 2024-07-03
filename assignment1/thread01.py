# running a function in another thread
<<<<<<< HEAD
from time import sleep, ctime 
=======
from time import sleep, ctime
>>>>>>> da9298ed63f8e733278d4eb60fc55328115df595
from threading import Thread

# a custom function that blocks for a moment
def task():
    # block for a moment
<<<<<<< HEAD
    sleep (1)
    # display a message
    print(f'{ctime()} This is from another thread')
    
# create a thread
thread = Thread (target=task)
# run the thread
thread. start ()
# wait for the thread to finish
print(f'{ctime()}Waiting for yhe thread...')
thread.join()
=======
    sleep(1)
    # display a message
    print(f'{ctime()} This is from another thread')

# create a thread
thread = Thread(target=task)
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()
>>>>>>> da9298ed63f8e733278d4eb60fc55328115df595
