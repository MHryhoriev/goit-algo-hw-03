def hanoi_recursive(n, source_rod, destination_rod, auxiliary_rod, rods_state):
    """
    Recursive function to solve the Tower of Hanoi problem with state printing after each move.

    Parameters:
        n (int): Number of disks to move.
        source_rod (str): The rod from which disks are moved.
        destination_rod (str): The rod to which disks are moved.
        auxiliary_rod (str): The auxiliary rod to assist in moving disks.
        rods_state (dict): Dictionary representing the current state of each rod.
    """
    if n == 1:
        disk = rods_state[source_rod].pop()
        rods_state[destination_rod].append(disk)

        print(f"Move the disk from {source_rod} to {destination_rod}: {disk}")
        return

    # Move n-1 disks from source to auxiliary
    hanoi_recursive(n - 1, source_rod, auxiliary_rod, destination_rod, rods_state)

    disk = rods_state[source_rod].pop()
    rods_state[destination_rod].append(disk)

    print(f"Move the disk from {source_rod} to {destination_rod}: {disk}")
    print(f"Intermediate state: {rods_state}")

    # Move the n-1 disks from auxiliary to destination
    hanoi_recursive(n - 1, auxiliary_rod, destination_rod, source_rod, rods_state)


def main():
    a_rod_list = [3, 2, 1]
    b_rod_list = []
    c_rod_list = []

    rods_state = {'A': a_rod_list, 'B': b_rod_list, 'C': c_rod_list}
    print(f"Initial state: {rods_state}")

    hanoi_recursive(len(a_rod_list), 'A', 'C', 'B', rods_state)

    print(f"Final state: {rods_state}")


if __name__ == '__main__':
    main()
