package day01

sealed trait Direction {
  val direction: Coordinates
}

case object North extends Direction {
  val direction = Coordinates(0, 1)
}

case object South extends Direction {
  val direction = Coordinates(0, -1)
}

case object West extends Direction {
  val direction = Coordinates(-1, 0)
}

case object East extends Direction {
  val direction = Coordinates(1, 0)
}
