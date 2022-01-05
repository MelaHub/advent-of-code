package day01

import org.scalatest._
import flatspec._
import matchers._

class MoveSpec
  extends AnyFlatSpec
    with should.Matchers {

  "The MoveLeft object" should "move to the left" in {
    MoveLeft.move(Position(0, 0, North)) shouldEqual Position(0, 0, West)
    MoveLeft.move(Position(0, 0, West)) shouldEqual Position(0, 0, South)
    MoveLeft.move(Position(0, 0, South)) shouldEqual Position(0, 0, East)
    MoveLeft.move(Position(0, 0, East)) shouldEqual Position(0, 0, North)
  }

  "The MoveRight object" should "move to the right" in {
    MoveRight.move(Position(0, 0, North)) shouldEqual Position(0, 0, East)
    MoveRight.move(Position(0, 0, West)) shouldEqual Position(0, 0, North)
    MoveRight.move(Position(0, 0, South)) shouldEqual Position(0, 0, West)
    MoveRight.move(Position(0, 0, East)) shouldEqual Position(0, 0, South)
  }

  "The step object" should "step in the right direction" in {
    Step.move(Position(0, 0, North)) shouldEqual Position(0, 1, North)
    Step.move(Position(0, 0, West)) shouldEqual Position(-1, 0, West)
    Step.move(Position(0, 0, South)) shouldEqual Position(0, -1, South)
    Step.move(Position(0, 0, East)) shouldEqual Position(1, 0, East)
  }

}
