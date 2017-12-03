package day02

import day01.Coordinates

trait Move {

  def newPosition(startPosition: Coordinates): Coordinates

  def move(startPosition: Coordinates, keyPad: Map[Coordinates, String]): Coordinates = {
    val pos = newPosition(startPosition)
    keyPad.get(pos) match {
      case None => startPosition
      case Some(value) => pos
    }
  }

}

case object MoveRight extends Move {

  def newPosition(startPosition: Coordinates): Coordinates = startPosition.copy(x=startPosition.x+1)

}

case object MoveUp extends Move {

  def newPosition(startPosition: Coordinates): Coordinates = startPosition.copy(y=startPosition.y+1)

}

case object MoveLeft extends Move {

  def newPosition(startPosition: Coordinates): Coordinates = startPosition.copy(x=startPosition.x-1)

}

case object MoveDown extends Move {

  def newPosition(startPosition: Coordinates): Coordinates = startPosition.copy(y=startPosition.y-1)

}

