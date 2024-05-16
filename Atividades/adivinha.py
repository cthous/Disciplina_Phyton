{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ec61ae4-7fec-4c14-8d06-c564cf364aee",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Adivinhe o Número\r",
    "#Escreva um programa que gera um número\r\n",
    "aleatório e solicita ao usuário que adivinhe o\r\n",
    "número. O programa deve fornecer feedback ao\r\n",
    "usuário se o palpite é muito alto, muito baixo ou\r\n",
    "correto."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "15b65a2b-cdb7-45ee-8cd1-2579f4cdf320",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  150\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quase. Tente um número menor\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quase. Tente um número maior\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  150\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quase. Tente um número menor\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  75\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quase. Tente um número maior\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  125\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quase. Tente um número maior\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  130\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quase. Tente um número maior\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  140\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quase. Tente um número maior\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quase. Tente um número maior\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  145\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quase. Tente um número maior\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Escolha um número entre 1 e 300:  148\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Parabéns! Você acertou o número.\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "numero_aleatorio = random.randint(1, 300)\n",
    "\n",
    "while True:\n",
    "    numero_escolhido = int(input('Escolha um número entre 1 e 300: '))\n",
    "    if numero_escolhido < 1 or numero_escolhido > 300:\n",
    "        print('Eu disse um número ENTRE 1 e 300.')\n",
    "    elif numero_escolhido < numero_aleatorio:\n",
    "        print('Quase. Tente um número maior')\n",
    "    elif numero_escolhido > numero_aleatorio:\n",
    "        print('Quase. Tente um número menor')\n",
    "    else:\n",
    "        print('Parabéns! Você acertou o número.')\n",
    "        break\n"
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
