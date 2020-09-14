import random

def updated_main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1

  rnd = random.randint(0, last)
  print("Quote #1: " + quotes[rnd])

  rnd = random.randint(0, last)
  print("Quote #2: " + quotes[rnd])
  
  rnd = random.randint(0, last)
  print("Quote #3: " + quotes[rnd])

if __name__== "__main__":
  updated_main()
