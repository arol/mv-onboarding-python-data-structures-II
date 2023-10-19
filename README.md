# Data Structures Exercise

## 🧠 Background

Welcome to the LinkedList exercise. 

Through this task, you'll solidify your understanding of linked lists, a fundamental data structure in computer science. This exercise is structured as a sequence of tasks that will guide you to create a complete singly linked list implementation in Python.

## 📦 Structure

The repository consists of several files structured as follows:

- `linked_list.py`: Where you'll implement the LinkedList and Node classes.
- `test_linked_list.py`: Contains unit tests that will help you verify the correctness of your code incrementally. You 
can use it to understand better what is asked from you no each task.
- `requirements.txt` or `poetry.lock` and `pyproject.toml`: Files that manage the dependencies required to run the tests.

## 🚀 Getting Started

1. Fork this repository.
2. Clone your fork to your local machine.
3. Install the dependencies using either `pip install -r requirements.txt` or `poetry install` if you’re using Poetry.
4. Run the tests using the `pytest` command to see which tests pass or fail.

## 🆙 Delivery

1. Once finished, commit & push
    ```bash
    git commit -am 'solution'
    git push origin main
    ```
2. Open a pull request with your name

## 🛠 Tasks

Your mission is to make all the unit tests pass by implementing the linked list functionalities incrementally, following the tasks below:

- **Task 1**: Instantiation –
  Ensure that your LinkedList class can be instantiated, and initially, the head is set to None.

- **Task 2**: Insertion at the Head –
  Implement the insert method that adds a new node with the given data at the head of the list.

- **Task 3**: Insertion with Existing Data –
  Modify the insert method, so if a node with the same data already exists, it should be moved, and the new data should be inserted at the head.

- **Task 4**: Finding Elements –
  Implement the find method that checks whether a node with a specific data value exists within the list.

- **Task 5**: Deleting Elements –
  Implement the delete method that will remove a node with a specific data value from the list.

- **Task 6**: LinkedList Length –
  Implement a method to calculate and return the length of the linked list.

- **Task 7**: Convert LinkedList to Python List –
  Implement a method that converts your linked list into a Python list (array).

## 🧪 Testing

- Run the tests after completing each task to ensure your implementation is correct.
- The tests are designed to guide you through the implementation process, helping you ensure that each part is working before moving on to the next.

## 🥇 Extra credits

Feel free to expand upon the exercise with additional features such as:

- Implementing a method to reverse the linked list.
- Adding a tail pointer to the LinkedList class and updating methods to maintain it correctly.
- Implementing additional tests to cover more edge cases or functionality.

## 🍀 Good Luck!

We believe that through this exercise, you’ll be able to enhance your problem-solving skills and deepen your understanding of linked lists in a hands-on way. 

Happy coding! 🚀
