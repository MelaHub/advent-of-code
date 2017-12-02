package day01

import scala.annotation.tailrec
import scala.math.abs

case class Vec(u: Double, v: Double) {
  def rotateLeft: Vec = Vec(-v, u)
  def rotateRight: Vec = Vec(v, -u)
}

case class Point(x: Double, y: Double) {
  def +(dir: Vec): Point = Point(x + dir.u, y + dir.v)
  def dist(that: Point): Double = abs(x - that.x) + abs(y - that.y)
}

object Day1 extends App {
  @tailrec
  def followGuide(start: Point, dir: Vec, guide: List[Char],
                  visited: Set[Point], HQ: Option[Point]): (Point, Option[Point]) = {
    guide match {
      case Nil => (start, HQ)
      case face :: rest => {
        val new_dir = (face: @unchecked) match {
          case 'L' => dir.rotateLeft
          case 'R' => dir.rotateRight
          case 'S' => dir
        }
        val dest = start + new_dir
        val new_HQ = if (HQ.isDefined ||
          !visited.contains(dest)) HQ else Some(dest)

        followGuide(dest, new_dir, rest, visited + dest, new_HQ)
      }
    }
  }

  def expand(step: String): List[Char] =
    step.head :: List.fill(step.tail.toInt - 1)('S')

  val input = "R8, R4, R4, R8"
  val guide = input.split(", ").toList.map(expand).flatten
  val start = Point(0, 0)

  followGuide(start, Vec(0, 1), guide, Set(start), None) match {
    case (dest, hq) => {
      println("start to destination: " + dest.dist(start))
      if (hq.isEmpty) println("HQ does not exist")
      else println("start to HQ: " + hq.get.dist(start))
    }
  }
}
