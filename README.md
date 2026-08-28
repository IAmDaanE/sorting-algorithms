# Visualized Sorting Algorithms

Three algorithms that sort an array of 200 values from smallest to biggest. See how long each one takes and which is the fastest.

---

<img width="1789" height="648" alt="Schermafbeelding 2026-08-29 001602" src="https://github.com/user-attachments/assets/555fdf22-6936-46a0-9dfb-a98a7f972117" />

## The Algorithms

The algorithms are bubble sort, insertion sort and selection sort. Here is how they work:

#### Bubble Sort
Always compares two neighboring values and checks if the left one is bigger then the right one, if so their positions are swapped.
#### Insertion Sort
There is a sorted and unsorted pool, at first everything is unsorted. It always takes the first upcoming value in the unsorted one and keeps shifting it left until its in the right place.
#### Selection Sort
Again works with a sorted and unsorted pool. It searches for the smallest one in the unsorted pool and sticks it to the right of the sorted one.

## Getting Started

### Getting the Source

This project is [hosted on GitHub](https://github.com/IAmDaanE/sorting-algorithms). You can download the zip or clone this project directly using this command:

```
git clone git@github.com:IAmDaanE/sorting-algorithms.git
```

### Running the Program

Requirements: You must have Python 3.10 or higher.
1. Clone the repository or download the zip and unpack it to your directory of choice.
2. Navigate to that directory in a terminal.
3. In a venv or the global python version install the needed libraries.
    ```
    pip install -r requirements.txt
    ```
4. Run the program.
    ```
    python bubble_sort.py
    ```

## License

This project is open-source and available under the MIT License.
