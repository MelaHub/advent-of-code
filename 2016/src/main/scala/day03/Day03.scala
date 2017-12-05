package day03

import java.io.InputStream

import scala.annotation.tailrec
import scala.io.Source


object Day03 {

  @tailrec
  private def checkTriangleGroupsRec(leftTriangles: List[Shape], validTriangles: Int) =
    leftTriangles match {
      case a :: b :: c :: _ => (a.lengths, b.lengths, c.lengths).zipped.toList.map(l => Shape(l.productIterator.toSeq))
      case _ => validTriangles
    }

  def checkTriangleGroups(): Int = getInputTriangles()

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
