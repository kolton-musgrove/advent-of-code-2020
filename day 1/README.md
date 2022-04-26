# Day 1: Report Repair

- [Problem](https://adventofcode.com/2020/day/1)
- [Code](https://github.com/kolton-musgrove/advent-of-code-2020/blob/master/day%201/main.rs)
- [Walkthrough](https://dev.to/koltonmusgrove/advent-of-code-2020-day-1-problem-1-9n9)

## Walkthrough for Problem 1

For this problem, we are given a list of numbers—one per line—and asked to find two entries that sum to the number 2020. Once we have the two numbers, we multiply them together to get our answer.

### Naive Approach

The naive approach to solving the classic sum-two problem is using a nested search to test every combination of numbers that add to the desired amount (2020).

```rust
let mut v: Vec<i32> = Vec::new();

// load data
let input = File::open("./input.txt").unwrap();
let reader = BufReader::new(input);

for line in reader.lines() {
    let integer = line.unwrap().parse::<i32>().unwrap();
    v.push(integer);
}

// for every number in the vector, check if any other value in the vector sums with that number to equal 2020. If a pair of numbers is found, print them and the answer

for num1 in &v {
    for num2 in &v {
        if num1 + num2 == 2020 {
            println!{"Values: {} and {}", num1, num2};
            println!{"Answer: {}", num1 * num2};
            break
        }
    }
}
```

This approach is very time inefficient. For every additional, unique number in the input, this solution adds an additional computation step for every item in the vector. This solution has a time complexity O(n<sup>2</sup>).

### Optimal Approach

One more-efficient approach is through the use of a binary search algorithm.

First, we need a binary search algorithm to use.

```rust
fn binary_search(vector: &Vec<i32>, len: usize, target: &i32) -> Option<bool> {
    // set the low and high indices
    let mut low: i8 = 0;
    let mut high: i8 = len as i8 -1;

    while low <= high {
        // find the mid point by floor dividing the sum of the high and low
        let mid = ((high - low) / 2) + low;
        let mid_index = mid as usize;
        let val = vector[mid_index];

        // return the index of the number if it is found, or set the high and low to reduce the search space
        if val == *target { return Some(true); }

        if val < *target { low = mid + 1; }
        if val > *target { high = mid - 1; }
    }
    Some(false)
}
```

Now that we have our binary search implementation, we can use it to search for an addend for each item in the list which sums with it to 2020.

```rust
let mut v: Vec<i32> = Vec::new();

// load data
let input = File::open("./input.txt").unwrap();
let reader = BufReader::new(input);

for line in reader.lines() {
    let integer = line.unwrap().parse::<i32>().unwrap();
    v.push(integer);
}

for num1 in &v {
    //  calculate the value we would need to sum with num1 to get to 2020.
    let target = 2020 - num1;

    // check if that item is in the vector
    let answer = binary_search(&v, v.len(), &target);

    if answer.unwrap() == true {
        println!{"Values: {} and {}", num1, target};
        println!{"Answer: {}", num1 * target};
    }
}
```

This function will give us an answer to the first problem in a reasonable amount of time regardless of the size of the input to the problem. It has a time complexity of N\*log(N).

However, a simpler and equally efficient option is to use sets.

```rust
	println!("\n Puzzle 1: \n");

	let mut set: HashSet<i32> = HashSet::new();

	let input = File::open("./input.txt").unwrap();
	let reader = BufReader::new(input);

	// I decided to use a set because it eliminates duplicate values and reduces the iteration and accessing times to roughly 0.

	for line in reader.lines() {
		let integer = line.unwrap().parse::<i32>().unwrap();

		set.insert(integer);
	}

	// iterate over all of the items in the set checking if the second value for the solution is in the set. If so, print and exit.
	for number in &set {
		let target: i32 = 2020 - number;

		if set.contains(&target){
			println!{"Values: {} and {}", number, target};
			println!{"Answer: {}", number * target};
			break;
		}
	}
```

While this looks like the naive approach, the use of sets allows for instantaneous item accessing and a time complexity of O(n).

## Problem 2

The second problem of day one is very similar to the first. The only difference is that we now need to find a solution that returns three addends that sum to 2020. Like the last problem, our answer is the product of the three numbers.

### Naive Approach

This naive solution for problem two is almost the same as the naive solution to problem 1. The only difference is that we now add an additional loop to the search portion of the solution.

```rust
let mut v: Vec<i32> = Vec::new();

// load data
let input = File::open("./input.txt").unwrap();
let reader = BufReader::new(input);

for line in reader.lines() {
    let integer = line.unwrap().parse::<i32>().unwrap();
    v.push(integer);
}

// for every number in the vector, check if any other value in the vector sums with that number to equal 2020. If a pair of numbers is found, print them and the answer

for num1 in &v {
    for num2 in &v {
        for num3 in &v {
            if num1 + num2 + num3 == 2020 {
                println!{"Values: {}, {}, and {}", num1, num2, num3};
                println!{"Answer: {}", num1 * num2 * num3};
                process::exit(0x0100);
            }
        }
    }
}
```

This is an even slower algorithm than the naive solution in problem 1. Because of the extra loop, this solution now has the time complexity O(n<sup>3</sup>). Ouch.

### Optimal Approach

The optimal solution to this problem is also similar to its problem-one counterpart. For this solution though, we add a loop that iterates over every item in the list and then runs the problem one solution to find the other two numbers. This significantly increases the time complexity of the algorithm, but there are no other solutions that have a relatively similar level of coding complexity.

```rust
let mut set: HashSet<i32> = HashSet::new();

let input = File::open("./input.txt").unwrap();
let reader = BufReader::new(input);

for line in reader.lines() {
    let integer = line.unwrap().parse::<i32>().unwrap();

    set.insert(integer);
}

// While this implementation uses nested for loops, it is only O(n^2) in the worst case and is still the best solution to this problem. In terms of space complexity, it could be more efficient if I didn't copy all of the data into a set first, but I valued speed more than space in this instance.

for number1 in &set {
    for number2 in &set {
        let target: i32 = 2020 - number1 - number2;

        if set.contains(&target){
            println!{"Values: {}, {}, and {}", number1, number2, target};
            println!{"Answer: {}", number1 * number2 * target};
            process::exit(0x0100);
        }
    }
}
```
