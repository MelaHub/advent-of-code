use std::io::{stdin, BufRead};
use reduce::Reduce;

fn count_trees_from(map: &Vec<Vec<usize>>, x_step: usize, y_step: usize, x_pos: usize, y_pos: usize) -> usize {
    let mut tree_count = 0;
    let mut x_pos_mut = x_pos;
    let mut y_pos_mut = y_pos;
    while y_pos_mut < map.len() {
        if x_pos_mut >= map[0].len() {
            x_pos_mut = x_pos_mut - map[0].len();
        }
        tree_count = tree_count + map[y_pos_mut][x_pos_mut];
        x_pos_mut = x_pos_mut + x_step;
        y_pos_mut = y_pos_mut + y_step;
    }
    tree_count
}

fn read_input() -> Vec<Vec<usize>> {
    let input_values: Vec<Vec<usize>> = stdin()
        .lock()
        .lines()
        .filter_map(|line_result| line_result.ok()) 
        .filter_map(|line| line.parse::<String>().ok())
        .map(|line| line.chars()
            .map(|c| if c == '#' {
                1
            } else {
                0
            }).collect::<Vec<usize>>())
        .collect();      
        input_values                               
}

fn main() {

    println!("Ok let's see how many trees we encounter");
    
    let map = read_input();

    let n_trees = count_trees_from(&map, 3, 1, 0, 0);

    println!("There are {} trees to reach the bottom of the map", n_trees);

    let slopes = vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];

    let n_trees_per_slope: Vec<usize> = slopes.iter().map(|slope| {
        let (x_step, y_step) = slope;
        count_trees_from(&map, *x_step, *y_step, 0, 0)
    }).collect();

    println!("Trees per slope: {:?}", n_trees_per_slope);

    let target = n_trees_per_slope.into_iter().reduce(|a, b| a * b);

    println!("Solution: {:?}", target);
    
}