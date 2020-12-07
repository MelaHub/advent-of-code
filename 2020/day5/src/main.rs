use std::io::{stdin, BufRead};

fn find_val(row &str, curr_min: usize, curr_max: usize, lower_char: char, upper_char: char) -> usize {

}

fn find_row(row: &str, curr_min: usize, curr_max: usize) -> usize{
    if row.len() == 0 {
        return curr_min;
    }

    let first_char = row.chars().nth(0);

    match first_char {
        Some('F') => find_row(&row[1..], curr_min, (curr_min + curr_max) / 2),
        Some('B') => find_row(&row[1..], (curr_min + curr_max) / 2, curr_max),
        _ => 0
    }

}

fn find_col(row: &str, curr_min: usize, curr_max: usize) -> usize{
    if row.len() == 0 {
        return curr_min;
    }

    let first_char = row.chars().nth(0);
    
    match first_char {
        Some('L') => find_col(&row[1..], curr_min, (curr_min + curr_max) / 2),
        Some('R') => find_col(&row[1..], (curr_min + curr_max) / 2, curr_max),
        _ => 0
    }
}

fn find_seat_id(seat: &str) -> usize {
    let row_str = &seat[0..7];
    let col_str = &seat[7..10];

    let row = find_row(row_str, 0, 128);
    let col = find_col(col_str, 0, 8);

    println!("Original {}, row {}, col {}: {}-{}", seat, row_str, col_str, row, col);
    0
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

    println!("Let's check those seats 🕵️‍♀️");
    
    let input_seats = read_input();

    println!("There are {} seats", input_seats.len());

    for seat in input_seats {
        find_seat_id(&seat);
    }
    
}
