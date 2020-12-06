use std::io::{stdin, BufRead};
use reduce::Reduce;


fn find_triplet_indexes(sorted_values: &Vec<u32>, target: u32) -> Vec<usize> {

    if sorted_values.len() >= 3 {
        let mut first: usize = 0;
        let mut second: usize = 0;
        let mut third: usize = 0;
        for i in 0..sorted_values.len() - 2 {
            let found_couple = find_couple_indexes(&sorted_values[(i + 1)..].to_vec(), target - sorted_values[i]);

            if found_couple.len() == 2 && found_couple[0] != found_couple[1] {
                first = i;
                second = found_couple[0] + i + 1;
                third = found_couple[1] + i + 1;
                break
            }
        }
        if first < second && second < third {
            println!("Found {}(#{}), {}(#{}) and {}(#{}) summing up to {}", sorted_values[first], first, sorted_values[second], second, sorted_values[third], third, target);
            vec!(first, second, third)
        } else {
            println!("No triplet found matching the target {} - {}, {}, {}", target, first, second, third);
            Vec::new()
        }
    } else {
        println!("There are less than 3 elements in the vector");
        Vec::new()
    }
}

fn find_couple_indexes(sorted_values: &Vec<u32>, target: u32) -> Vec<usize> {

    let mut start = 0;
    let mut end = sorted_values.len() - 1;

    while start <  end {
        let partial = sorted_values[start] + sorted_values[end];

        if partial > target {
            end = end - 1;
        } else if partial < target {
            start = start + 1;
        } else {
            break
        }
    }

    if start > end {
        Vec::new()
    } else {
        println!("Found {}(#{}) and {}(#{}) summing up to {}", sorted_values[start], start, sorted_values[end], end, target);
        vec!(start, end)
    }
}

fn compute_output(input_values: &Vec<u32>, indexes: Vec<usize>) -> Option<u32> {
    indexes.into_iter().map(|a| input_values[a]).reduce(|a, b| a * b)
}

fn read_input() -> Vec<u32> {
    let input_values: Vec<u32> = stdin()
        .lock()
        .lines()
        .filter_map(|line_result| line_result.ok()) 
        .filter_map(|line| line.parse().ok())       
        .collect();  
    input_values                               
}

fn main() {
    const TARGET: u32 = 2020;
    let mode = String::from("triplet");

    println!("Ho-ho-ho! Let's find the two entries that sums up to {}", TARGET);
    
    let mut input_values: Vec<u32> = read_input();
    input_values.sort();

    let indexes_vec = match mode.as_str() {
        "couple" => find_couple_indexes(&input_values, TARGET),
        "triplet" => find_triplet_indexes(&input_values, TARGET),
        _ => {
            println!("Mode does not exist");
            Vec::new()
        }
    };

    if indexes_vec.len() == 0 {
        println!("No values found summing up to {}", TARGET);
    } else {
        let target = compute_output(&input_values, indexes_vec);

        println!("Found target {:?}", target);
    }

}
