use std::collections::HashMap;
use std::io::{stdin, BufRead};
use std::collections::HashSet;
use lazy_static::lazy_static;
use regex::Regex;

const PASSPORT_REGEX: &str = r"([^ ]+):([^ ]+)";

// fn validate_birth_year(year: String): Result<usize, ParseIntError> {

// }
// byr (Birth Year) - four digits; at least 1920 and at most 2002.
// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
// hgt (Height) - a number followed by either cm or in:
// If cm, the number must be at least 150 and at most 193.
// If in, the number must be at least 59 and at most 76.
// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
// pid (Passport ID) - a nine-digit number, including leading zeroes.
// cid (Country ID) - ignored, missing or not.

// struct Passport {
//     byr: usize,
//     iyr: usize,
//     eyr: usize,
//     hgt: str,
//     hcl: str,
//     ecl: str,
//     pid: str,
// }

// impl Passport {
//     type Err = ParsePassportError;

//     fn from_hash(input_hash: &HashMap<String, String>) -> Result<Passport, Self::Err> {

//     }
// }

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
