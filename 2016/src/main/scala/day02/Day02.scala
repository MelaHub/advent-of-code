package day02

import java.io.InputStream

import day01.Coordinates

import scala.annotation.tailrec
import scala.io.Source


object Day02 {

  @tailrec
  def bathroomCodeRecFn(keypad: Map[Coordinates, String], currentCoordinate: Coordinates, currentInstruction: List[Move], remainingInstructionList: List[List[Move]], partialCode: String): String = {
    def newCode = s"$partialCode${keypad.getOrElse(currentCoordinate, throw new IllegalArgumentException(s"No key found for coordinate $currentCoordinate"))}"
    if (currentInstruction.isEmpty && remainingInstructionList.isEmpty)
      newCode
    else
      if (currentInstruction.isEmpty)
        bathroomCodeRecFn(keypad, currentCoordinate, remainingInstructionList.head, remainingInstructionList.tail, newCode)
      else
        bathroomCodeRecFn(keypad, currentInstruction.head.move(currentCoordinate, keypad), currentInstruction.tail, remainingInstructionList, partialCode)
  }

  def bathroomCodeRec(keypad: Map[Coordinates, String], instructionsList: List[List[Move]]): String =
    bathroomCodeRecFn(keypad, Coordinates(0, 0), instructionsList.head, instructionsList.tail, "")

  def bathroomCode(): String = bathroomCodeRec(GRID_KEYPAD, getInputInstructions)

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
