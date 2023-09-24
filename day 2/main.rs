use std::fs::File;
use std::io::*;

fn main() {
    puzzle_one();
    puzzle_two();
}

fn count_characters(input: &str, character: &char) -> usize {
    return input.matches(*character).count();
}

fn puzzle_one() {
    println!("\n Puzzle 1: \n");

    let mut valid_passwords_count: usize = 0;

    let input = File::open("./input.txt").unwrap();
    let reader = BufReader::new(input);

    let mut range: &str;
    let mut character_string: &str;
    let mut password: &str;

    for line in reader.lines() {
        let line_value = line.unwrap();
        let mut parts_iter = line_value.split_whitespace();

        range = parts_iter.next().unwrap();
        character_string = &parts_iter.next().unwrap()[0..1];
        password = parts_iter.next().unwrap();

        let character = character_string.chars().nth(0).unwrap();

        let num_chars: usize = count_characters(password, character);

        let mut range_iter = range.split("-");

        let range_min: usize =
            range_iter.next().unwrap().parse::<usize>().unwrap();
        let range_max: usize =
            range_iter.next().unwrap().parse::<usize>().unwrap();

        if range_min <= num_chars && num_chars <= range_max {
            valid_passwords_count += 1;
        }
    }

    println!("{}", valid_passwords_count);
}

fn puzzle_two() {
    println!("\n Puzzle 2: \n");

    let mut valid_passwords_count: usize = 0;

    let input = File::open("./input.txt").unwrap();
    let reader = BufReader::new(input);

    for line in reader.lines() {
        let line_value = line.unwrap();
        let mut parts_iter = line_value.split_whitespace();

        let range = parts_iter.next().unwrap();
        let character_string = &parts_iter.next().unwrap()[0..1];
        let password = parts_iter.next().unwrap();

        let character_array = character_string.chars().collect::<Vec<_>>();
        let character = character_array.get(0).unwrap();

        let mut range_iter = range.split("-");

        let pos_one: usize =
            range_iter.next().unwrap().parse::<usize>().unwrap();
        let pos_two: usize =
            range_iter.next().unwrap().parse::<usize>().unwrap();

        let pos_one_char = password.chars().nth(pos_one - 1).unwrap();
        let pos_two_char = password.chars().nth(pos_two - 1).unwrap();

        if (pos_one_char == *character) ^ (pos_two_char == *character) {
            valid_passwords_count += 1;
        }
    }
    println!("{}", valid_passwords_count);
}
