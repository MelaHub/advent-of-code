package day03

import day01.Coordinates
import org.scalatest._
import flatspec._
import matchers._

class TriangleSpec
  extends AnyFlatSpec
    with should.Matchers {

  "The triangle object" should "recognize a valid triangle" in {
    Shape(Seq(5, 10, 25)).is_a_valid_triangle shouldEqual false
    Shape(Seq(16, 10, 25)).is_a_valid_triangle  shouldEqual true
    Shape(Seq(1, 2, 3, 4)).is_a_valid_triangle  shouldEqual false
  }

}
