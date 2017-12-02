import Dependencies._

lazy val root = (project in file(".")).
  settings(
    inThisBuild(List(
      version := "0.13.15",
      organization := "com.example",
      scalaVersion := "2.11.11",
      version      := "0.1.0-SNAPSHOT"
    )),
    name := "advent2016",
    libraryDependencies += scalaTest % Test
  )
