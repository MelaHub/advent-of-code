use std::collections::HashMap;
use std::io::{stdin, BufRead};
use std::collections::HashSet;
use lazy_static::lazy_static;
use regex::Regex;

const PASSPORT_REGEX: &str = r"([^ ]+):([^ ]+)";
const HEIGHT_REGEX: &str = r"^(\d+)(cm|in)$";
const HAIR_REGEX: &str = r"^#[0-9a-f]{6}";
const PID_REGEX: &str = r"^[0-9]{9}";

fn byr_validation(year: String) -> bool {
    match year.parse::<usize>() {
        Ok(y) => y >= 1920 && y <= 2002 && year.chars().count() == 4,
        Err(_) => false,
    }
}

fn iyr_validation(year: String) -> bool {
    match year.parse::<usize>() {
        Ok(y) => y >= 2010 && y <= 2020 && year.chars().count() == 4,
        Err(_) => false,
    }
}

fn eyr_validation(year: String) -> bool {
    match year.parse::<usize>() {
        Ok(y) => y >= 2020 && y <= 2030 && year.chars().count() == 4,
        Err(_) => false,
    }
}

fn hgt_validation(height: String) -> bool {
    lazy_static! {
        static ref REGEX: Regex = Regex::new(HEIGHT_REGEX).unwrap();
      }
    let mut valid: bool = false;

    for cap in REGEX.captures_iter(&height) {
        valid = match cap[0].parse::<usize>() {
            Ok(h) => match &cap[1] {
                "cm" => h >= 150 && h <= 193,
                "in" => h >= 59 && h <= 76,
                _ => false
            },
            Err(_) => false
        };
        break
    }
    valid
}

fn hcl_validation(hair: String) -> bool {
    lazy_static! {
        static ref REGEX: Regex = Regex::new(HAIR_REGEX).unwrap();
      }
      REGEX.is_match(&hair)
}

fn ecl_validation(eye: String) -> bool {
    let mut keys = HashSet::new();
    let necessary_keys = vec!["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];

    for key in necessary_keys{
        keys.insert(key.to_string());
    }

    keys.contains(&eye)
}

fn pid_validation(pid: String) -> bool {
    lazy_static! {
        static ref REGEX: Regex = Regex::new(PID_REGEX).unwrap();
      }
      REGEX.is_match(&pid)
}

fn read_input() -> Vec<String> {
    let input_lines: Vec<String> = stdin()
        .lock()
        .lines()
        .filter_map(|line_result| line_result.ok()) 
        .filter_map(|line| line.parse().ok())       
        .collect();

    let mut passports_as_str: Vec<String> = Vec::new();

    let mut curr_passport: String = String::from("");

    for line in input_lines {
        if line.chars().count() == 0 {
            passports_as_str.push(curr_passport);
            curr_passport = String::from("");
        }
        curr_passport.push_str(" ");
        curr_passport.push_str(&line);
    }

    passports_as_str.push(curr_passport);

    passports_as_str
}

fn parse_passport(passports_as_str: Vec<String>) -> Vec<HashMap<String, String>> {

    let mut passports: Vec<HashMap<String, String>> = Vec::new();

    lazy_static! {
        static ref REGEX: Regex = Regex::new(PASSPORT_REGEX).unwrap();
      }
    
    for passport in passports_as_str {
        let mut currHash: HashMap<String, String> = HashMap::new();
        for cap in REGEX.captures_iter(&passport) {
            currHash.insert(String::from(&cap[1]), String::from(&cap[2]));
        }
        passports.push(currHash);
    }

    passports                               
}

fn is_passport_valid(passport: &HashMap<String, String>, mandatory_keys: &HashSet<String>) -> bool {
    let mut passport_keys = HashSet::new();

    for key in passport.keys() {
      passport_keys.insert(key.to_string());
    }
    
    let common_keys: HashSet<_> = mandatory_keys.intersection(&passport_keys).collect();

    common_keys.len() == mandatory_keys.len()
}

fn get_mandatory_keys() -> HashSet<String> {
    let mut keys = HashSet::new();
    let necessary_keys = vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

    for key in necessary_keys{
        keys.insert(key.to_string());
    }

    keys
}

fn main() {

    println!("Passport validation 🕵️‍♀️");
    
    let input_passports_as_str = read_input();
    let input_passports = parse_passport(input_passports_as_str);
    let npassports = input_passports.len();
    
    let mandatory_keys = get_mandatory_keys();
    println!("Check valid passports for keys {:?}", mandatory_keys);

    let valid_passports: Vec<&HashMap<String, String>> = input_passports
      .iter()
      .filter(|passport| is_passport_valid(passport, &mandatory_keys))
      .collect();

    println!("There are {} valid passports on a total of {}", valid_passports.len(), npassports);
    
}
