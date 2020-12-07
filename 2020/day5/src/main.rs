use std::io::{stdin, BufRead};

fn find_val(row: &str, curr_min: usize, curr_max: usize, lower_char: char, upper_char: char) -> usize {
    if row.len() == 0 {
        return curr_min;
    }

    let first_char = row.chars().nth(0);

    match first_char {
        Some(c) if c == lower_char => find_val(&row[1..], curr_min, (curr_min + curr_max) / 2, lower_char, upper_char),
        Some(c) if c == upper_char => find_val(&row[1..], (curr_min + curr_max) / 2, curr_max, lower_char, upper_char),
        _ => 0
    }
}

fn find_row(row: &str) -> usize {
    find_val(row, 0, 128, 'F', 'B')
}

fn find_col(row: &str) -> usize {
    find_val(row, 0, 8, 'L', 'R')
}

fn find_seat_id(seat: &str) -> usize {
    let row_str = &seat[0..7];
    let col_str = &seat[7..10];

    let row = find_row(row_str);
    let col = find_col(col_str);

    row * 8 + col
}

fn read_input() -> Vec<String> {
    let input_lines: Vec<String> = stdin()
        .lock()
        .lines()
        .filter_map(|line_result| line_result.ok()) 
        .filter_map(|line| line.parse().ok())       
        .collect();

    input_lines
}


fn main() {

    println!("Let's check those seats ✈️");
    
    let input_seats = read_input();

    println!("There are {} seats", input_seats.len());

    let mut all_ids: Vec<usize> = input_seats.iter().map(|seat| find_seat_id(seat)).collect();

    let max_id = all_ids.iter().max();

    println!("And the highest id is {:?}", max_id);

    all_ids.sort();
    
    let mut seat_id = 0;
    for i in 1..all_ids.len() {
        if all_ids[i - 1] == all_ids[i] - 2 {
            seat_id = all_ids[i - 1] + 1;
            break
        } 
    }

    println!("The only free seat is {}", seat_id);
    
}
