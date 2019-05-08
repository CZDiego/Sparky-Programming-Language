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

Return Atomic type function, in this example we show how to use recursion

```
function factorial( n : Int) -> Int{
  if n == 1{
		return 1;
	}
	return n * factorial(n-1);
}
```

A class is declared like this:
```
class product{
	var quantity : Int;
	var price : Float;
	var available : Bool;
	
	init();
	
	function getPrice() -> Float{
		return price;
	}
}
  
```
The init(); is mandatory, and it gives the object space in memory, also you can use variables and functions inside the class!
An object can call its own methods by:
```
main(){
	var x : Person;
	
	x.getPrice();
}
```

We can also send objects as parameters in a function

```
function foo(p : Person){
	print(p.age);
}

main(){
	var x : Person;
	
	x.age = 23;
	
	foo(x);
}
```

If we send arrays as parameters, they are sent as reference, that means that if you modify them inside a function, their value will be changed inside the main program as well. All the other values are sent by value, so we make a copy and if we modify it inside a function it wont be changed on the main program.

A class can inherit from another one by:

```
class A {
	var a : Int
	init();
}

class B : A{
	var b : Float;
	init();
}

main(){
	var c : B;
	
	c.a = 10;
	c.b = 29.1;
}
```

#Have Fun!
Sparky contains:

```
variables
constants
arrays
matrices
objects
infinite simple inheritance
functions
parameters
```
