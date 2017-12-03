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

}
