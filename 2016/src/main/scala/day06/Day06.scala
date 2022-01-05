package day06

import java.io.InputStream
import scala.io.Source

object Day06 extends App {

  def decomposedValues: List[String] => List[List[Char]] = messages => messages
    .foldLeft(List.empty[List[Char]]){
      case (currBag, message) =>
        message.zipAll(currBag, '-', List.empty[Char])
          .map {
            case (currChar, currBag) => currBag :+ currChar
          }.toList
    }

  def counter: List[List[Char]] => List[Map[Char, Int]] = values => values
    .map(
      _.groupBy(identity)
        .map {
          case (currChar, listChars) => currChar -> listChars.size
        })

  def mostCommonLetters: List[Map[Char, Int]] => List[Option[Char]] = seqCounters => seqCounters
    .map(
      _.toList.sortBy { case (_, count) => -count }.take(1).headOption.map { case (currChar, _) => currChar}
    )

  def findHiddenMessage: List[String] => String = messages => (decomposedValues andThen counter andThen mostCommonLetters)(messages).flatten.mkString

  private def getInputMessages(): List[String] = {
    val resource: InputStream = this.getClass.getClassLoader.getResourceAsStream("day06_input")
    Source.fromInputStream(resource).getLines().toList
  }

  println(s"The hidden message is: ${findHiddenMessage(getInputMessages())}")

}
