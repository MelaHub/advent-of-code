package day01


case class Coordinates(x: Int, y: Int) {
  def +(that: Coordinates): Coordinates = Coordinates(this.x + that.x, this.y + that.y)
}

