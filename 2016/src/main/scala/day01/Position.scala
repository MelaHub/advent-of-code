package day01


case class Position(coordinates: Coordinates, facing: Direction) {
  val x: Int = coordinates.x
  val y: Int = coordinates.y
}

object Position {
  def apply(x: Int, y: Int, facing: Direction): Position = Position(Coordinates(x, y), facing)
}

