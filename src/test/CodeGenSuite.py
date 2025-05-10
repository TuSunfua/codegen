import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    def test_401(self):
        input = """func main() {
  var a int = 5;
  var b int = 10;
  var sum int = a + b;
  putIntLn(sum);
}"""
        expect = "15\n"
        self.assertTrue(TestCodeGen.test(input, expect, 401))
        
    def test_402(self):
        input = """func main() {
  var flag bool = true;
  if (flag) {
    putStringLn("True branch");
  } else {
    putStringLn("False branch");
  }
}"""
        expect = "True branch\n"
        self.assertTrue(TestCodeGen.test(input, expect, 402))
        
    def test_403(self):
        input = """func main() {
  var i int = 0;
  for (i < 5) {
    putInt(i);
    putString(" ");
    i += 1;
  }
  putLn();
}"""
        expect = "0 1 2 3 4 \n"
        self.assertTrue(TestCodeGen.test(input, expect, 403))
        
    def test_404(self):
        input = """func multiply(a int, b int) int {
  return a * b;
}

func main() {
  var result int = multiply(4, 5);
  putIntLn(result);
}"""
        expect = "20\n"
        self.assertTrue(TestCodeGen.test(input, expect, 404))
        
    def test_405(self):
        input = """func main() {
  var numbers = [5]int{1, 2, 3, 4, 5}
  var i int = 0;
  var total int = 0;
  for (i < 5) {
    total += numbers[i];
    i += 1;
  }
  putIntLn(total);
}"""
        expect = "15\n"
        self.assertTrue(TestCodeGen.test(input, expect, 405))
        
    def test_406(self):
        input = """type Person struct {
  name string;
  age int;
}

func main() {
  var p Person = Person{name: "Alice", age: 30};
  putStringLn(p.name);
  putIntLn(p.age);
}"""
        expect = "Alice\n30\n"
        self.assertTrue(TestCodeGen.test(input, expect, 406))
        
    def test_407(self):
        input = """func main() {
  var x float = 7.0;
  var y float = 3.0;
  var result float = x / y;
  putFloatLn(result);
}"""
        expect = "2.3333333\n"
        self.assertTrue(TestCodeGen.test(input, expect, 407))
        
    def test_408(self):
        input = """func isEven(n int) boolean {
  return n % 2 == 0;
}

func main() {
  var number int = 11;
  if (isEven(number)) {
    putStringLn("Even");
  } else {
    putStringLn("Odd");
  }
}"""
        expect = "Odd\n"
        self.assertTrue(TestCodeGen.test(input, expect, 408))
    
    def test_409(self):
        input = """func factorial(n int) int {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

func main() {
  var num int = 5;
  var fact int = factorial(num);
  putIntLn(fact);
}"""
        expect = "120\n"
        self.assertTrue(TestCodeGen.test(input, expect, 409))
        
    def test_410(self):
        input = """type Rectangle struct {
  width float;
  height float;
}

func area(r Rectangle) float {
  return r.width * r.height;
}

func main() {
  var rect Rectangle = Rectangle{width: 3.0, height: 4.5};
  var a float = area(rect);
  putFloatLn(a);
}"""
        expect = "13.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 410))


    def test_411(self):
        input = """type Rectangle struct {
  width float;
  height float;
}

func (r Rectangle) area() float {
  return r.width * r.height;
}

func main() {
  var rect Rectangle = Rectangle{width: 3.0, height: 4.5};
  var a float = rect.area()
  putFloatLn(a);
}"""
        expect = "13.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 411))
        
    def test_412(self):
        input = """func fib(n int) int {
  if (n <= 1) {
    return n;
  }
  return fib(n - 1) + fib(n - 2);
}

func main() {
  var i int = 0;
  for (i < 10) {
    putInt(fib(i)); putString(" ");
    i += 1;
  }
  putLn();
}"""
        expect = "0 1 1 2 3 5 8 13 21 34 \n"
        self.assertTrue(TestCodeGen.test(input, expect, 412))
        
    def test_413(self):
        input = """type Counter struct {
  value int;
}

func (c Counter) increment(step int) Counter {
  c.value += step;
  return c;
}

func main() {
  var c Counter = Counter{value: 0};
  var i int = 0;
  for (i < 3) {
    c := c.increment(2);
    putIntLn(c.value);
    i += 1;
  }
}"""
        expect = "2\n4\n6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 413))
        
    def test_414(self):
        input = """func maxArray(arr [5]int) int {
  var max int = arr[0];
  var i int = 1;
  for (i < 5) {
    if (arr[i] > max) {
      max := arr[i];
    }
    i += 1;
  }
  return max;
}

func main() {
  var data [5]int = [5]int{4, 9, 1, 6, 2};
  var result int = maxArray(data);
  putIntLn(result);
}"""
        expect = "9\n"
        self.assertTrue(TestCodeGen.test(input, expect, 414))
        
    def test_415(self):
        input = """type Student struct {
  name string;
  scores [3]int;
}

func average(s Student) int {
  var total int = 0;
  var i int = 0;
  for (i < 3) {
    total += s.scores[i];
    i += 1;
  }
  return total / 3;
}

func main() {
  var st Student = Student{name: "Bob", scores: [3]int{80, 90, 100}};
  putStringLn(st.name);
  putIntLn(average(st));
}"""
        expect = "Bob\n90\n"
        self.assertTrue(TestCodeGen.test(input, expect, 415))
        
    def test_416(self):
        input = """func reverse(arr [4]int) [4]int {
  var temp int;
  var i int = 0;
  for (i < 2) {
    temp := arr[i];
    arr[i] := arr[3 - i];
    arr[3 - i] := temp;
    i += 1;
  }
  return arr;
}

func main() {
  var a = [4]int{1, 2, 3, 4};
  a := reverse(a);
  var j int = 0;
  for (j < 4) {
    putInt(a[j]); putString(" ");
    j += 1;
  }
  putLn();
}"""
        expect = "4 3 2 1 \n"
        self.assertTrue(TestCodeGen.test(input, expect, 416))
        
    def test_417(self):
        input = """func isPrime(n int) boolean{
  if (n <= 1) {
    return false;
  }
  var i = 2;
  for (i * i <= n) {
    if (n % i == 0) {
      return false;
    }
    i += 1;
  }
  return true;
}

func main() {
  var i = 2;
  for (i <= 15) {
    if (isPrime(i)) {
      putInt(i); putString(" ");
    }
    i += 1;
  }
  putLn();
}"""
        expect = "2 3 5 7 11 13 \n"
        self.assertTrue(TestCodeGen.test(input, expect, 417))
        
    def test_418(self):
        input = """func countTrue(arr [5]boolean) int {
  var count int = 0;
  var i int = 0;
  for (i < 5) {
    if (arr[i]) {
      count += 1;
    }
    i += 1;
  }
  return count;
}

func main() {
  var flags = [5]boolean{true, false, true, true, false};
  putIntLn(countTrue(flags));
}"""
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 418))
        
    def test_419(self):
        input = """type Box struct {
  width float;
  height float;
  depth float;
}

func volume(b Box) float {
  return b.width * b.height * b.depth;
}

func main() {
  var b Box = Box{depth: 2.0, width: 3.5, height: 4.0};
  var v float = volume(b);
  putFloatLn(v);
}"""
        expect = "28.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 419))
        
    def test_420(self):
        input = """func search(arr [6]int, target int) int {
  var i int = 0;
  for (i < 6) {
    if (arr[i] == target) {
      return i;
    }
    i += 1;
  }
  return -1;
}

func main() {
  var a = [6]int{3, 5, 7, 1, 9, 2};
  var index int = search(a, 9);
  putIntLn(index);
}""" 
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input, expect, 420))
        
    def test_421(self):
        input = """func main() {
  var a int = 6;
  var b int = 2;
  var op string = "*";
  var result int;

  if (op == "+") {
    result := a + b;
  } else if (op == "-") {
    result := a - b;
  } else if (op == "*") {
    result := a * b;
  } else if (op == "/") {
    result := a / b;
  } else {
    result := 0;
  }

  putIntLn(result);
}"""
        expect = "12\n"
        self.assertTrue(TestCodeGen.test(input, expect, 421))
        
    def test_22(self):
        input = """type Point struct {
  x int;
  y int;
}

func (p1 Point) distance(p2 Point) int {
  return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)
}

func main() {
  var a Point = Point{x: 3, y: 4};
  putIntLn(a.distance(Point{y: 8, x: 6}));
}"""
        expect = "25\n"
        self.assertTrue(TestCodeGen.test(input, expect, 422))
        
    def test_423(self):
        input = """type Shape interface {
  area() float;
}

type Rectangle struct {
  w float;
  h float;
}

func (r Rectangle) area() float {
  return r.w * r.h;
}

func main() {
  var r Shape = Rectangle{w: 4.0, h: 5.5};
  putFloatLn(r.area());
}"""
        expect = "22.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 423))
        
    def test_424(self):
        input = """func factorial(n int) int {
  var res int = 1;
  var i int = 2;
  for (i <= n) {
    res *= i;
    i += 1;
  }
  return res;
}

func main() {
  var x int = 10;
  putIntLn(factorial(x));
}"""
        expect = "3628800\n"
        self.assertTrue(TestCodeGen.test(input, expect, 424))
        
    def test_425(self):
        input = """func countEven(arr [6]int) int {
  var cnt int = 0;
  var i int = 0;
  for i := 0; i < 6; i += 1 {
    if (arr[i] % 2 == 0) {
      cnt += 1;
    }
  }
  return cnt;
}

func main() {
  var a [6]int = [6]int{1, 2, 3, 4, 5, 6};
  putIntLn(countEven(a));
}"""
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 425))
        
    def test_426(self):
        input = """type Person struct {
  name string;
  age int;
}

func isAdult(p Person) boolean {
  return p.age >= 18;
}

func main() {
  var p Person = Person{name: "Alice", age: 20};
  putBoolLn(isAdult(p));
}"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 426))
        
    def test_427(self):
        input = """func pow(x int, y int) int {
  var res int = 1;
  var i int = 0;
  for (i < y) {
    res *= x;
    i += 1;
  }
  return res;
}

