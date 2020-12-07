use std::io::{stdin, BufRead};
use std::collections::HashSet;


fn read_input() -> Vec<HashSet<char>> {
    let input_lines: Vec<String> = stdin()
        .lock()
        .lines()
        .filter_map(|line_result| line_result.ok()) 
        .filter_map(|line| line.parse().ok())       
        .collect();

    let mut answer_groups: Vec<HashSet<char>> = Vec::new();

    let mut curr_group: HashSet<char> = HashSet::new();

    for line in input_lines {
        if line.chars().count() == 0 {
            answer_groups.push(curr_group);
            curr_group = HashSet::new();
        }
        for answer in line.chars() {
            curr_group.insert(answer);
        }
    }

    answer_groups.push(curr_group);

    answer_groups
}


fn main() {

    println!("Ready to know how many distinct answers we got?");
    
    let input_groups = read_input();

    println!("There are {} groups", input_groups.len());

    let count_answers = input_groups.iter().fold(0, |mut count, group| count + group.len());

    println!("For each group, the number of questions to which anyone answered yes is {}.", count_answers);
    
}
