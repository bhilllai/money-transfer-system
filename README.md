# Money Transfer System
Project for Crypto Course

## Problem statement

>Person A wants to send money to person B. 
So person A initiates a transaction but without revealing his bank balance we have to prove he has enough money to carry out the transaction.
The successful transactions then have to be stored in such a way so that no one can tamper with them. 

## Solution

```sh
Implement a blockchain to store all the successful transactions and using zero knowledge proofs to verify the transactions
```

## Features
- Register new users to the system with the amount they have
- The users can then add transactions
- Verify transactions using zero knowledge proofs
- Using PoS (Proof of Stake) consensus algorithm to mine blocks
- Implementation of Merkle root to calculate the hash of all the transactions in a block.
- To be able to view the transaction history that is related to a user.

## Functions implemented 
- createBlock() 
- verifyTransaction()
- mineBlock()
- viewUser()

## Transaction structure:
- Sender ID/name
- Receiver ID/name
- Amount
- Timestamp of the transaction

## Block structure:
- Timestamp
- Merkle root
- Hash of the previous block
- Block Height
- Hash of the Block

## Tech Used
- Python 

## Members:
- Jai Sehgal
- Dhruv Jain
- Tushar Chattopadhyay
- Aditya Khandelwal
- Shreyans Soni



