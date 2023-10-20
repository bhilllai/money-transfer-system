# This function asks transaction ID from the user and prints the corresponding transaction details
# seller is receiver
def addSpaces(input, total_length):
    input = str(input)
    while (total_length - len(input)) > 0:
        input = input + " "
    return input


def viewTransaction(blockchain):
    if len(blockchain.chain) == 0:
        print('\nBlockchain empty!!!')
        return

    while True:

        seller_name = input("\nEnter Receiver's name: ")
        print("Transaction ID      Receiver      Sender        Amount(INR)     Timestamp")
        print("-------------------------------------------------------------------------------------")
        quote_string = "{}      {}      {}          {}      {}"
        exists = False
        for block in blockchain.chain:
            for transaction in block["transactions_list"]:
                if transaction[2] == seller_name:
                    print(quote_string.format(addSpaces(transaction[0], len("Transaction ID")),
                                              addSpaces(
                                                  transaction[2], len("Seller")),
                                              addSpaces(
                                                  transaction[3], len("Buyer")),
                                            #   addSpaces(
                                            #       transaction[4], len("Property_ID")),
                                              addSpaces(
                                                  transaction[1], len("Amount(INR)")),
                                              transaction[4]))
                    exists = True

        if exists == False:
            print("\nInvalid Receiver name!!!")
            y_or_n = input("\n>>> Repeat query?[y/n]")
            if y_or_n == "y":
                continue
        print("-------------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------")
        break
    print("")
    return
