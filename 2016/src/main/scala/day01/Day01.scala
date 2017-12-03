package day01

import java.io.InputStream

import scala.annotation.tailrec
import scala.io.Source

object Day01 {

  val startingPosition = Position(Coordinates(0, 0), North)

  private[day01] def getFinalPositionFromStart(directions: List[Move]): Position =
    directions.foldLeft(startingPosition)((p, move) => move.move(p))

  private[day01] def getDistanceFromStart(endPosition: Position): Int =
    Math.abs(startingPosition.x - endPosition.x) + Math.abs(startingPosition.y - endPosition.y)

  @tailrec
  private def stopAtFirstLoopAcc(currentPosition: Position, futureDirections: List[Move], visitedNodes: Set[Coordinates]): Position =
    futureDirections.headOption match {
      case None => currentPosition
      case Some(move) =>
        val nextPos = move.move(currentPosition)
        move match {
          case Step if (visitedNodes.contains(nextPos.coordinates)) => nextPos
          case _ => stopAtFirstLoopAcc(nextPos, futureDirections.tail, visitedNodes + nextPos.coordinates)
        }
    }

  def stopAtFirstLoop(directions: List[Move]): Position = stopAtFirstLoopAcc(startingPosition, directions, Set())

  def easterBunnyHQDistance(): Int = getDistanceFromStart(getFinalPositionFromStart(getInputDirections()))

  def easterBunnyHQDistanceLoop(): Int = getDistanceFromStart(stopAtFirstLoop(getInputDirections()))

  private def getInputDirections(): List[Move] = {
    val resource: InputStream = this.getClass.getClassLoader.getResourceAsStream("day01_input")
    val source = Source.fromInputStream(resource)
    source
      .getLines()
      .flatMap(
        row =>
          row.split(','))
      .flatMap(direction =>
        direction.trim match {
          case d if d.startsWith("R") => MoveRight :: (1 to d.stripPrefix("R").toInt).map(_ => Step).toList
          case d if d.startsWith("L") => MoveLeft :: (1 to d.stripPrefix("L").toInt).map(_ => Step).toList
          case _ => throw new IllegalArgumentException(s"$direction is not a valid direction")
        })
      .toList
  }

}

