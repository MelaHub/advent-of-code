use std::collections::HashMap;
use std::io::{stdin, BufRead};
use std::collections::HashSet;
use lazy_static::lazy_static;
use regex::Regex;

const PASSPORT_REGEX: &str = r"([^ ]+):([^ ]+)";

fn read_input() -> Vec<HashMap<String, String>> {
    let input_lines: Vec<String> = stdin()
        .lock()
        .lines()
        .filter_map(|line_result| line_result.ok()) 
        .filter_map(|line| line.parse().ok())       
        .collect();

    let mut currHash: HashMap<String, String> = HashMap::new();
    let mut passports: Vec<HashMap<String, String>> = Vec::new();

    lazy_static! {
        static ref REGEX: Regex = Regex::new(PASSPORT_REGEX).unwrap();
      }
    
    for line in input_lines {
        if line.chars().count() == 0 {
          passports.push(currHash);
          currHash = HashMap::new();
        }
        for cap in REGEX.captures_iter(&line) {
            currHash.insert(String::from(&cap[1]), String::from(&cap[2]));
        }
    }
    passports.push(currHash);
    currHash = HashMap::new();

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
    
    let input_passports = read_input();
    let npassports = input_passports.len();
    
    let mandatory_keys = get_mandatory_keys();
    println!("Check valid passports for keys {:?}", mandatory_keys);

    let valid_passports: Vec<&HashMap<String, String>> = input_passports
      .iter()
      .filter(|passport| is_passport_valid(passport, &mandatory_keys))
      .collect();

    println!("There are {} valid passports on a total of {}", valid_passports.len(), npassports);
    
}
