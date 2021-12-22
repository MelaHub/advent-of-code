package day03

import java.io.InputStream

import scala.annotation.tailrec
import scala.io.Source


object Day03 extends App {

  @tailrec
  private def checkTriangleGroupsRec(leftTriangles: List[Shape], validTriangles: Int): Int =
    leftTriangles match {
      case a :: b :: c :: _ =>
        val validGroupTriangles = (a.lengths, b.lengths, c.lengths).zipped.toList.map((l: (Int, Int, Int)) => Shape(l.productIterator.toSeq.map(_.toString.toInt).toList)).map(_.is_a_valid_triangle).count(identity)
        checkTriangleGroupsRec(leftTriangles.drop(3), validTriangles + validGroupTriangles)
      case _ => validTriangles
    }

  def checkTriangleGroups(): Int = checkTriangleGroupsRec(getInputTriangles(), 0)

  def checkTrianglesInRows(): Int = getInputTriangles.count(_.is_a_valid_triangle)

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

  println(s"Number of triangles per rows ${checkTrianglesInRows()}")
  println(s"Number of triangles groups ${checkTriangleGroups()}")

}
