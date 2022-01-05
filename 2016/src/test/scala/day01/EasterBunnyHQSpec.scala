package day01

import org.scalatest._
import flatspec._
import matchers._


class EasterBunnyHQSpec
  extends AnyFlatSpec
    with should.Matchers {

  "EasterBunnyHQ" should "get the distance of the HQ" in {
    Day01.easterBunnyHQDistanceFromMoves(List(MoveRight) ::: Step(2) ::: List(MoveLeft) ::: Step(3)) shouldEqual 5
    Day01.easterBunnyHQDistanceFromMoves(List(MoveRight) ::: Step(2) ::: List(MoveRight) ::: Step(2) ::: List(MoveRight) ::: Step(2)) shouldEqual 2
    Day01.easterBunnyHQDistanceFromMoves(List(MoveRight) ::: Step(5) ::: List(MoveLeft) ::: Step(5) ::: List(MoveRight) ::: Step(5) ::: List(MoveRight) ::: Step(3)) shouldEqual 12
  }

  "EasterBunnyHQ" should "get the distance of the HQ stopping at the first visited node" in {
    Day01.easterBunnyHQDistanceLoopFromMoves(List(MoveRight) ::: Step(8) ::: List(MoveRight) ::: Step(4) ::: List(MoveRight) ::: Step(4) ::: List(MoveRight) ::: Step(8)) shouldEqual 4
  }
}
