# Leaderboard Management using Skip List

This project implements a **Leaderboard Management System** using the **Skip List** data structure to efficiently manage player rankings. The system supports fast insertion, deletion, search, and ranking operations while maintaining sorted order based on player scores.

The project demonstrates how probabilistic data structures can be used to achieve near logarithmic performance for dynamic leaderboard updates, making it suitable for large-scale gaming or ranking applications.

---

## Overview

A leaderboard system requires efficient handling of frequent updates such as adding new players, updating scores, searching player ranks, and removing entries. Traditional structures like arrays or linked lists become inefficient as the dataset grows.

This project uses a **Skip List**, a layered linked structure that enables fast search and update operations with average time complexity comparable to balanced trees, while being simpler to implement.

---

## Features

- Player insertion with score-based ranking
- Efficient player search
- Player deletion
- Automatic leaderboard ordering
- Scalable performance for large datasets
- Performance testing using large CSV datasets
- Modular and extensible design

---

## Concepts Covered

- Skip List Data Structure
- Probabilistic Level Assignment
- Dynamic Data Structures
- Search and Update Optimization
- Algorithm Performance Analysis
- Data Structure Scalability

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- CSV Data Processing
- Algorithm Design and Analysis

---

## Project Structure
LeaderboardUsingSkipList.py # Core Skip List implementation
PlayerClass.py # Player data model
addTest.py # Insert operation testing
deleteTest.py # Delete operation testing
searchTest.py # Search operation testing
smallCSVTesting.py # Testing with small datasets
largeCSVTesting.py # Performance testing
players*.csv # Test datasets (10 to 1M players)


---

## How It Works

1. Player data is read from CSV files.
2. Each player is inserted into the skip list based on score.
3. Multiple levels allow faster traversal and search.
4. Operations such as search, insert, and delete run in average **O(log n)** time.
5. Leaderboard remains sorted automatically.

---

## Usage

Run the main leaderboard implementation:

```bash
python LeaderboardUsingSkipList.py