func main() {
  var a int = 2;
  var b int = 10;
  putIntLn(pow(a, b));
}"""
        expect = "1024\n"
        self.assertTrue(TestCodeGen.test(input, expect, 427))
        
    def test_428(self):
        input = """func minMax(arr [4]int) [2]int {
  var min int = arr[0];
  var max int = arr[0];
  var i int = 1;
  for (i < 4) {
    if (arr[i] < min) {
      min := arr[i];
    }
    if (arr[i] > max) {
      max := arr[i];
    }
    i += 1;
  }
  var res [2]int;
  res[0] := min;
  res[1] := max;
  return res;
}

func main() {
  var nums = [4]int{7, 2, 9, 4};
  var result [2]int = minMax(nums);
  putInt(result[0]); putString(" "); putIntLn(result[1]);
}"""
        expect = "2 9\n"
        self.assertTrue(TestCodeGen.test(input, expect, 428))
        
    def test_429(self):
        input = """type Matrix2x2 struct {
  a int;
  b int;
  c int;
  d int;
}

func det(m Matrix2x2) int {
  return m.a * m.d - m.b * m.c;
}

func main() {
  var m Matrix2x2 = Matrix2x2{a: 1, d: 2, c: 3};
  putIntLn(det(m)); 
}"""
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 429))
        
    def test_430(self):
        input = """func gcd(a int, b int) int {
  for (b != 0) {
    var t int = b;
    b := a % b;
    a := t;
  }
  return a;
}

