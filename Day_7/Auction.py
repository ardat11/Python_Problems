# This code tells you at what price the product was sold in the Auction

bidcount= int(input("enter the number of bids"))

bids = []

for i in range(bidcount):
    bid = int(input("enter the bid"))
    bids.append(bid)
    print("The bid for the auction was successfully placed")

print("Sold: ", max(bids))