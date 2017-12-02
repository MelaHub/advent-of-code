package day01

import org.scalatest._


class GetDistanceSpec
  extends FlatSpec
  with Matchers {

  "Moving in a diagonal direction" should "work" in {
    Day01.getDistanceFromStart(Position(2, 3, North)) shouldEqual 5
  }

  "Moving in a 3/4 circle" should "work" in {
    Day01.getDistanceFromStart(Position(0, -2, West)) shouldEqual 2
  }

  "Multisteps" should "work" in {
    Day01.getDistanceFromStart(Position(10, 2, South)) shouldEqual 12
  }
}
