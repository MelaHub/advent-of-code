package day03

import java.io.InputStream

import scala.io.Source


object Day03 {

  def checkTriangles(): Int = getInputTriangles.count(_.is_a_valid_triangle)

  private def getInputTriangles(): List[Shape] = {
    val resource: InputStream = this.getClass.getClassLoader.getResourceAsStream("day03_input")
    val source = Source.fromInputStream(resource)
    source
      .getLines()
      .map(
        row => Shape(row.split(' ').filter(_.length > 0).map(_.toInt).toList)
        )
      .toList
  }
}
