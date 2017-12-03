package day01

import org.scalatest._


class GetFinalPositionSpec
  extends FlatSpec
  with Matchers {

  "Moving in a diagonal direction" should "work" in {
    Day01.getFinalPositionFromStart(List(MoveRight) ++ Step(2) ++ List(MoveLeft) ++ Step(3)) shouldEqual Position(2, 3, North)
  }

  "Moving in a 3/4 circle" should "work" in {
    Day01.getFinalPositionFromStart(List(MoveRight) ++ Step(2) ++ List(MoveRight) ++ Step(2) ++ List(MoveRight) ++ Step(2)) shouldEqual Position(0, -2, West)
  }

  "Multisteps" should "work" in {
    Day01.getFinalPositionFromStart(List(MoveRight) ++ Step(5) ++ List(MoveLeft) ++ Step(5) ++ List(MoveRight) ++ Step(5) ++ List(MoveRight) ++ Step(3)) shouldEqual Position(10, 2, South)
  }
}
