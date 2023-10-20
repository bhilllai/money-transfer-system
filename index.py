import BlockChain
import AddTransactions
import ViewMultipleTransaction
import ViewTimestamp
import ViewBChain
import ViewUnverified
import Node
import ViewSeller
import ViewBuyer
# Initiating the blockchain
blockchain = BlockChain.Blockchain()

print("<------------------------SESSION START------------------------->")

leftover_trns = []
unverified_trns=[]  
count = 1              
# To hold any unverified transactions after an iteration

# Iterations start...
# In each iteration the user can perform only one query
while True:
    print("\n_________________________________________")
    print("_________________________________________")
    print("\n[1] - Add Users")
    print("[2] - View all Users")
    print("[3] - Add Transactions")
    print("[4] - View all confirmed Transactions")
    print("[5] - View all incoming Transactions for a particular user")
    print("[6] - View all outgoing Transactions for a particular user")
    print("[7] - View a block")
    print("[8] - View the Blockchain")
    print("[9] - View Timestamp of a transaction")
    print("[10] - View all unconfirmed transactions")
    print("[11] - Mining the Block")
    print("\n[e] - Exit")
    choice = input("\n>>> Choose a query to execute: ")

    if choice == "1":
        Node.addNode()
    elif choice == "2":
        Node.viewNode()
    elif choice == "3":
        unverified_trns = AddTransactions.inputTransactions(
            blockchain, leftover_trns, count)
        count+=1

    elif choice == "4":
        ViewMultipleTransaction.viewTransactions(blockchain)

    elif choice == "5":
        ViewSeller.viewTransaction(blockchain)

    elif choice == "6":
        ViewBuyer.viewTransaction(blockchain)    

    elif choice == "7":
        ViewBChain.viewBlock(blockchain)

    elif choice == "8":
        ViewBChain.viewBlockchain(blockchain)

    elif choice == "9":
        ViewTimestamp.viewTimestamp(blockchain)

    elif choice == "10":
        ViewUnverified.viewUnverifiedTransactions(leftover_trns)
    elif choice == "11":
        leftover_trns = AddTransactions.addTransactions(
            unverified_trns, blockchain)
        print("Mined the block successfully!")

    elif choice == "e":
        if blockchain.chain_valid(blockchain.chain) == False:

            exit()

        print("\nThank you.\n")
        break

    else:
        print('\nPlease choose from the queries given!!!')

print("<-------------------------SESSION END-------------------------->")
