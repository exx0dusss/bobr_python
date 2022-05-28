import threading as th
import time
#t = th.Thread(target=func, args = (arg1,))
def thread_func(name, time_to_sleep):
    print(f"Thread{name}has started")
    time.sleep(time_to_sleep)
    print(f"Thread{name}has stopped")
if __name__ == '__main__':
    print("Main: Before any thread starts")
    t = th.Thread(target=thread_func, args = ('One',5),daemon=True)
    t2 = th.Thread(target=thread_func, args = ('Two',3),daemon=True)
    print(type(t))
    print(type(t2))

    print("Main: before thread starting")
    t.start()
    t2.start()

    print("Main: Waiting for Thread ...")
    t.join()
    t2.join()
    print("Main: Program is about to finish")


