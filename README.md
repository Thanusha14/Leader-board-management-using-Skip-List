# LeaderBoard_using_SkipLists

An efficient leaderboard management system implemented using a **Skip List** data structure.  
The system supports fast player ranking, score updates, and Top-N queries while maintaining high performance even for large datasets.

Skip Lists provide probabilistic balancing, enabling performance comparable to balanced trees while remaining simpler to implement and maintain.

---

## Overview

Leaderboard systems require efficient handling of dynamic updates such as inserting players, updating scores, ranking queries, and retrieving top performers. Traditional linear structures become inefficient as the number of players increases.

This project uses a **Skip List**, a probabilistically balanced multi-level linked structure, to achieve near logarithmic performance for core leaderboard operations while ensuring stable ordering and efficient rank computation.

---

## Features

- Efficient leaderboard operations using Skip Lists
- Supports:
  - Adding new players
  - Updating player scores
  - Deleting players
  - Searching player rank
  - Retrieving Top-N players
- Tie-breaking handled using join order
- Optimized for large datasets (hundreds of thousands of players)
- CSV-based bulk data loading
- Fast rank calculation using span values

---

## Data Structures Used

### Skip List
- Multiple forward pointers per node
- Probabilistic level assignment
- Span values for efficient rank calculation
- Maintains sorted order by score

### Hash Map
- Stores player name to `(score, tie-breaker)` mapping
- Enables O(1) player lookup
- Supports efficient updates and deletions

---

## Design Overview

Each player is represented as a node in the skip list and ordered by:

1. Higher score (descending order)
2. Tie-breaker (earlier join time gets higher rank)

The leaderboard maintains:

- Fast traversal across multiple levels
- Accurate rank calculation using span counters
- Stable ordering during score updates
- Efficient insertion and deletion operations

---

## Time Complexity

| Operation          | Average Time |
|--------------------|--------------|
| Insert Player      | O(log n)     |
| Delete Player      | O(log n)     |
| Update Score       | O(log n)     |
| Search Rank        | O(log n)     |
| Top-N Retrieval    | O(n)         |

---

## Technologies Used

- Python
- Custom Skip List Implementation
- CSV File Handling
- Object-Oriented Programming

---

## Usage

Prepare a CSV file in the following format:
name,score
player1,1200
player2,950


Run the leaderboard system:

```bash
python LeaderboardUsingSkipList.py

