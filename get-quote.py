import random
def primary():
    #print("Keep it logically awesome.")
    #python get-quote.py
    #python3 get-quote.py

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = 13
    rnd = random.randint(0, last)
    print(quotes[rnd])
    print(quotes[14])

if __name__== "__main__":
  primary()
