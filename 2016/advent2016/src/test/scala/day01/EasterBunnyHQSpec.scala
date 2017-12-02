package day01

import org.scalatest._


class EasterBunnyHQSpec
  extends FlatSpec
  with Matchers {

  "EasterBunnyHQ" should "get the distance of the HQ" in {
    Day01.easterBunnyHQDistance() shouldEqual 234
  }

  "EasterBunnyHQ" should "get the distance of the HQ stopping at the first visited node" in {
    Day01.easterBunnyHQDistanceLoop() shouldEqual 113
  }
}
