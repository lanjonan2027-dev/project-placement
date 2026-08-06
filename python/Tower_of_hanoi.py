#Tower of hanoi  

def tower_of_hanoi(n, x, y, z):
    if n == 1:
        print(f"Move disk 1 from {x} to {z}")
        return
    tower_of_hanoi(n-1, x, z, y)
    print(f"Move disk {n} from {x} to {z}")
    tower_of_hanoi(n-1, y, x, z)

tower_of_hanoi(3, 'A', 'B', 'C')