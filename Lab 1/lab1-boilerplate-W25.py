"""
Program Modified By: Sebastian Deluca
Student ID: 20250909
Date: January 17 2025
Lab No. 1
Goal:?
"""
import multiprocessing
import threading
import os
import time
import psutil

# define a function that performs some I/O tasks
def io_task(name):
    print("Demonstrating an I/O-bound task")
    print(f"Process {name} (PID: {os.getpid()}) is starting I/O task)...")

    # TODO-1: Simulate system call for I/O-bound task
    # Check OS name/type, and print OS name
    print(f"OS name: {os.name}")
    # Execute a system shell command to list directory
    os.listdir()
    # sleep for 5 seconds
    time.sleep(5)
    # print that the process with current process id has finished tasks
    print(f"Process {name} (PID: {os.getpid()}) has completed its tasks.")

# Define a function to demonstrate CPU-bound tasks
def cpu_task(name):
    print("Demonstrating a CPU-bound task")
    print(f"Process {name} with PID {os.getpid()} is starting CPU-bound task..")
    # TODO-2: define a CPU intensive tasks

# Define a function to demonstrate threading and simulate file download
def thread_task_download(name):
    print("Threading-file download")
    # TODO-3
    # Print Start of: Thread name and thread ID
    # simulate file download
    # Print Finishing of: Thread name and thread ID

# Define a function to demonstrate threading
def thread_task_process(name):
    print("Threading-process data")
    # TODO-4
    # Print Start of: Thread name and thread ID
    # simulate data processing
    # Print Finishing of: Thread name and thread ID

# Define a function to print PCB info for all processes
def pcb_of_created_processes(processes):
    print("Process information:")
    # TODO-5
    # Loop through the process and print the process information (id, name, status, cpu usage, memory information, number of threads


# Define a function to print info from Thread control block for all threads
def list_threads_info():
    print("Listing thread details:")
    # TODO-6
    # Loop through the threads and print the thread information (name, id,, native id)


if __name__ == "__main__":
    processes = []
    threads = []
    print("This is a demonstration of I/O and CPU bound processes, multiprogramming and multitasking, PCB, TCB, system calls and context swotch")

    # Demonstrating few I/O dound process creation for multiprogramming
    # TODO-7
    # Create a number of I/O bound processes, append them in processes and start those processes
    # print PCB information for the created processes


    # Demonstrating few CPU dound process creation for multiprogramming
    # TODO-8
    # Create a number of CPU bound processes, append them in processes and start those processes
    # print PCB information for the created processes


    # Demonstrating thread creation for download task
    # TODO-9
    # Create a number of threads that simulate download task, append them in threads and start those threads
    # print TCB information for the created threads

    # Demonstrating thread creation for data processing task
    # TODO-10
    # Create a number of threads that simulate data processing task, append them in threads and start those threads
    # print TCB information for the created threads


    # TODO-11:
    # Wait for all processes to complete
    # Wait for all threads to complete


    # TODO-12:
    # Record and display total time taken by the different type of processes
    # Record and display total time taken by all the threads
    # Record and display total execution time

    print("All processes and threads finished.")