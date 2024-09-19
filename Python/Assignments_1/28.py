# create a code that defines two sets of integers. then print the union intersection and different of these two sets.


def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}

    union = set1 | set2

    intersection = set1 & set2

    difference = set1 - set2

    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
    print(f"Difference (Set1 - Set2): {difference}")

if __name__ == "__main__":
    main()
