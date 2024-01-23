{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5f38f5bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def hello():\n",
    "    return \"Hello, Svante!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e460f0f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == '__main__':\n",
    "   app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71831d77",
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
