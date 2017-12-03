package day02

import day01.Coordinates

trait Move {

  def move(startPosition: Coordinates): Coordinates

}

case object MoveRight extends Move {

  def move(startPosition: Coordinates): Coordinates =
    if (startPosition.x < 1)
      startPosition.copy(x=startPosition.x+1)
    else
      startPosition

}

case object MoveUp extends Move {

  def move(startPosition: Coordinates): Coordinates =
    if (startPosition.y < 1)
      startPosition.copy(y=startPosition.y+1)
    else
      startPosition

}

case object MoveLeft extends Move {

  def move(startPosition: Coordinates): Coordinates =
    if (startPosition.x > -1)
      startPosition.copy(x=startPosition.x-1)
    else
      startPosition

}

case object MoveDown extends Move {

  def move(startPosition: Coordinates): Coordinates =
    if (startPosition.y > -1)
      startPosition.copy(y=startPosition.y-1)
    else
      startPosition

}

