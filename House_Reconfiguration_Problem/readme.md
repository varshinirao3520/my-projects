An optimization-based approach using Answer Set Programming (ASP) to solve space reconfiguration challenges.

📌 Overview
The House Reconfiguration Problem (HRP) is an optimization problem that involves reorganizing objects such as rooms, cabinets, and items while satisfying constraints like ownership rules, storage limits, and compatibility requirements. The objective is to minimize reconfiguration costs while ensuring efficient space utilization.

📌 Problem Domain: Constraint Optimization, Space Management, Knowledge Representation
📌 Solution Approach: Answer Set Programming (ASP) using Clingo
📌 Inspired by: Industrial reconfiguration problems and ASP Challenge 2019

⚡ Features
✅ Legacy Configuration Handling – Supports pre-existing room and cabinet assignments
✅ Capacity Constraints – Limits on the number of items per cabinet and cabinets per room
✅ Ownership and Compatibility Rules – Ensures correct assignment of items based on ownership
✅ Cost Optimization – Minimizes reconfiguration costs while maximizing space reuse
✅ Answer Set Programming (ASP) Implementation – Solves HRP using Clingo

🛠️ Technologies Used
Answer Set Programming (ASP)
Clingo Solver (by Potassco)
Constraint Logic Programming
Optimization Techniques in ASP
📌 Problem Definition
The HRP problem consists of:
1️⃣ Legacy Configurations: Initial layout of rooms, cabinets, and items
2️⃣ Capacity Constraints:
Cabinets hold max 5 items
Rooms hold max 4 cabinets
3️⃣ Compatibility Rules:
Long items must be stored in high cabinets
Items must be stored in cabinets belonging to their owner’s room
4️⃣ Cost Minimization:
Reusing rooms/cabinets has lower cost
Adding/removing components increases cost

📌 How to Run the Project
🔹 Prerequisites
Ensure you have Clingo installed:
pip install clingo

🔹 Clone the Repository

git clone https://github.com/varshinirao3520/my-projects/new/main/House_Reconfiguration_Problem.git

🔹 Run the Solver
Execute Clingo with the ASP program:
clingo house_reconfiguration.lp --opt-mode=optN

📊 Results & Observations
Test Case 1: Small-Scale Scenario
Input: 2 rooms, 2 cabinets, 4 items
Output: Correctly assigned cabinets/items without new rooms
Cost: Minimal (1 unit)
Test Case 2: Medium-Scale Scenario
Input: 3 rooms, 6 cabinets, 10 items
Output: Added 1 new room, reused all legacy cabinets
Cost: Higher due to additional space
✅ Capacity, ownership, and size constraints were satisfied in both cases.
