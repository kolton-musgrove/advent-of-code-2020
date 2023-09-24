//  Most of the logic for the problems in day 3 can be contained in one
// function. The only logic in the actual function calls is which paths are
// followed be each problem

use std::fs::File;
use std::io::*;

fn main() {
    puzzle_one();
    puzzle_two();
}

fn read_input() -> BufReader<File> {
    let input = File::open("./input.txt").unwrap();
    let reader = BufReader::new(input);

    return reader;
}

fn path_solve(right: usize, down: usize) -> usize {
    let reader = read_input();

    let mut tree_collisions: usize = 0;
    let mut right_increment: usize = 0;
    let mut down_increment: usize = 0;

    for line in reader.lines() {
        // we only want to check the lines that match the 'down' input given to
        // the function
        if down_increment % down == 0 {
            // now we have to find if the horizontal position matches the
            // 'right' input given to the function also, since we
            // only have 31 characters of horizontal space, we need to use the
            // modulus operator to find our location relative to the first 31.
            if line
                .unwrap()
                .chars()
                .nth((right_increment * right) % 31)
                .unwrap()
                == '#'
            {
                tree_collisions += 1;
            }
            right_increment += 1;
        }

        down_increment += 1;
    }

    return tree_collisions;
}

fn puzzle_one() {
    println!("\n Puzzle 1: \n");

    let solution: usize = path_solve(3, 1);
    println!("{}", solution);
}

fn puzzle_two() {
    println!("\n Puzzle 2: \n");

    let solution: usize = path_solve(1, 1)
        * path_solve(3, 1)
        * path_solve(5, 1)
        * path_solve(7, 1)
        * path_solve(1, 2);
    println!("{}", solution)
}
