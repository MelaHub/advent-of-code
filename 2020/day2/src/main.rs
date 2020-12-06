use regex::Regex;
use lazy_static::lazy_static;
use std::{
    fmt::{self, Display, Formatter},
    error::Error,
    num::ParseIntError,
    str::FromStr,
    io::{stdin, BufRead},
    char::ParseCharError,
    convert::Infallible,
  };
  

const POLICY_REGEX: &str = r"^(\d+)-(\d+) ([a-z]): ([a-z]+)";

#[derive(Debug, Clone)]
struct ParsePolicyError;

impl Display for ParsePolicyError {
  fn fmt(&self, f: &mut Formatter) -> fmt::Result {
    write!(f, "Unable to parse to a Policy.")
  }
}

impl Error for ParsePolicyError {
  fn description(&self) -> &str {
    "Unable to parse to a Policy."
  }

  fn cause(&self) -> Option<&Error> {
    None
  }
}

impl From<ParseIntError> for ParsePolicyError {
  fn from(_error: ParseIntError) -> Self {
    ParsePolicyError
  }
}

impl From<ParseCharError> for ParsePolicyError {
    fn from(_error: ParseCharError) -> Self {
        ParsePolicyError
      }
}

impl From<Infallible> for ParsePolicyError {
    fn from(_error: Infallible) -> Self {
        ParsePolicyError
      }
}

#[derive(Debug)]
struct Policy {
    min: usize,
    max: usize,
    letter: char,
    pass: String,
}

impl Policy {
    fn is_valid_policy1(&self) -> bool {
        let check_n_letter = self.pass.chars().filter(|a| *a == self.letter).count();
        check_n_letter >= self.min && check_n_letter <= self.max
    }
    fn is_valid_policy2(&self) -> bool {
        let first_check = match self.pass.chars().nth(self.min - 1){
            Some(letter) => letter == self.letter,
            None => false,
        };
        let second_check = match self.pass.chars().nth(self.max - 1){
            Some(letter) => letter == self.letter,
            None => false,
        };
        first_check ^ second_check
    }
}

impl FromStr for Policy {
    type Err = ParsePolicyError;

    fn from_str(policy_str: &str) -> Result<Self, Self::Err> {
        lazy_static! {
            static ref REGEX: Regex = Regex::new(POLICY_REGEX).unwrap();
          }
      
      
        REGEX.captures(policy_str)
            .ok_or(ParsePolicyError)
            .and_then(|cap| {
                Ok(Policy {
                min: cap[1].parse()?,
                max: cap[2].parse()?,
                letter: cap[3].parse()?,
                pass: cap[4].parse()?
            })})
    }
}

fn read_input() -> Vec<Policy> {
    let input_values: Vec<Policy> = stdin()
        .lock()
        .lines()
        .filter_map(|line_result| line_result.ok()) 
        .filter_map(|line| line.parse().ok())       
        .collect();  
    input_values                               
}

fn main() {

    println!("Ready to find the number of wrong policies");
    
    let input_values = read_input();
    let npolicies = input_values.len();

    let valid_passwords_policy1: Vec<&Policy> = input_values.iter().filter(|policy| policy.is_valid_policy1()).collect();
    let valid_passwords_policy2: Vec<&Policy> = input_values.iter().filter(|policy| policy.is_valid_policy2()).collect();

    println!("Out of {} policies, only {} are valid according to the first policy, and {} according to the second", npolicies, valid_passwords_policy1.len(), valid_passwords_policy2.len());
    
}