func main() {
  putIntLn(gcd(48, 18)); 
}"""
        expect = "6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 430))
        
    def test_431(self):
        input = """func isPalindrome(s [5]int) boolean {
  var i int = 0;
  var j int = 4;
  for (i < j) {
    if (s[i] != s[j]) {
      return false;
    }
    i += 1;
    j -= 1;
  }
  return true;
}

func main() {
  var nums = [5]int{999, 111, 0, 111, 999}
  putBoolLn(isPalindrome(nums));
}"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 431))
        
    def test_432(self):
        input = """func printArray(arr [10]float) {
  for var i = 0; i < 10; i := i + 1 {
    putFloat(arr[i]); putString(" ");
  }
  putLn()
}

func main() {
  var arr [4][10]float = [4][10]int{{1,2,3,4,5,6,7,8,9,10}, {10,9,8,7,6,5,4,3,2,1}, {1,2,3,4,5,4,3,2,1,0}, {9,8,7,6,5,6,7,8,9,10}}
  for var i = 0; i < 4; i += 1 {
    printArray(arr[i])
  }
}"""
        expect = """1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 
10.0 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0 
1.0 2.0 3.0 4.0 5.0 4.0 3.0 2.0 1.0 0.0 
9.0 8.0 7.0 6.0 5.0 6.0 7.0 8.0 9.0 10.0 
"""
        self.assertTrue(TestCodeGen.test(input, expect, 432))
        
    def test_433(self):
        input = """func printArray(arr [10]float) {
  for var i = 0; i < 10; i := i + 1 {
    putFloat(arr[i]); putString(" ");
  }
  putLn()
}

func main() {
  var arr [4][10]float = [4][10]int{{1,2,3,4,5,6,7,8,9,10}, {10,9,8,7,6,5,4,3,2,1}, {1,2,3,4,5,4,3,2,1,0}, {9,8,7,6,5,6,7,8,9,10}}
  arr[2] := [10]int{29, 1, 2004, 0xFF, 0xFF, 0xFF, 0xFF, 23, 1, 2004}
  var i = 0
  for (i < 4) {
    printArray(arr[i])
    i := i + 1
  }
}"""
        expect = """1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 
10.0 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0 
29.0 1.0 2004.0 255.0 255.0 255.0 255.0 23.0 1.0 2004.0 
9.0 8.0 7.0 6.0 5.0 6.0 7.0 8.0 9.0 10.0 
"""
        self.assertTrue(TestCodeGen.test(input, expect, 433))
        
    def test_434(self):
        input = """var arr [10]int = [10]int{29, 1, 2004, 0xFF, 0xFF, 0xFF, 0xFF, 23, 1, 2004};
func printArray() {
  for var i = 0; i < 10; i := i + 1 {
    putFloat(arr[i]); putString(" ");
  }
  putLn()
}


func main() {
  printArray();
}"""
        expect = "29.0 1.0 2004.0 255.0 255.0 255.0 255.0 23.0 1.0 2004.0 \n"
        self.assertTrue(TestCodeGen.test(input, expect, 434))
        
    def test_435(self):
        input = """func printArray(arr [4][10]float, n, m int) {
  i := 0
  for (i < n) {
    for var j = 0; j < m; j += 1 {
      putFloat(arr[i][j]); putString(" ");
    }
    putLn()
    i := i + 1
  }
}

var arr [4][10]float = [4][10]int{{1,2,4,5,6,7,8,9,10}, {10,9,8,7,6,5,4,3,2,1}, {1,2,3,4,5,4,3,2,1}, {9,8,7,6,5,6,7,8,9}}
func main() {
  printArray(arr, 4, 10)
}"""
        expect = """1.0 2.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 0.0 
10.0 9.0 8.0 7.0 6.0 5.0 4.0 3.0 2.0 1.0 
1.0 2.0 3.0 4.0 5.0 4.0 3.0 2.0 1.0 0.0 
9.0 8.0 7.0 6.0 5.0 6.0 7.0 8.0 9.0 0.0 
"""
        self.assertTrue(TestCodeGen.test(input, expect, 435))
        
    def test_436(self):
        input = """func main() {
  var a = [3]int{1, 2, 3};
  putIntLn(a[0]);
  putIntLn(a[1]);
  putIntLn(a[2]);
}"""
        expect = "1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 436))
        
    def test_437(self):
        input = """func sum(arr [5]int) int {
  var total int = 0;
  var i int = 0;
  for (i < 5) {
    total += arr[i];
    i += 1;
  }
  return total;
}

func main() {
  var a [5]int = [5]int{10, 20, 30, 40, 50};
  putIntLn(sum(a));
}""" 
        expect = "150\n"
        self.assertTrue(TestCodeGen.test(input, expect, 437))
        
    def test_438(self):
        input = """func main() {
  var b [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}};
  putIntLn(b[0][1]);  // Output: 2
  putIntLn(b[1][2]);  // Output: 6
}"""
        expect = "2\n6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 438))
        
    def test_439(self):
        input = """func initArray(n int) [4]int {
  var arr = [4]int{0, 0, 0, 0};
  var i int = 0;
  for (i < 4) {
    arr[i] := n * (i + 1);
    i += 1;
  }
  return arr;
}

func main() {
  var result [4]int = initArray(3);
  putIntLn(result[0]);
  putIntLn(result[3]);
}"""
        expect = "3\n12\n"
        self.assertTrue(TestCodeGen.test(input, expect, 439))
        
    def test_440(self):
        input = """func printDiagonal(m [3][3]int) {
  for var i = 0; i < 3; i += 1 {
    putIntLn(m[i][i]);
  }
}

func main() {
  var mat = [3][3]int{{1,2,3},{4,5,6},{7,8,9}};
  printDiagonal(mat);
}"""
        expect = "1\n5\n9\n"
        self.assertTrue(TestCodeGen.test(input, expect, 440))
        
    def test_441(self):
        input = """func main() {
  var arr [5]int;
  arr[0] := 5;
  arr[1] := arr[0] + 10;
  arr[2] := arr[1] * 2;
  putIntLn(arr[2]); // Output: 30
}"""
        expect = "30\n"
        self.assertTrue(TestCodeGen.test(input, expect, 441))
        
    def test_442(self):
        input = """type Cell struct {
  value int;
}

func printFirst(cells [3]Cell) {
  putInt(cells[0].value);
}

func main() {
  var cells = [3]Cell{Cell{value: 10}, Cell{value: 20}, Cell{}};
  printFirst(cells);
}"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 442))
        
    def test_443(self):
        input = """func transpose(mat [2][3]int) [3][2]int {
  var result [3][2]int;
  for i := 0; i < 2; i += 1 {
    for j := 0; j < 3; j += 1 {
      result[j][i] := mat[i][j];
    }
  }
  return result;
}

