package day02

import java.io.InputStream

import day01.Coordinates

import scala.annotation.tailrec
import scala.io.Source


object Day02 {

  val KEYPAD = Map[Coordinates, String](
    Coordinates(-1, 1) -> "1",
    Coordinates(0, 1) -> "2",
    Coordinates(1, 1) -> "3",
    Coordinates(-1, 0) -> "4",
    Coordinates(0, 0) -> "5",
    Coordinates(1, 0) -> "6",
    Coordinates(-1, -1) -> "7",
    Coordinates(0, -1) -> "8",
    Coordinates(1, -1) -> "9"
  )

  @tailrec
  def bathroomCodeRecFn(currentCoordinate: Coordinates, currentInstruction: List[Move], remainingInstructionList: List[List[Move]], partialCode: String): String = {
    def newCode = s"$partialCode${KEYPAD.getOrElse(currentCoordinate, throw new IllegalArgumentException(s"No key found for coordinate $currentCoordinate"))}"
    if (currentInstruction.isEmpty && remainingInstructionList.isEmpty)
      newCode
    else
      if (currentInstruction.isEmpty)
        bathroomCodeRecFn(currentCoordinate, remainingInstructionList.head, remainingInstructionList.tail, newCode)
      else
        bathroomCodeRecFn(currentInstruction.head.move(currentCoordinate), currentInstruction.tail, remainingInstructionList, partialCode)
  }

  def bathroomCodeRec(instructionsList: List[List[Move]]): String =
    bathroomCodeRecFn(Coordinates(0, 0), instructionsList.head, instructionsList.tail, "")

  def bathroomCode(): String = bathroomCodeRec(getInputInstructions)

  private def getInputInstructions(): List[List[Move]] = {
    val resource: InputStream = this.getClass.getClassLoader.getResourceAsStream("day02_input")
    val source = Source.fromInputStream(resource)
    source
      .getLines()
      .map(
        row =>
          row.map(
            direction =>
              direction match {
                case 'U' => MoveUp
                case 'D' => MoveDown
                case 'L' => MoveLeft
                case 'R' => MoveRight
              }
          ).toList
        )
      .toList
  }
}
