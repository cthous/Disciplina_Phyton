{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a31582e4-5a33-4216-9832-fd7c93e8aea2",
   "metadata": {},
   "outputs": [],
   "source": [
    "numero % 3 == 0 and numero % 5 == 0:\n",
    "        print('FizzBuzz')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1e18199-3f1b-4162-9d62-0ed5a121d13c",
   "metadata": {},
   "source": [
    "Fizz Buzz\n",
    "\n",
    "Escreva um programa que imprime os números de 1 a 100.\n",
    "\n",
    "Mas para múltiplos de três, imprima \"Fizz\" em vez do\n",
    "número, e para múltiplos de cinco, imprima \"Buzz\".\n",
    "    \n",
    "Para números que são múltiplos de três e cinco, imprima\n",
    "\"FizzBuzz\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "83215a74-d6df-41af-af13-82c12ac8503d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]\n",
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "Buzz\n",
      "11\n",
      "Fizz\n",
      "13\n",
      "14\n",
      "FizzBuzz\n",
      "16\n",
      "17\n",
      "Fizz\n",
      "19\n",
      "Buzz\n",
      "Fizz\n",
      "22\n",
      "23\n",
      "Fizz\n",
      "Buzz\n",
      "26\n",
      "Fizz\n",
      "28\n",
      "29\n",
      "FizzBuzz\n",
      "31\n",
      "32\n",
      "Fizz\n",
      "34\n",
      "Buzz\n",
      "Fizz\n",
      "37\n",
      "38\n",
      "Fizz\n",
      "Buzz\n",
      "41\n",
      "Fizz\n",
      "43\n",
      "44\n",
      "FizzBuzz\n",
      "46\n",
      "47\n",
      "Fizz\n",
      "49\n",
      "Buzz\n",
      "Fizz\n",
      "52\n",
      "53\n",
      "Fizz\n",
      "Buzz\n",
      "56\n",
      "Fizz\n",
      "58\n",
      "59\n",
      "FizzBuzz\n",
      "61\n",
      "62\n",
      "Fizz\n",
      "64\n",
      "Buzz\n",
      "Fizz\n",
      "67\n",
      "68\n",
      "Fizz\n",
      "Buzz\n",
      "71\n",
      "Fizz\n",
      "73\n",
      "74\n",
      "FizzBuzz\n",
      "76\n",
      "77\n",
      "Fizz\n",
      "79\n",
      "Buzz\n",
      "Fizz\n",
      "82\n",
      "83\n",
      "Fizz\n",
      "Buzz\n",
      "86\n",
      "Fizz\n",
      "88\n",
      "89\n",
      "FizzBuzz\n",
      "91\n",
      "92\n",
      "Fizz\n",
      "94\n",
      "Buzz\n",
      "Fizz\n",
      "97\n",
      "98\n",
      "Fizz\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "#criar uma lista\n",
    "lista = [list(range(1,101))]\n",
    "print(lista)\n",
    "for numero in range(1,101):\n",
    "    if numero % 3 == 0 and numero % 5 == 0:\n",
    "        print('FizzBuzz')\n",
    "    elif numero % 5 == 0:\n",
    "        print('Buzz')\n",
    "    elif numero % 3 == 0:\n",
    "        print('Fizz')\n",
    "    else:\n",
    "        print(numero)\n"
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
