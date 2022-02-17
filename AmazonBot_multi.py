import oneinstance
from multiprocessing import Process
import sys

try:

    product = str(sys.argv[1])
    instances = int(sys.argv[2])
    headless = str(sys.argv[3])

    if __name__ == '__main__':
        for items in range(0,instances):
            print(f"Starting Search for {product}")
            p = Process(target=oneinstance.startinstance, args=(product,headless,))
            p.start()
            # p.join()
except:
    print("Input Format product instances headless(default=yes)")
    print("i.e: python multi-instance amd5800x 10 no")
    print(f"current input reads python {sys.argv}")