func main() {
  var m [2][3]int = [2][3]int{{1,2,3},{4,5,6}};
  var t [3][2]int = transpose(m);
  putIntLn(t[1][0]); // Output: 2
  putIntLn(t[2][1]); // Output: 6
}"""
        expect = "2\n6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 443))
        
    def test_444(self):
        input = """func reverse(arr [4]int) [4]int {
  var rev [4]int;
  for var i = 0; i < 4; i += 1 {
    rev[i] := arr[3 - i];
  }
  return rev;
}

func main() {
  var data [4]int = [4]int{7, 8, 9, 10};
  var res [4]int = reverse(data);
  putIntLn(res[0]); // 10
  putIntLn(res[3]); // 7
}"""
        expect = "10\n7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 444))
        
    def test_445(self):
        input = """func main() {
  var count [10]int;
  var i int = 0;
  for (i < 10) {
    count[i] := i * i;
    i += 1;
  }
  putIntLn(count[4]); // Output: 16
  putIntLn(count[9]); // Output: 81
}"""
        expect = "16\n81\n"
        self.assertTrue(TestCodeGen.test(input, expect, 445))
        
    def test_446(self):
        input = """type Person struct {
  name string;
  age int;
}

func main() {
  var p Person = Person{name: "Alice"};
  putStringLn(p.name);
  putIntLn(p.age);
}"""
        expect = "Alice\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 446))
        
    def test_447(self):
        input = """type Point struct {
  x int;
  y int;
}

func (p Point) move(dx int, dy int) Point {
  p.x := p.x + dx;
  p.y := p.y + dy;
  return p
}

func main() {
  var pt Point = Point{y:5, x:10};
  var moved Point = pt.move(2, 3);
  putIntLn(moved.x);
  putIntLn(moved.y);
}"""
        expect = "12\n8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 447))
        
    def test_448(self):
        input = """type Student struct {
  id int;
  scores [3]int;
}

func main() {
  var s = Student{id: 1, scores: [3]int{80, 90, 85}};
  putIntLn(s.scores[0]);
  putIntLn(s.scores[2]);
}"""
        expect = "80\n85\n"
        self.assertTrue(TestCodeGen.test(input, expect, 448))
        
    def test_449(self):
        input = """type Rect struct {
  width int;
  height int;
}

func area(r Rect) int {
  return r.width * r.height;
}

func (r Rect) area() int {
  return r.width * r.height;
}

func main() {
  var box Rect = Rect{width: 4, height: 5};
  putInt(box.area() + area(Rect{height: 4, width: 11}));
}"""
        expect = "64"
        self.assertTrue(TestCodeGen.test(input, expect, 449))
        
    def test_450(self):
        input = """type Book struct {
  title string;
  pages int;
}

func printBook(b Book) {
  putString(b.title + " ");
  putIntLn(b.pages);
}

func main() {
  var books [2]Book = [2]Book{Book{title: "MiniGo", pages: 120}, Book{title: "Compiler Design", pages: 300}};
  printBook(books[0]);
  printBook(books[1]);
}"""
        expect = "MiniGo 120\nCompiler Design 300\n"
        self.assertTrue(TestCodeGen.test(input, expect, 450))
        
    def test_451(self):
        input = """type Inventory struct {
  name string;
  quantities [4]int;
}

func total(inv Inventory) int {
  var sum int = 0;
  var i int = 0;
  for (i < 4) {
    sum += inv.quantities[i];
    i += 1;
  }
  return sum;
}

func main() {
  var inv Inventory = Inventory{name: "Apples", quantities: [4]int{10, 15, 20, 25}};
  putIntLn(total(inv));
}"""
        expect = "70\n"
        self.assertTrue(TestCodeGen.test(input, expect, 451))
        
    def test_452(self):
        input = """func main() {
  var o Outer = Outer{id: 100, m_inner: Inner{value: 999}};
  putIntLn(o.m_inner.value);
}

type Inner struct {
  value int;
}

type Outer struct {
  id int;
  m_inner Inner;
}"""
        expect = "999\n"
        self.assertTrue(TestCodeGen.test(input, expect, 452))
        
    def test_453(self):
        input = """type Matrix struct {
  cells [2][2]int;
}

func getCorner(m Matrix) int {
  return m.cells[1][1];
}

