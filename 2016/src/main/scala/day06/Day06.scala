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

  def mostRelevantLetters(seqCounters: List[Map[Char, Int]])(implicit sortingCount: ((Char, Int)) => Int, ord: Ordering[Int]): List[Option[Char]] = seqCounters
    .map(
      _.toList.sortBy { sortingCount }.take(1).headOption.map { case (currChar, _) => currChar}
    )

  def findHiddenMessageLetters(messages: List[String])(implicit sortingCount: ((Char, Int)) => Int, ord: Ordering[Int]): String =
    (decomposedValues andThen counter andThen mostRelevantLetters)(messages).flatten.mkString

  def findHiddenMessageMostCommonLetter: List[String] => String = messages => {
    implicit def mostCommonLetters: ((Char, Int)) => Int = {case (_, count) => (-count)}
    findHiddenMessageLetters(messages)
  }

  def findHiddenMessageLeaseCommonLetter: List[String] => String = messages => {
    implicit def leastCommonLetters: ((Char, Int)) => Int = {case (_, count) => (count)}
    findHiddenMessageLetters(messages)
  }

  private def getInputMessages(): List[String] = {
    val resource: InputStream = this.getClass.getClassLoader.getResourceAsStream("day06_input")
    Source.fromInputStream(resource).getLines().toList
  }

  println(s"The hidden message with most common letter is is: ${findHiddenMessageMostCommonLetter(getInputMessages())}")
  println(s"The hidden message with least common letter is is: ${findHiddenMessageLeaseCommonLetter(getInputMessages())}")

}
