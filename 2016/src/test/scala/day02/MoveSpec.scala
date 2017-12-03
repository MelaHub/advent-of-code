package day02

import day01.Coordinates
import org.scalatest._

class MoveSpec
  extends FlatSpec
    with Matchers {

  "The MoveRight object" should "move to the right" in {
    MoveRight.move(Coordinates(-1, 0), GRID_KEYPAD) shouldEqual Coordinates(0, 0)
    MoveRight.move(Coordinates(0, 0), GRID_KEYPAD) shouldEqual Coordinates(1, 0)
    MoveRight.move(Coordinates(1, 0), GRID_KEYPAD) shouldEqual Coordinates(1, 0)
  }
  "The MoveUp object" should "move up" in {
    MoveUp.move(Coordinates(0, -1), GRID_KEYPAD) shouldEqual Coordinates(0, 0)
    MoveUp.move(Coordinates(0, 0), GRID_KEYPAD) shouldEqual Coordinates(0, 1)
    MoveUp.move(Coordinates(0, 1), GRID_KEYPAD) shouldEqual Coordinates(0, 1)
  }
  "The MoveDown object" should "move down" in {
    MoveDown.move(Coordinates(0, -1), GRID_KEYPAD) shouldEqual Coordinates(0, -1)
    MoveDown.move(Coordinates(0, 0), GRID_KEYPAD) shouldEqual Coordinates(0, -1)
    MoveDown.move(Coordinates(0, 1), GRID_KEYPAD) shouldEqual Coordinates(0, 0)
  }
  "The MoveLeft object" should "move to the left" in {
    MoveLeft.move(Coordinates(-1, 0), GRID_KEYPAD) shouldEqual Coordinates(-1, 0)
    MoveLeft.move(Coordinates(0, 0), GRID_KEYPAD) shouldEqual Coordinates(-1, 0)
    MoveLeft.move(Coordinates(1, 0), GRID_KEYPAD) shouldEqual Coordinates(0, 0)
  }

}
