### Computational Thinking Exercise

**Step 1: Identify the Big Problem**

Main Problem:
The school canteen has a slow lunch process which causes delays for students because ordering, payment, and inventory management are not organized efficiently.

**Step 2: Identify Three to Four Sub-Problems**

1. Students take too long to decide what food to order, which slows down the line.
2. The cashier manually calculates the total and gives change, making payment slower and at a risk of inaccuracy.
3. There is no system for monitoring food inventory, so staff may not know when items are running out.


**Step 3: Define Computational Thinking Approaches**

**| Sub-Problem | CT Skill | Example Solution |**
|---|---|---|
| Students take too long to decide what food to order. | Abstraction | Create a simplified menu showing food names, prices, and available items so students can quickly choose. |
| The cashier manually calculates totals and gives change. | Algorithm Design | Create a step-by-step system that adds item prices, calculates the total, receives payment, and calculates the change automatically. |
| There is no system for monitoring food inventory. | Pattern Recognition | Track which food items sell most frequently to identify patterns in demand and predict which items may run out. |

**Step 4: Pseudocode**

### Cashier Payment System

START

totalcost = 0

PRINT "Enter the number of items."
READ numberofitems

REPEAT numberofitems times
PRINT "Select an item."
READ fooditem

GET the price of fooditem

PRINT "Enter the quantity."
READ quantity

totalcost = totalcost + (price × quantity)
END REPEAT

PRINT "Total cost: ", totalcost

PRINT "Enter amount paid."
READ amountpaid

IF amountpaid >= totalcost THEN
change = amountpaid - totalcost
PRINT "Change: ", change
ELSE
PRINT "Insufficient payment."
ENDIF

STOP
