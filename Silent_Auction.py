print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to the silent auction!")

list = {
  
}

def bid():
  name = input("Enter your name: ")
  amnt = int(input("Enter Your bid $"))
  list[name] = amnt

  extr_play = input("Is there another player , type 'yes' or 'no.'\n")
  if extr_play == "yes":
    bid()
  elif extr_play == "no":
    bid_amnt = []
    bid_num = list.values()
    highest_bid = max(bid_num)
    winner = ""
    for bidder in list:
      bid_record = list[bidder]
      if bid_record >= highest_bid:
        highest_bid = bid_record
        winner = bidder
      
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bid()
  
  
             
  
