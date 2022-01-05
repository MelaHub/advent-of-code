package day06

import org.scalatest._
import flatspec._
import matchers._

class MessageBagSpec extends AnyFlatSpec with should.Matchers {

  private val testInput = List(
      "eedadn",
      "drvtee",
      "eandsr",
      "raavrd",
      "atevrs",
      "tsrnev",
      "sdttsa",
      "rasrtv",
      "nssdts",
      "ntnada",
      "svetve",
      "tesnvt",
      "vntsnd",
      "vrdear",
      "dvrsen",
      "enarar"
  )

  private val expectedListChar = List(
    List('e', 'd', 'e'),
    List('e', 'r', 'a'),
    List('d', 'v', 'n'),
    List('a', 't', 'd'),
    List('d', 'e', 's'),
    List('n', 'e', 'r')
  )

  private val expectedListCount = List(
    Map('e' -> 2, 'd' -> 1),
    Map('e' -> 1, 'r' -> 1, 'a' -> 1),
    Map('d' -> 1, 'v' -> 1, 'n' -> 1),
    Map('a' -> 1, 't' -> 1, 'd' -> 1),
    Map('d' -> 1, 'e' -> 1, 's' -> 1),
    Map('n' -> 1, 'e' -> 1, 'r' -> 1)
  )

  "A message bag" should "decompose correctly input messages" in {
    Day06.decomposedValues(testInput.take(3)) should be(expectedListChar)
  }

  "A message bag" should "corectly count the number of chars per column" in {
    (Day06.decomposedValues andThen Day06.counter)(testInput.take(3)) should be(expectedListCount)
  }

  "A message bag" should "correctly retrieve the most occurring char" in {
    (Day06.decomposedValues andThen Day06.counter andThen Day06.mostRelevantLetters)(testInput) should be(List(Some('e'), Some('a'), Some('s'), Some('t'), Some('e'), Some('r')))
  }

  "Day06" should "correctly decode a message" in {
    Day06.findHiddenMostCommonLetterMessage(testInput) should be("easter")
  }
}