func main() {
  var m Matrix = Matrix{cells: [2][2]int{{1, 2}, {3, 4}}};
  putIntLn(getCorner(m));
}"""
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input, expect, 453))
        
    def test_454(self):
        input = """type LogEntry struct {
  level string;
  times [3]int;
}

func (e LogEntry) printTimes() {
  var i int = 0;
  for (i < 3) {
    putInt(e.times[i]); putString(" ");
    i += 1;
  }
  putLn();
}

func main() {
  var entry = LogEntry{level: "INFO", times: [3]int{2, 4, 6}};
  entry.printTimes();
}"""
        expect = "2 4 6 \n"
        self.assertTrue(TestCodeGen.test(input, expect, 454))
        
    def test_455(self):
        input = """type Grid struct {
  name string;
  cells [2][2]int;
}

func main() {
  var g Grid = Grid{cells: [2][2]int{{5, 6}, {7, 8}}, name: "MyGrid"};
  putStringLn(g.name);
  putIntLn(g.cells[0][1]); // 6
  putIntLn(g.cells[1][0]); // 7
}"""
        expect = "MyGrid\n6\n7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 455))
        
    def test_456(self):
        input = """type Shape interface {
  area() int;
}

type Square struct {
  side int;
}

func (s Square) area() int {
  return s.side * s.side;
}

func main() {
  var sq Shape = Square{side: 4};
  putIntLn(sq.area());
}"""
        expect = "16\n"
        self.assertTrue(TestCodeGen.test(input, expect, 456))
        
    def test_457(self):
        input = """func (p Person) greet() {
  putStringLn("Hello, " + p.name);
}

func greetSomeone(g Greeter) {
  g.greet();
}

func main() {
  var p Person = Person{name: "Alice"};
  var g Greeter = p;
  greetSomeone(g);
}

type Person struct {
  name string;
}

type Greeter interface {
  greet();
}
"""
        expect = "Hello, Alice\n"
        self.assertTrue(TestCodeGen.test(input, expect, 457))
        
    def test_458(self):
        input = """type Animal interface {
  sound() string;
}

type Dog struct {
  color string;
}

func (d Dog) sound() string {
  return "Woof";
}

type Cat struct {
  teeth int;
}

func (c Cat) sound() string {
  return "Meow";
}

func makeSound(a Animal) {
  putStringLn(a.sound());
}

func main() {
  var d = Dog{color: "black"};
  var c = Cat{teeth: 12}
  var animal Animal;
  animal := d;
  makeSound(animal);
  animal := c;
  makeSound(animal);
}"""
        expect = "Woof\nMeow\n"
        self.assertTrue(TestCodeGen.test(input, expect, 458))
        
    def test_459(self):
        input = """func toString(val int) string {
  var res = "";
  var lookup = [10]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
  for (val != 0) {
    rem := val % 10;
    val := val / 10;
    res := lookup[rem] + res;
  }
  return res
}

type Describer interface {
  describe() string;
}

type City struct {
  name string;
  population int;
}

func (c City) describe() string {
  return c.name + " has population " + toString(c.population)
}

func main() {
  var d Describer = City{name: "Metropolis", population: 1000000};
  putString(d.describe());
}"""
        expect = "Metropolis has population 1000000"
        self.assertTrue(TestCodeGen.test(input, expect, 459))
        
    def test_460(self):
        input = """type Printer interface {
  print();
}

type Number struct {
  val int;
}

func (n Number) print() {
  putIntLn(n.val);
}

func printAll(ps [2]Printer) {
  var i int = 0;
  for (i < 2) {
    ps[i].print();
    i += 1;
  }
}

func main() {
  var ps [2]Number = [2]Number{Number{val: 10}, Number{val: 20}};
  var ls [2]Printer;
  ls[0] := ps[0];
  ls[1] := ps[1];
  printAll(ls);
}"""
        expect = "10\n20\n"
        self.assertTrue(TestCodeGen.test(input, expect, 460))
        
    def test_461(self):
        input = """type Printer interface {
  print();
}

type Number struct {
  val int;
}

func (n Number) print() {
  putIntLn(n.val);
}

type String struct {
  val string;
}

func (s String) print() {
  putStringLn(s.val)
}

func printAll(ps [2]Printer) {
  var i int = 0;
  for (i < 2) {
    ps[i].print();
    i += 1;
  }
}

func main() {
  var ps [2]Number = [2]Number{Number{val: 10}, Number{val: 20}};
  var ls [2]Printer;
  ls[0] := ps[0];
  ls[1] := ps[1];
  printAll(ls);
  var us [2]String = [2]String{String{val: "PPL"}, String{val: "HK241"}}
  ls[0] := us[0];
  ls[0] := us[1]
  printAll(ls);
}"""
        expect = "10\n20\nHK241\n20\n"
        self.assertTrue(TestCodeGen.test(input, expect, 461))
        
    def test_462(self):
        input = """type Talker interface {
  talk() string;
}

type Robot struct {
  id int;
}

func (r Robot) talk() string {
  return "Beep from " + "Robot " + toString(r.id);
}

func talk(bot Talker) {
  putStringLn(bot.talk());
}

func main() {
  var bots = [2]Robot{Robot{id: 1}, Robot{id: 2}};
  talk(bots[0]);
  talk(bots[1]);
}

func toString(val int) string {
  var res = "";
  var lookup = [10]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
  for (val != 0) {
    rem := val % 10;
    val := val / 10;
    res := lookup[rem] + res;
  }
  return res
}"""
        expect = "Beep from Robot 1\nBeep from Robot 2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 462))
        
    def test_463(self):
        input = """type Calculator interface {
  compute() int;
}

type Multiplier struct {
  a int;
  b int;
}

func (m Multiplier) compute() int {
  return m.a * m.b;
}

type Adder struct {
  a int;
  b int;
}

func (m Adder) compute() int {
  return m.a + m.b;
}


