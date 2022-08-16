{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6537fde8",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [20]\u001b[0m, in \u001b[0;36m<cell line: 25>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     21\u001b[0m     popularity\u001b[38;5;241m.\u001b[39mappend(item[\u001b[38;5;241m1\u001b[39m])\n\u001b[1;32m     24\u001b[0m \u001b[38;5;66;03m#Now lets make our bar\u001b[39;00m\n\u001b[0;32m---> 25\u001b[0m \u001b[43mplt\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mbarh\u001b[49m\u001b[43m(\u001b[49m\u001b[43mlanguages\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mpopularity\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     27\u001b[0m plt\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMost top 15 popular language\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     28\u001b[0m plt\u001b[38;5;241m.\u001b[39mxlabel(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPopularity\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[0;31mTypeError\u001b[0m: 'tuple' object is not callable"
     ]
    }
   ],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import numpy as np\n",
    "import csv\n",
    "from collections import Counter\n",
    "\n",
    "plt.style.use(\"fivethirtyeight\")\n",
    "\n",
    "with open('data.csv') as csv_file:\n",
    "    csv_reader = csv.DictReader(csv_file)\n",
    "    \n",
    "    language_counter = Counter()\n",
    "    \n",
    "    for row in csv_reader:\n",
    "        language_counter.update(row['LanguagesWorkedWith'].split(';'))\n",
    "\n",
    "languages = []\n",
    "popularity = []\n",
    "\n",
    "for item in language_counter.most_common(15):\n",
    "    languages.append(item[0])\n",
    "    popularity.append(item[1])\n",
    "\n",
    "#If you wish to reverse your chart order\n",
    "'''\n",
    "languages.reverse()\n",
    "popularity.reverse()\n",
    "'''\n",
    "    \n",
    "#Now lets make our bar\n",
    "plt.barh(languages, popularity)\n",
    "\n",
    "plt.title(\"Most top 15 popular language\")\n",
    "plt.xlabel(\"Popularity\")\n",
    "#plt.ylabel(\"Top 15 languages\")\n",
    "\n",
    "plt.tight_layout()\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d1f06f7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "370dfe3b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2bac9cc5",
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
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
