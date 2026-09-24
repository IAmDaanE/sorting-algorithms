# Visualized Sorting Algorithms

Three algorithms that sort an array of 200 values from smallest to biggest. See how long each one takes and which is the fastest.

---

<img width="1789" height="648" alt="Schermafbeelding 2026-08-29 001602" src="https://github.com/user-attachments/assets/555fdf22-6936-46a0-9dfb-a98a7f972117" />

## The Algorithms

The algorithms are bubble sort, insertion sort and selection sort. Here is how they work and their average benchmarked times on my laptop:

#### Bubble Sort
Always compares two neighboring values and checks if the left one is bigger then the right one, if so their positions are swapped. It completed in `14.5167` seconds.
#### Insertion Sort
There is a sorted and unsorted pool, at first everything is unsorted. It always takes the first upcoming value in the unsorted one and keeps shifting it left until its in the right place. It completed in `8.1183` seconds.
#### Selection Sort
Again works with a sorted and unsorted pool. It searches for the smallest one in the unsorted pool and sticks it to the right of the sorted one. It completed in `15.117` seconds.

## Running a Algorithm

**Requires:** Python 3.9 - 3.14
1. Install the required libraries, preferably in a venv.

    ```
    pip install -r requirements.txt
    ```
2. Run the program.

    ```
    python src/bubble_sort.py # replace bubble_sort.py with the desired variant
    ```

## License

This project is open-source and available under the MIT License.