func main() {
  var m Multiplier = Multiplier{a: 3, b: 5};
  var c Calculator = m;
  putIntLn(c.compute());
  c := Adder{b: m.a, a: m.b};
  putIntLn(c.compute());
}"""
        expect = "15\n8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 463))
        
    def test_464(self):
        input = """type Info interface {
  get() string;
}

type Book struct {
  title string;
}

func (b Book) get() string {
  return "Book: " + b.title;
}

type Pen struct {
  color string;
}

func (p Pen) get() string {
  return "Pen: " + p.color;
}

func displayAll(items [2]Info) {
  var i int = 0;
  for (i < 2) {
    putStringLn(items[i].get());
    i += 1;
  }
}

func main() {
  var items [2]Info;
  items[0] := Book{title: "MiniGo"};
  items[1] := Pen{color: "Blue"};
  displayAll(items);
}"""
        expect = "Book: MiniGo\nPen: Blue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 464))
        
    def test_465(self):
        input = """type Result interface {
  getScore() int;
}

type Exam struct {
  score int;
}

func (e Exam) getScore() int {
  return e.score;
}

type Game struct {
  points int;
}

func (g Game) getScore() int {
  return g.points;
}

func sumScores(results [2]Result) int {
  return results[0].getScore() + results[1].getScore();
}

func main() {
  var r [2]Result;
  r[0] := Exam{score: 85};
  r[1] := Game{points: 15};
  putInt(sumScores(r));
}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 465))
        
    def test_466(self):
        input = """type Engine interface {
  start();
}

type Car struct {
  name string;
}

func (c Car) start() {
  putStringLn("Car " + c.name + " starts");
}

type Plane struct {
  name string;
}

func (p Plane) start() {
  putStringLn("Plane " + p.name + " starts");
}

func startAll(e [2]Engine) {
  var i int = 0;
  for (i < 2) {
    e[i].start();
    i += 1;
  }
}

func main() {
  var engines [2]Engine;
  var vehicle Engine = Car{name: "Tesla"}
  engines[0] := vehicle;
  vehicle := Plane{name: "Boeing"}
  engines[1] := vehicle;
  startAll(engines);
}"""
        expect = "Car Tesla starts\nPlane Boeing starts\n"
        self.assertTrue(TestCodeGen.test(input, expect, 466))
        
    def test_467(self):
        input = """type Engine interface {
  start();
}

type Car struct {
  name string;
}

func (c Car) start() {
  putStringLn("Car " + c.name + " starts");
}

func invoker(e Engine) {
  e.start();
}

func main() {
  var vehicle Engine = Car{name: "Tesla"}
  invoker(vehicle)
}"""
        expect = "Car Tesla starts\n"
        self.assertTrue(TestCodeGen.test(input, expect, 467))
        
    def test_468(self):
        input = """type Shape interface {
  area() float;
}

type Circle struct {
  radius int;
}

func (c Circle) area() float {
  return 3.1415926 * c.radius * c.radius;
}

type Rectangle struct {
  width int;
  height int;
}

func (r Rectangle) area() float {
  return r.width * r.height;
}

func main() {
  var shapes [2]Shape;
  shapes[0] := Circle{radius: 5};
  shapes[1] := Rectangle{width: 4, height: 6};
  putFloatLn(shapes[0].area());
  putFloatLn(shapes[1].area());
}"""
        expect = "78.53981\n24.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 468))
        
    def test_469(self):
        input = """type Person struct {
  name string;
  age int;
  address Address;
}

type Address struct {
  city string;
  zip int;
}

func (p Person) getInfo() string {
  return p.name + " " + toString(p.age) + " " + p.address.city + " " + toString(p.address.zip);
}

func toString(val int) string {
  var res = "";
  var lookup = [10]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
  for (val != 0) {
      rem := val % 10;
      val := val / 10;
      res := lookup[rem] + res;
  }
  return res
} 

func main() {
  var p Person = Person{name: "Alice", age: 30, address: Address{city: "New York", zip: 10001}};
  putStringLn(p.getInfo());
}"""
        expect = "Alice 30 New York 10001\n"
        self.assertTrue(TestCodeGen.test(input, expect, 469))
        
    def test_470(self):
        input = """func aLotsParameters(a, b, c, d, e, f, g, h, i, j, k float, arr [3][1]string) {
  putStringLn(arr[0][0] + " " + arr[1][0] + " " + arr[2][0]);
  putFloatLn(a + b + c + d + e + f + g + h + i + j + k);
}

func main() {
  aLotsParameters(9.1, 0x11, 0b0101, 1.2, 99, 3, 5, 6, 1, 13 / 2.5, 0o765, [3][1]string{{"Hello"}, {"from"}, {"aLotsParameters"}});
}"""
        expect = "Hello from aLotsParameters\n652.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 470))
        
    def test_471(self):
        input = """const x = 42;
var y = x;

func main() {
  y := x + 8;
  putIntLn(y);
}"""
        expect = "50\n"
        self.assertTrue(TestCodeGen.test(input, expect, 471))
        
    def test_472(self):
        input = """const pi = 3.14;

func main() {
  var r float = 5.0;
  var area float = pi * r * r;
  putFloatLn(area);
}"""
        expect = "78.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 472))
        
    def test_473(self):
        input = """var a boolean = true;
const b = false;

func main() {
  putBool(a && !b);
}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 473))
        
    def test_474(self):
        input = """const hello = "Hello";

func main() {
  var name string = "MiniGo";
  var msg string = hello + ", " + name;
  putString(msg);
}"""
        expect = "Hello, MiniGo"
        self.assertTrue(TestCodeGen.test(input, expect, 474))
    
    def test_475(self):
        input = """var arr [3]float = [3]int{1, 2, 3};

