package day04

case class Room(encryptedName: String, sectorId: Int, checksum: String) {

  private val lettersAlphabet = 26

  lazy val isReal: Boolean = encryptedName
    .filterNot(_ == '-')
    .groupBy(identity)
    .mapValues(_.length)
    .toList
    .sortBy{ case (c, l) => (-l, c)}
    .take(5)
    .map(_._1)
    .mkString == checksum

  lazy val cipherRotation = sectorId % lettersAlphabet

  lazy val realName = encryptedName
      .map{
        case c if c == '-' => c
        case c => (c.toInt + cipherRotation match {
          case x if x <= 'z'.toInt => x
          case x => x - lettersAlphabet
        }).toChar
      }.mkString


}


