public class TowerOfHanoi {

    // Recursive function to solve Tower of Hanoi puzzle
    public static void solveHanoi(int n, char fromRod, char toRod, char auxRod) {
        // Base case: If only 1 disk, move it from fromRod to toRod
        if (n == 1) {
            System.out.println("Move disk 1 from rod " + fromRod + " to rod " + toRod);
            return;
        }

        // Move n-1 disks from fromRod to auxRod using toRod as auxiliary
        solveHanoi(n - 1, fromRod, auxRod, toRod);

        // Move the nth disk from fromRod to toRod
        System.out.println("Move disk " + n + " from rod " + fromRod + " to rod " + toRod);

        // Move the n-1 disks from auxRod to toRod using fromRod as auxiliary
        solveHanoi(n - 1, auxRod, toRod, fromRod);
    }

    public static void main(String[] args) {
        int n = 3; // Number of disks

        // A, B, C are names of rods
        solveHanoi(n, 'A', 'C', 'B');
    }
}
