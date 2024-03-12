{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b920b5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install numpy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "05650cd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as ns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1d184be5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6 7]\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "import numpy as ns\n",
    "arr=ns.array([1,2,3,4,5,6,7])\n",
    "print(arr)                              # Creating arrays with numpy and accesing the single array\n",
    "print(arr[3])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "383cfcb3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4  5]\n",
      " [ 6  7  8  9 10]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as ns\n",
    "arr=ns. array([[1,2,3,4,5],\n",
    "             [6,7,8,9,10]])            # Creating two dimensional arrays using numpy\n",
    "print(arr)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3c8c2999",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[11 12 13 14 15]\n",
      "  [16 17 18 19 20]\n",
      "  [21 22 23 24 25]]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as ns\n",
    "arr=ns.array([[[11,12,13,14,15],        # Creating three dimensional arrays using numpy\n",
    "              [16,17,18,19,20],\n",
    "              [21,22,23,24,25]]])\n",
    "print(arr)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "54791aec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "29\n"
     ]
    }
   ],
   "source": [
    "import numpy as ns\n",
    "arr=ns.array([11,12,13,14,15,16])          # array addition using numpy\n",
    "print(arr[2] + arr[5])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3e85c760",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4th row in 3rd element,arr: 26\n",
      "2nd row in 2nd element,arr: 20\n"
     ]
    }
   ],
   "source": [
    "import numpy as ns\n",
    "arr=ns.array([[15,16,17],\n",
    "             [18,19,20],\n",
    "             [21,22,23],                        # Accesing the two dimensional array \n",
    "             [24,25,26],\n",
    "             [27,28,29]])\n",
    "print(\"4th row in 3rd element,arr:\",arr[3,2])\n",
    "print(\"2nd row in 2nd element,arr:\",arr[1,2])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d15d5065",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "34\n",
      "49\n",
      "54\n"
     ]
    }
   ],
   "source": [
    "import numpy as ns\n",
    "arr=ns.array([[[11,12,13,14],\n",
    "              [15,16,17,18]],\n",
    "              \n",
    "             [[19,20,21,22],\n",
    "             [23,24,25,26]],\n",
    "              \n",
    "              [[27,28,29,30],\n",
    "              [31,32,33,34]],                            # Creating 3d arrays using numpy\n",
    "              \n",
    "              [[35,36,37,38],\n",
    "              [39,40,41,42]],\n",
    "              \n",
    "              [[43,44,45,46],\n",
    "              [47,48,49,50]],\n",
    "              \n",
    "              [[51,52,53,54],\n",
    "              [55,56,57,58]]])\n",
    "print(arr[2,1,3])\n",
    "print(arr[4,1,2])\n",
    "print(arr[5,0,3])\n",
    "\n",
    "              "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "c2976461",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4  5  6]\n",
      " [ 7  8  9 10 11 12]\n",
      " [13 14 15 16 17 18]\n",
      " [19 20 21 22 23 24]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as ns\n",
    "arr=ns.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])\n",
    "newarr=arr.reshape(4,6)\n",
    "print(newarr)                                          # reshape array using numpy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "c65e5608",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "import numpy as ns\n",
    "a = ns.array([1,2,3,4,5])\n",
    "b = ns.array([[6,7,8,9,10],[11,12,13,14,15]])\n",
    "c = ns.array([[[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]])    # ndim using numpy\n",
    "print(a.ndim)\n",
    "print(b.ndim)\n",
    "print(c.ndim)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "406cf267",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[30 57 29 27 98]\n"
     ]
    }
   ],
   "source": [
    "from numpy import random\n",
    "x = random.randint(100,size=(5))\n",
    "print(x)                                    # random function using numpy\n",
    "                                           "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
