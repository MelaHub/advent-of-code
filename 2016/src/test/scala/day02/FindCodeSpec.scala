package day02

import day01.Coordinates
import org.scalatest._

class FindCodeSpec
  extends FlatSpec
    with Matchers {

  "The find code object" should "find the correct code in a grid keypad" in {
    Day02.bathroomCodeRec(GRID_KEYPAD, List(List(MoveUp, MoveLeft, MoveLeft))) shouldEqual "1"
    Day02.bathroomCodeRec(
      GRID_KEYPAD,
      List(
        List(MoveUp, MoveLeft, MoveLeft),
        List(MoveRight, MoveRight, MoveDown, MoveDown, MoveDown),
        List(MoveLeft, MoveUp, MoveRight, MoveDown, MoveLeft),
        List(MoveUp, MoveUp, MoveUp, MoveUp, MoveDown))) shouldEqual "1985"
  }

  "The find code object" should "find the solution to the input" in {
    Day02.bathroomCode() shouldEqual "74921"
  }
}
