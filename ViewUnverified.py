from ViewMultipleTransaction import addSpaces

# This function prints the leftover unverified transactions in an iteration


def viewUnverifiedTransactions(leftover_transactions):
    if len(leftover_transactions) == 0:
        print("\nNo unconfirmed Transactions.")
        return

    print("Transaction ID      Receiver      Sender         Amount(INR)     Timestamp")
    print("-------------------------------------------------------------------------------------")

    for unverified_trn in leftover_transactions:
        print("{}      {}      {}            {}      {}".format(
            addSpaces(unverified_trn[0], len("Transaction ID")),
            addSpaces(unverified_trn[2], len("Seller")),
            addSpaces(unverified_trn[3], len("Buyer")),
            addSpaces(unverified_trn[1], len("Amount(INR)")),
            unverified_trn[4]
        ))
