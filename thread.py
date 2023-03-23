import threading

def func_with_while_loop():
    while True:
        print("Function with while loop running...")

def while_loop_in_thread():
    while True:
        print("While loop running in thread...")

# Create a thread for the while loop
thread = threading.Thread(target=while_loop_in_thread)
thread.start()

# Call the function with the while loop
func_with_while_loop()