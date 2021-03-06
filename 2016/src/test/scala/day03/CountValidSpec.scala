package day03

import org.scalatest._

class CountValidSpec
  extends FlatSpec
    with Matchers {

  "The count object" should "count the valid triangles in input" in {
    Day03.checkTriangles() shouldEqual 0
  }

  "The count object" should "count the valid group triangles in input" in {
    Day03.checkTriangleGroups() shouldEqual 0
  }
}
