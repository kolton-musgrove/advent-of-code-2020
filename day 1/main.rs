// only time efficient solutions and their dependencies are in this file

use std::collections::HashSet;
use std::fs::File;
use std::io::*;
use std::process;

fn main() {
    puzzle_one();
    puzzle_two();
}

fn puzzle_one() {
    println!("\n Puzzle 1: \n");

    let mut set: HashSet<i32> = HashSet::new();

    let input = File::open("./input.txt").unwrap();
    let reader = BufReader::new(input);

    // I decided to use a set because it eliminates duplicate values and reduces
    // the iteration and accessing times to roughly 0.

    for line in reader.lines() {
        let integer = line.unwrap().parse::<i32>().unwrap();

        set.insert(integer);
    }

    // iterate over all of the items in the set checking if the second value for
    // the solution is in the set. If so, print and exit.
    for number in &set {
        let target: i32 = 2020 - number;

        if set.contains(&target) {
            println! {"Values: {} and {}", number, target};
            println! {"Answer: {}", number * target};
            break;
        }
    }
}

fn puzzle_two() {
    println!("\n Puzzle 2: \n");

    let mut set: HashSet<i32> = HashSet::new();

    let input = File::open("./input.txt").unwrap();
    let reader = BufReader::new(input);

    for line in reader.lines() {
        let integer = line.unwrap().parse::<i32>().unwrap();

        set.insert(integer);
    }

    // While this implementation uses nested for loops, it is only O(n^2) in the
    // worst case and is still the best solution to this problem.
    // In terms of space complexity, it could be more efficient if I didn't copy
    // all of the data into a set first, but I valued speed more than space in
    // this instance.

    for number1 in &set {
        for number2 in &set {
            let target: i32 = 2020 - number1 - number2;

            if set.contains(&target) {
                println! {"Values: {}, {}, and {}", number1, number2, target};
                println! {"Answer: {}", number1 * number2 * target};
                process::exit(0x0100);
            }
        }
    }
}
