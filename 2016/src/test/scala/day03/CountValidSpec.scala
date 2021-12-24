package day03

import org.scalatest._
import flatspec._
import matchers._

class CountValidSpec
  extends AnyFlatSpec
    with should.Matchers {

  "The count object" should "count the valid triangles in input" in {
    Day03.checkTrianglesInRows() shouldEqual 0
  }

  "The count object" should "count the valid group triangles in input" in {
    Day03.checkTriangleGroups() shouldEqual 0
  }
}
