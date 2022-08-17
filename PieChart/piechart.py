{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b1f3bb5b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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qFu3bixYsICMjIxytz04OJiPP/6Yhx9+mM6dO3PXXXcRFBSEyWTi0qVL/Pnnn+h0Os6fPw/Apk2bePHFF+nQoUPJSeDJycn8+uuvmM1mpk+fXrLsDh06MGPGDN5//306d+7MkCFDcHR0ZNOmTRw8eJDQ0FBmzZpVlW9hKS4uLnz11VeMHz+eXr16ER0dTbNmzbCysuLSpUvs2bOHixcvcu7cuRseyKpKVlZWxMXFMWzYMMaNG0e7du2IiIjAzs6OS5cucejQIU6dOsXWrVtLAmTixIns3LmT7777jjZt2tC/f388PDy4evUq27dvp2/fvrz55pu3VY9SqeTBBx/kgw8+IDIykn79+mEwGEhISCAjI4OoqKhyW+23Ehsby759+5gwYQK9evXC2toaPz8/xowZc8N5bjv8XnrpJf744w8OHz7Mxo0bUavV+Pr6MnPmTB588MFqucymadOmLF68mI8++oi4uLiSFtaoUaOqZX2LFi0iMjKSZcuWsWzZMsxmM0FBQbzyyitMmTKlzJHGN954A6VSyebNm9m1axdms5mxY8feNPwAPvroIwICAli5ciVLlizB3d2dvn378txzz5U6+bQ6eHt7Ex8fz0svvcSuXbv4448/CA4O5r333iMmJuaG4RcaGoqnpyfXrl0r062NjIzEysoKg8FwwxOtR4wYQVhYGAsWLGDLli0lYd+gQQN69uxZqhveo0cPLl68yM6dO1m3bh3Z2dl4enrSoUMHpkyZQmxsbKllz5o1i/DwcBYvXswPP/yATqejUaNGPPnkk0ybNq3c0yyqUnR0NNu3b2f+/Pls3LiR3bt3o1arS640eemll6ptn2N5QkND2b59O5988gm//vor3377LZIk4eXlRbNmzXj00UdL7QZQKBQsXLiQHj168MUXX7Bq1Sp0Oh0eHh60a9eOoUOH3lE9zz//PG5ubixbtowvvvgCR0dHunXrxgsvvHDbd4d54oknyM7OJj4+nrlz52I0GunSpctNw0/xz4mUgiAIFkXcz08QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIskwk8QBIsk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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "\n",
    "\n",
    "plt.style.use('fivethirtyeight')\n",
    "slice = [60, 40, 20]\n",
    "explode = [0,0.1,0]\n",
    "#edgecolor: will ad sepeartor between the pie\n",
    "plt.pie(slice, labels=['Sixty', 'Forty', 'Twenty'], wedgeprops={'edgecolor':'black'}, explode=explode, shadow=True, startangle=90, autopct='%.1f%%')\n",
    "\n",
    "\n",
    "plt.title(\"Isn't not an awesome Piechart\")\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "404ab388",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2b98640",
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