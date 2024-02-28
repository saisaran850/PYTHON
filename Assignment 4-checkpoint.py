{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a56b972a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 4, 5, 7]\n"
     ]
    }
   ],
   "source": [
    "U=[2,3,4,5,6,7]\n",
    "U.remove(6)                                             # REMOVE OF THE LIST\n",
    "print(U)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "beb51f1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 12, 14, 16, 20]\n"
     ]
    }
   ],
   "source": [
    "L=[10,12,14,16,18,20]\n",
    "L.pop(4)                                               # POP OF THE LIST\n",
    "print(L)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "8e1d15b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "N=[11,12,13,15,17,19]\n",
    "N.index(17)                                               # INDEX OF THE LIST\n",
    "print(N.index(17))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "a4256868",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "R=[15,25,25,25,55,65,75]\n",
    "R.count(25)\n",
    "print(R.count(25))                                        # COUNT OF THE LIST\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a4a301a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Apple', 'Banana', 'Cherry', 'grapes']\n"
     ]
    }
   ],
   "source": [
    "K=[\"Cherry\",\"Banana\",\"Apple\",\"grapes\"]\n",
    "K.sort()                                                  # SORT OF THE LIST\n",
    "print(K)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3f35e4f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1.5, 1.4, 1.3, 1.2, 1.1]\n"
     ]
    }
   ],
   "source": [
    "P=[1.1,1.2,1.3,1.4,1.5]\n",
    "P.reverse()                                               # REVERSE OF THE LIST\n",
    "print(P)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "24ff96af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "n\n",
      "ai,s\n"
     ]
    }
   ],
   "source": [
    "P=\"sai,saran\"\n",
    "print(P[8])                                               # SLICING OF THE STRING\n",
    "print(P[1:5])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "1a11d37d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "java python\n"
     ]
    }
   ],
   "source": [
    "Y=\"java\"\n",
    "Z=\"python\"                                                  # CONCATENATION OF STRING\n",
    "K=Y+\" \"+Z\n",
    "print(K)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "6c04cfed",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['data scientist', 'data analyst', 'data engineer', 'statistician', 'data scientist', 'data analyst', 'data engineer', 'statistician']\n"
     ]
    }
   ],
   "source": [
    "G=[\"data scientist\",\"data analyst\",\"data engineer\",\"statistician\"]\n",
    "P=G*2                                                                           # REPETITION OF STRING\n",
    "print(P)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "f615d95b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the age  is32\n"
     ]
    }
   ],
   "source": [
    "age = 32\n",
    "y=\"the age  is{}\"\n",
    "print(y.format(age))                                                          # STRING FORMAT METHOD\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "7366a22d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello,My name is akshay and I'm 33 years old.\n"
     ]
    }
   ],
   "source": [
    "name=\"akshay\"\n",
    "age = 33\n",
    "print(f\"hello,My name is {name} and I'm {age} years old.\")                     # FORMAT 2 METHOD\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "2ae02244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "K=\"saran\"\n",
    "print(len(K))\n",
    "                                                                                # LENGTH OF STRING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "614c7b3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dheeraj\n"
     ]
    }
   ],
   "source": [
    "U=\"DHEERAJ\"\n",
    "print(U.lower())                                                                 # LOWER OF STRING\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "35b94723",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AMITABH\n"
     ]
    }
   ],
   "source": [
    "L=\"amitabh\"\n",
    "print(L.upper())                                                                 # UPPER OF STRING\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "6499c907",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['python', 'programming', 'is', 'object', 'oriented', 'language']\n"
     ]
    }
   ],
   "source": [
    "J=\"python programming is object oriented language\"\n",
    "J.split()                                                                        # SPLIT OF STRING\n",
    "print(J.split())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "92460cdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PYTHON  IS EASY TO UNDERSTAND\n"
     ]
    }
   ],
   "source": [
    "U=  \"PYTHON  IS EASY TO UNDERSTAND \"\n",
    "U.strip()                                                                         # STRIP OF STRING\n",
    "print(U.strip())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "c00680ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TODAY CLASS IS UNDERSTANDABLE\n"
     ]
    }
   ],
   "source": [
    "Y=\"TODAY CLASS IS DIFFICULTY\"                                                 \n",
    "print(Y.replace(\"DIFFICULTY\",\"UNDERSTANDABLE\"))                               # REPLACE OF STRING\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79dfa63b",
   "metadata": {},
   "outputs": [],
   "source": []
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
