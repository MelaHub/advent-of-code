import day01.Coordinates

package object day02 {

  val GRID_KEYPAD = Map[Coordinates, String](
    Coordinates(-1, 1) -> "1",
    Coordinates(0, 1) -> "2",
    Coordinates(1, 1) -> "3",
    Coordinates(-1, 0) -> "4",
    Coordinates(0, 0) -> "5",
    Coordinates(1, 0) -> "6",
    Coordinates(-1, -1) -> "7",
    Coordinates(0, -1) -> "8",
    Coordinates(1, -1) -> "9"
  )

  val STAR_KEYPAD = Map[Coordinates, String](
    Coordinates(0, 0) -> "5",
    Coordinates(1, 1) -> "2",
    Coordinates(1, 0) -> "6",
    Coordinates(1, -1) -> "A",
    Coordinates(2, 2) -> "1",
    Coordinates(2, 1) -> "3",
    Coordinates(2, 0) -> "7",
    Coordinates(2, -1) -> "B",
    Coordinates(2, -2) -> "D",
    Coordinates(3, 1) -> "4",
    Coordinates(3, 0) -> "8",
    Coordinates(3, -1) -> "C",
    Coordinates(4, 0) -> "9"
  )

}
