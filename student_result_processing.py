from multiprocessing import Process, Array, Semaphore


def producer(marks, input_marks, empty, full):
    empty.acquire()

    print("\nProducer: Storing marks in shared memory...", flush=True)

    for i in range(5):
        marks[i] = input_marks[i]

    print("Producer: Marks stored in shared memory.", flush=True)

    full.release()


def consumer(marks, empty, full):
    full.acquire()

    print("\nConsumer: Reading marks from shared memory...", flush=True)

    total = sum(marks)
    average = total / len(marks)

    print("Student Marks:", list(marks), flush=True)
    print("Total Marks:", total, flush=True)
    print("Average Marks:", round(average, 2), flush=True)

    empty.release()


if __name__ == "__main__":
    print("------------------------------------------------------------")
    print("              STUDENT RESULT PROCESSING")
    print("------------------------------------------------------------")

    input_marks = []

    print("Enter marks for 5 subjects:")
    print("----------------------------")

    for i in range(5):
        mark = int(input(f"Subject {i + 1}: "))
        input_marks.append(mark)

    marks = Array('i', 5)

    empty = Semaphore(1)
    full = Semaphore(0)

    producer_process = Process(
        target=producer,
        args=(marks, input_marks, empty, full)
    )

    consumer_process = Process(
        target=consumer,
        args=(marks, empty, full)
    )

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("\n------------------------------------------------------------")
    print("              Result processing completed.")
    print("------------------------------------------------------------")
