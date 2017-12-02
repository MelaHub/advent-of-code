package day01

import org.scalatest._


class StopAtFirstLoopSpec
  extends FlatSpec
    with Matchers {

  "Stops at first loop " should "stop when a node already visited has been found" in {
    Day01.stopAtFirstLoop(List(MoveRight) ++ Step(8) ++ List(MoveRight) ++ Step(4) ++ List(MoveRight) ++ Step(4) ++ List(MoveRight) ++ Step(8)) shouldEqual(Position(4, 0, North))
  }

}
