import time


def brewCoffe():
    print("Start brewCoffe()")
    time.sleep(3)
    print("End brewCoffe()")
    return "Coffe is ready"

def toastBagel():
    print("Start toastbagel()")
    time.sleep(2)
    print("End toastBagel()")
    return "Bagel is toasted"

def main():

    start_time = time.time()

    result_coffe = brewCoffe()
    result_bagel = toastBagel()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of brewCoffe: {result_coffe}")
    print(f"Result of toasBagel: {result_bagel}")
    print(f"Total execution time: {elapsed_time: .2f} seconds")

if  __name__ == "__main__":
    main()

