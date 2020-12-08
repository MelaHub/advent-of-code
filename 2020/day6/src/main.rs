use std::io::{stdin, BufRead};
use std::collections::HashSet;


fn read_input() -> Vec<Vec<HashSet<char>>> {
    let input_lines: Vec<String> = stdin()
        .lock()
        .lines()
        .filter_map(|line_result| line_result.ok()) 
        .filter_map(|line| line.parse().ok())       
        .collect();

    let mut answer_groups: Vec<Vec<HashSet<char>>> = Vec::new();

    let mut curr_group: Vec<HashSet<char>> = Vec::new();

    for line in input_lines {
        if line.chars().count() == 0 {
            answer_groups.push(curr_group);
            curr_group = Vec::new();
        } else {
            curr_group.push(line.chars().collect());
        }
    }

    answer_groups.push(curr_group);

    answer_groups
}

fn count_first_part(groups: &Vec<Vec<HashSet<char>>>) -> usize {
    groups.iter()
        .map(|group| {
            group
                .iter()
                .fold(HashSet::new(), |acc, hs| acc.union(hs).cloned().collect())
                .len()
        }).sum()
}


fn count_second_part(groups: &Vec<Vec<HashSet<char>>>) -> usize {
    groups.iter()
    .map(|group| {
        group
            .iter()
            .skip(1)
            .fold(group[0].clone(), |acc, hs| {
                acc.intersection(hs).cloned().collect()
            })
            .len()
    })
    .sum()
}


fn main() {

    println!("Ready to know how many distinct answers we got?");
    
    let input_groups = read_input();

    let answers_with_at_least_one_yes = count_first_part(&input_groups);

    let answers_with_at_all_yes = count_second_part(&input_groups);

    println!("There are {} answers with at least one yes and {} with all yes", answers_with_at_least_one_yes, answers_with_at_all_yes);
    
}
