# Welcome to Sparky

[![Code Climate](https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg)](https://codeclimate.com/github/CZDiego/Sparky-Programming-Language)

Sparky is an object oriented programming language developed for the class of compilers in Tec de Monterrey. It has variables of atomic types (Int, Bool and Float), arrays and matrix of atomics and also custom class types, functions, and more.

## Structure of a program

```
//Hello world program in Sparky

main () {
  print("Hello World!");
}
```

The main block, is the part that is going to be executed first. To declare a variable the syntaxis is:

```
var name : Int;
var price : Float;
var is_object : Bool;
var arr : [10]Int;
var diego : Person;
```

There are two types of functions in sparky.
Void Functions:
```
function hello(){
  print("hello world!");
}
```

Return Atomic type function:

```
function factorial( n : Int) -> Int{
  if n == 1{
		return 1;
	}
	return n * factorial(n-1);
}
```



Desarrollar un lenguaje orientado a objetos con elementos básicos que se esperan para poder desarrollar código orientado a objetos como son los siguientes, que seran lo minimo que tenga el lenguaje:

- [ ] Arreglos
- [ ] Matrices
- [ ] Clases
- [ ] Herencia simple
- [ ] Funciones
- [ ] SpFunc Arreglos
