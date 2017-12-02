package day01

trait Move {

  def move(startPosition: Position): Position

}

case object MoveRight extends Move {

  def move(startPosition: Position): Position =
    startPosition.facing match {
      case South => startPosition.copy(facing=West)
      case East => startPosition.copy(facing=South)
      case North => startPosition.copy(facing=East)
      case West => startPosition.copy(facing=North)
    }

}

case object MoveLeft extends Move {

  def move(startPosition: Position): Position =
    startPosition.facing match {
      case North => startPosition.copy(facing=West)
      case West => startPosition.copy(facing=South)
      case South => startPosition.copy(facing=East)
      case East => startPosition.copy(facing=North)
    }

}

case object Step extends Move {

  def move(startPosition: Position): Position =
    startPosition.copy(coordinates = startPosition.coordinates + startPosition.facing.direction)

  def apply(n: Int) = (1 to n).map(_ => Step).toList

}
