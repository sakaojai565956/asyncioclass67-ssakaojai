# running a function with arguments in another thread
from time import sleep, ctime
from threading import Thread

# a custom function that blocks for a moment
<<<<<<< HEAD
def task(sleep_time, message) :
    # block for a moment
    sleep (sleep_time)
    #display a message
    print(f'{ctime()}{message}')
    
# create a thread
thread = Thread (target=task, args=(1.5, 'New message from another thread'))
=======
def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(f'{ctime()} {message}')

# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))
>>>>>>> da9298ed63f8e733278d4eb60fc55328115df595
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()