func main() {
  putFloat(arr[1]);
}"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 475))
        
    def test_476(self):
        input = """type Point struct {
  x int;
  y int;
}

var origin Point = Point{y: 2, x: 0};

func main() {
  var p Point = Point{x: 3, y: 4};
  putIntLn(p.x + origin.y);
}"""
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 476))
        
    def test_477(self):
        input = """type Describer interface {
  describe() string;
}

type Product struct {
  name string;
}

func (p Product) describe() string {
  return "Product: " + p.name;
}

var d Describer = Product{name: "MiniWidget"};

func main() {
  putStringLn(d.describe());
}"""
        expect = "Product: MiniWidget\n"
        self.assertTrue(TestCodeGen.test(input, expect, 477))
        
    def test_478(self):
        input = """var nums [2]float = [2]float{1.5, 2.5};
const threshold = 3.0;

func main() {
  var total float = nums[0] + nums[1];
  putBoolLn(total > threshold);
}"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 478))
        
    def test_479(self):
        input = """const isDebug = true;
var message string;

func main() {
  if (isDebug) {
    message := "Debug mode on";
  } else {
    message := "Release mode";
  }
  putStringLn(message);
}"""
        expect = "Debug mode on\n"
        self.assertTrue(TestCodeGen.test(input, expect, 479))
        
    def test_480(self):
        input = """
        type Box struct {
  w int;
  h int;
}

type Shape interface {
  area() int;
}

func (b Box) area() int {
  return b.w * b.h;
}

var shapes [2]Shape;

func main() {
  var b1 Box = Box{h:2, w:3};
  var b2 Box = Box{w:4, h:5};
  shapes[0] := b1; shapes[1] := b2;
  putIntLn(shapes[0].area());
  putIntLn(shapes[1].area());
}"""
        expect = "6\n20\n"
        self.assertTrue(TestCodeGen.test(input, expect, 480))
        
    def test_481(self):
        input = """
        const msg = "Result: ";

func square(n int) int {
  return n * n;
}

func main() {
  var a int = 4;
  var b int = square(a);
  putString(msg);
  putIntLn(b);
}"""
        expect = "Result: 16\n"
        self.assertTrue(TestCodeGen.test(input, expect, 481))
        
    def test_482(self):
        input = """var primes [5]int = [5]int{2, 3, 5, 7, 11};

func sum(arr [5]int) int {
  var total int = 0;
  for var i int = 0; i < 5; i := i + 1 {
    total += arr[i];
  }
  return total;
}

func main() {
  putIntLn(sum(primes));
}"""
        expect = "28\n"
        self.assertTrue(TestCodeGen.test(input, expect, 482))
        
    def test_483(self):
        input = """type User struct {
  name string;
  age int;
}

func isAdult(u User) boolean {
  return !!!!!!!!!!!!!!!!!!(u.age >= 18);
}

func main() {
  var u User = User{name: "Alice", age: 21};
  putBoolLn(isAdult(u));
}"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 483))
        
    def test_484(self):
        input = """type Shape interface {
  area() float;
}

type Circle struct {
  r float;
}

func (c Circle) area() float {
  return 3.14 * c.r * c.r;
}

var c = Circle{}

func main() {
  var s Shape = Circle{r: 2.0 * 1.2 + c.r};
  putFloatLn(s.area());
}"""
        expect = "18.086403\n"
        self.assertTrue(TestCodeGen.test(input, expect, 484))
        
    def test_485(self):
        input = """const limit = 5;

func main() {
  for i := 0; i < limit; i := i + 1 {
    if (i % 2 == 0) {
      continue;
    }
    putIntLn(i);
  }
}"""
        expect = "1\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 485))

    def test_486(self):
        input = """const limit = 5;

func main() {
  i := 0;
  for (i < 10) {
    i += 1;
    if (i % 2 == 0) {
      continue;
    }
    putIntLn(i);
  }
}"""
        expect = "1\n3\n5\n7\n9\n"
        self.assertTrue(TestCodeGen.test(input, expect, 486))
        
    def test_487(self):
        input = """var matrix [2][2]int = [2][2]int{{1, 2}, {3, 4}};

func sum2x2(m [2][2]int) int {
  var sum int = 0;
  for var i int = 0; i < 2; i := i + 1 {
    for var j int = 0; j < 2; j := j + 1 {
      sum += m[i][j];
    }
  }
  return sum;
}

func main() {
  putIntLn(sum2x2(matrix));
}"""
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 487))
        
    def test_488(self):
        input = """var matrix [2][2]int = [2][2]int{{1, 2}, {3, 4}};

func sum2x2(m [2][2]int) int {
  var sum int = 0;
  for var i int = 0; i < 2; i := i + 1 {
    for var j int = 0; j < 2; j := j + 1 {
      sum += m[i][j];
      if (i == j) { break; }
    }
  }
  return sum;
}

func main() {
  putIntLn(sum2x2(matrix));
}"""
        expect = "8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 488))
        
    def test_489(self):
        input = """var matrix [2][2]int = [2][2]int{{1, 2}, {3, 4}};

func sum2x2(m [2][2]int) int {
  var sum int = 0;
  for var i int = 0; i < 2; i := i + 1 {
    for var j int = 0; j < 2; j := j + 1 {
      sum += m[i][j];
      if (i == j) { 
        return sum * sum - sum / (sum + 1); 
      }
    }
  }
  return sum;
}

func main() {
  putIntLn(sum2x2(matrix));
}"""
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 489))
        
    def test_490(self):
        input = """type Point struct {
  x int;
  y int;
}

type Drawable interface {
  draw() string;
}

func (p Point) draw() string {
  return "Point(" + toString(p.x) + ", " + toString(p.y) + ")";
}

func main() {
  var d Drawable = Point{y: 3, x: 4};
  putStringLn(d.draw());
}

func toString(val int) string {
  var res = "";
  var lookup = [10]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
  for (val != 0) {
    rem := val % 10;
    val := val / 10;
    res := lookup[rem] + res;
  }
  return res
}"""
        expect = "Point(4, 3)\n"
        self.assertTrue(TestCodeGen.test(input, expect, 490))
        
    def test_491(self):
        input = """const prefix = "Hello, ";

func greet(name string) string {
  return prefix + name;
}

func main() {
  var result string = greet("MiniGo");
  putStringLn(result);
}"""
        expect = "Hello, MiniGo\n"
        self.assertTrue(TestCodeGen.test(input, expect, 491))
        
    def test_492(self):
        input = """type Product struct {
  id int;
  name string;
}

var inventory = [2]Product{Product{id: 1, name: "Pen"}, Product{id: 2, name: "Book"}};

func main() {
  for var i int = 0; i < 2; i += 1 {
    putStringLn(inventory[i].name);
  }
}"""
        expect = "Pen\nBook\n"
        self.assertTrue(TestCodeGen.test(input, expect, 492))
        
    def test_493(self):
        input = """func avg(nums [4]float, n int) float {
  var sum float = 0.0;
  for var i int = 0; i < n; i := i + 1 {
    sum += nums[i];
  }
  return sum / n;
}

func main() {
  var values [4]float = [4]float{1.1, 2.2, 3.3, 4.4};
  putFloatLn(avg(values, 4));
}"""
        expect = "2.75\n"
        self.assertTrue(TestCodeGen.test(input, expect, 493))
        
    def test_494(self):
        input = """var messages [2]string;

func initMessages() {
  messages[0] := "Init";
  messages[1] := "Done";
}

func main() {
  initMessages();
  putStringLn(messages[0]);
  putStringLn(messages[1]);
}"""
        expect = "Init\nDone\n"
        self.assertTrue(TestCodeGen.test(input, expect, 494))
        
    def test_495(self):
        input = """const yes = true;
const no = false;

func flip(b boolean) boolean {
  return !b;
}

func main() {
  putBoolLn(flip(flip(no) || true) || flip(yes));
}"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 495))
    
    def test_496(self):
        input = """var log [3]string;
