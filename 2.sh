#!/bin/bash


cd secret


python3 success.py > results.txt


cd ../



#result comes back like this
#Congratulations!!! You completed your task in 0:00:00.837014
#That qualifies you for 35 speed points. That's the max possible plus a bonus 10!!!
#35$67$a02310135
#Submit this ticket value to the website: a96945c86816d3c65c21ca2b1207d7c85841077215667217098f37b3:67:35:837014


python3 client.py submit


whoami


