# Amazon-Bot
 Amazon bot used to purchase AMD  Ryzen 5800.

Two versions of the bot:

1. AmazonBot_single.py - Uses one process to do the scanning and purchasing on a given product.

2. AmazonBot_multi.py which is used to increase odds of purchasing by running the purchasing function on the product with n number of given process instances(brower instances). The Scaning is ran on one instance and onces the product is avaiable, it will fire off purchases to start hitting on the other processes. If the product is sold out than it will switch off the purchasing process instances and go back to just scanning.

3. oneinstance.py is a helper file.

Recommended usage:

product list can be updated in the helper file, oneinstance.py

system args for multi version:
product instances headless(default=yes)
i.e:python multi-instance amd5800x 10 no