var idx = 0;

func addLog(msg string) {
  log[idx] := msg;
  idx += 1;
}

func main() {
  addLog("Start");
  addLog("Run");
  addLog("Stop");
  for var idx int = 0; idx < 3; idx := idx + 1 {
    putStringLn(log[idx]);
  }
}"""
        expect = "Start\nRun\nStop\n"
        self.assertTrue(TestCodeGen.test(input, expect, 496))
        
    def test_497(self):
        input = """type Vec2 struct {
  x float;
  y float;
}

func (v Vec2) length() float {
  return v.x * v.x + v.y * v.y;
}

func main() {
  var v Vec2 = Vec2{y: 3.0, x: 4.0};
  putFloatLn(v.length());
}"""
        expect = "25.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 497))
        
    def test_498(self):
        input = """type Matrix struct {
  data [2][2]int;
}

func (m Matrix) trace() int {
  return m.data[0][0] + m.data[1][1];
}

func (m Matrix) transpose() Matrix {
  var t Matrix = Matrix{};
  for var i int = 0; i < 2; i := i + 1 {
    for var j int = 0; j < 2; j := j + 1 {
      t.data[j][i] := m.data[i][j];
    }
  }
  return t;
}

func main() {
  var m Matrix = Matrix{data: [2][2]int{{1, 2}, {3, 4}}};
  var t Matrix = m.transpose();
  putIntLn(m.trace());    // Output: 1 + 4 = 5
  putIntLn(t.data[0][1]); // Output: 3
  putIntLn(t.data[1][0]); // Output: 2
}"""
        expect = "5\n3\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 498))
        
    def test_499(self):
        input = """type Expr interface {
  eval() int;
}

type Literal struct {
  value int;
}

func (l Literal) eval() int {
  return l.value;
}

type Add struct {
  left Expr;
  right Expr;
}

func (a Add) eval() int {
  return a.left.eval() + a.right.eval();
}

type Mul struct {
  left Expr;
  right Expr;
}

func (m Mul) eval() int {
  return m.left.eval() * m.right.eval();
}

func main() {
  // Represents: (2 + 3) * (4 + 5)
  var expr Expr = Mul{left: Add{left: Literal{value: 2}, right: Literal{value: 3}}, right: Add{left: Literal{value: 4}, right: Literal{value: 5}}};
  putIntLn(expr.eval()); // (2+3)*(4+5) = 5*9 = 45
}"""
        expect = "45\n"
        self.assertTrue(TestCodeGen.test(input, expect, 499))
        
    def test_500(self):
        input = """type Node struct {
  value int;
  left Node;
  right Node;
}

func insert(root Node, val int) Node {
  if (root.value == -1) {
    return Node{value: val, left: Node{value: -1}, right: Node{value: -1}};
  }

  if (val < root.value) {
    root.left := insert(root.left, val);
  } else {
    root.right := insert(root.right, val);
  }

  return root;
}

func inorder(root Node) {
  if (root.value != -1) {
    inorder(root.left);
    putInt(root.value); putString(" ");
    inorder(root.right);
  }
}

func main() {
  var root Node = Node{value: -1};
  var values [7]int = [7]int{9, 0, 4, 1, 8, 3, 8};

  for var i int = 0; i < 7; i := i + 1 {
    root := insert(root, values[i]);
  }

  inorder(root); putLn();
}"""
        expect = "0 1 3 4 8 8 9 \n"
        self.assertTrue(TestCodeGen.test(input, expect, 500))