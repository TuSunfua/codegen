import unittest
from TestUtils import TestCodeGen
from AST import *
from itertools import count

num = count(501)

class CheckCodeGenSuite(unittest.TestCase):
    def test_501(self):
        input = """func totalOdd(numbers [6]int) int {
  var count int = 0;
  var index int = 0;
  for index := 0; index < 6; index += 1 {
    if (numbers[index] % 2 != 0) {
      count += 1;
    }
  }
  return count;
}

func main() {
  var values [6]int = [6]int{10, 15, 20, 25, 30, 35};
  putIntLn(totalOdd(values));
}"""
        expect = """3
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_502(self):
        input = """type Speaker interface {
  speak() string;
}

type Android struct {
  serial int;
}

func (a Android) speak() string {
  return "Hello from " + "Android " + toStr(a.serial);
}

func communicate(unit Speaker) {
  putStringLn(unit.speak());
}

func main() {
  var devices = [2]Android{Android{serial: 101}, Android{serial: 202}};
  communicate(devices[0]);
  communicate(devices[1]);
}

func toStr(num int) string {
  var output = "";
  var digits = [10]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
  for (num != 0) {
    remainder := num % 10;
    num := num / 10;
    output := digits[remainder] + output;
  }
  return output;
}"""
        expect = """Hello from Android 101
Hello from Android 202
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_503(self):
        input = """type Calculation interface {
  compute() int;
}

type Constant struct {
  val int;
}

func (c Constant) compute() int {
  return c.val;
}

type Sum struct {
  first Calculation;
  second Calculation;
}

func (s Sum) compute() int {
  return s.first.compute() + s.second.compute();
}

type Product struct {
  first Calculation;
  second Calculation;
}

func (p Product) compute() int {
  return p.first.compute() * p.second.compute();
}

func main() {
  // Represents: (5 + 7) * (3 + 4)
  var expression Calculation = Product{first: Sum{first: Constant{val: 5}, second: Constant{val: 7}}, second: Sum{first: Constant{val: 3}, second: Constant{val: 4}}};
  putIntLn(expression.compute()); // (5+7)*(3+4) = 12*7 = 84
}"""
        expect = """84
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_504(self):
        input = """func isPerfectSquare(num int) boolean {
  if (num < 0) {
    return false;
  }
  var j = 0;
  for (j * j <= num) {
    if (j * j == num) {
      return true;
    }
    j += 1;
  }
  return false;
}

func main() {
  var j = 1;
  for (j <= 20) {
    if (isPerfectSquare(j)) {
      putInt(j); putString(" ");
    }
    j += 1;
  }
  putLn();
}"""
        expect = """1 4 9 16 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_505(self):
        input = """const greeting = "Hi";

func main() {
  var user string = "GoLang";
  var output string = greeting + ", " + user;
  putString(output);
}"""
        expect = """Hi, GoLang"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_506(self):
        input = """func displayGrid(grid [3][5]int, rows, cols int) {
  for var row = 0; row < rows; row += 1 {
    var colIndex = 0
    for (colIndex < cols) {
      putInt(grid[row][colIndex]); 
      putString(" ");
      colIndex := colIndex + 1
    }
    putLn()
  }
}

var gridData [3][5]int = [3][5]int{{1,3,5,7,9}, {2,4,6,8,10}, {10,9,8,7,6}}
func main() {
  displayGrid(gridData, 3, 5)
}"""
        expect = """1 3 5 7 9 
2 4 6 8 10 
10 9 8 7 6 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_507(self):
        input = """var records [5]string;
var counter = 0;

func logEntry(entry string) {
  records[counter] := entry;
  counter += 1;
}

func main() {
  logEntry("Begin");
  logEntry("Process");
  logEntry("Complete");
  for var i int = 0; i < 3; i += 1 {
    putStringLn(records[i]);
  }
}"""
        expect =  """Begin
Process
Complete
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_508(self):
        input = """const on = true;
const off = false;

func toggle(value boolean) boolean {
  return !value;
}

func main() {
  putBoolLn(toggle(toggle(off) && false) && toggle(on));
}"""
        expect = """false
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_509(self):
        input = """const debugMode = false;
var outputMessage string;

func main() {
  if (debugMode) {
    outputMessage := "Debugging is active";
  } else {
    outputMessage := "Production environment";
  }
  putStringLn(outputMessage);
}"""
        expect = """Production environment
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_510(self):
        input = """type Item struct {
  id int;
  title string;
}

var catalog = [2]Item{Item{id: 3, title: "Notebook"}, Item{id: 4, title: "Folder"}};

func main() {
  for var j int = 0; j < 2; j += 1 {
    putStringLn(catalog[j].title);
  }
}"""
        expect = """Notebook
Folder
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_511(self):
        input = """func findIndex(elements [6]int, value int) int {
  var index int = 0;
  for (index < 6) {
    if (elements[index] == value) {
      return index;
    }
    index += 1;
  }
  return -1;
}

func main() {
  var numbers = [6]int{2, 4, 8, 6, 10, 1};
  var foundIndex int = findIndex(numbers, 10);
  putIntLn(foundIndex);
}"""
        expect = """4
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_512(self):
        input = """func checkAnagram(word1 [5]string, word2 [5]string) boolean {
  var count1 [26]int;
  var count2 [26]int;
  for var k int = 0; k < 5; k += 1 {
    return true;
  }
  for var l int = 0; l < 26; l += 1 {
    if (count1[l] != count2[l]) {
      return false;
    }
  }
  return true;
}

func main() {
  var wordSet1 = [5]string{"listen", "silent", "enlist", "tinsel", "inlets"};
  var wordSet2 = [5]string{"inlets", "listen", "silent", "tinsel", "enlist"};
  putBoolLn(checkAnagram(wordSet1, wordSet2));
}"""
        expect = """true
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_513(self):
        input = """type Appliance interface {
  operate();
}

type Refrigerator struct {
  brand string;
}

func (r Refrigerator) operate() {
  putStringLn("Refrigerator " + r.brand + " is running");
}

type WashingMachine struct {
  brand string;
}

func (w WashingMachine) operate() {
  putStringLn("Washing Machine " + w.brand + " is operating");
}

func runAll(appliances [2]Appliance) {
  var m int = 0;
  for (m < 2) {
    appliances[m].operate();
    m += 1;
  }
}

func main() {
  var appliances [2]Appliance;
  var fridge Appliance = Refrigerator{brand: "LG"}
  appliances[0] := fridge;
  fridge := WashingMachine{brand: "Samsung"}
  appliances[1] := fridge;
  runAll(appliances);
}"""
        expect = """Refrigerator LG is running
Washing Machine Samsung is operating
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_514(self):
        input = """type User struct {
  username string;
  points int;
  location Place;
}

type Place struct {
  area string;
  postalCode int;
}

func (u User) displayDetails() string {
  return u.username + " has " + toString(u.points) + " points in " + u.location.area + " with postal code " + toString(u.location.postalCode);
}

func toString(number int) string {
  var result = "";
  var digits = [10]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
  for (number != 0) {
      remainder := number % 10;
      number := number / 10;
      result := digits[remainder] + result;
  }
  return result
} 

func main() {
  var userInfo User = User{username: "Bob", points: 50, location: Place{area: "Los Angeles", postalCode: 90001}};
  putStringLn(userInfo.displayDetails());
}"""
        expect = """Bob has 50 points in Los Angeles with postal code 90001
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_515(self):
        input = """func stringify(num int) string {
  var result = "";
  var digits = [10]string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}
  for (num != 0) {
    rem := num % 10;
    num := num / 10;
    result := digits[rem] + result;
  }
  return result
}

type Notifier interface {
  notify() string;
}

type Town struct {
  title string;
  inhabitants int;
}

func (t Town) notify() string {
  return t.title + " has inhabitants " + stringify(t.inhabitants)
}

func main() {
  var n Notifier = Town{title: "Smallville", inhabitants: 50000};
  putString(n.notify());
}"""
        expect = """Smallville has inhabitants FAAAA"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_516(self):
        input = """var values [4]float = [4]int{2, 4, 6, 8};

func main() {
  putFloat(values[2]);
}"""
        expect = """6.0"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_517(self):
        input = """type Circle struct {
  radius float;
}

func (c Circle) circumference() float {
  return 2 * 3.14 * c.radius;
}

func main() {
  var circle Circle = Circle{radius: 5.0};
  var c float = circle.circumference()
  putFloatLn(c);
}"""
        expect = """31.400002
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_518(self):
        input = """func main() {
  var nums = [6]int{10, 20, 30, 40, 50, 60}
  var index int = 0;
  var sum int = 0;
  for (index < 6) {
    sum += nums[index];
    index += 1;
  }
  putIntLn(sum);
}"""
        expect = """210
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_519(self):
        input = """func lcm(x int, y int) int {
  var product int = x * y;
  for (y != 0) {
    var temp int = y;
    y := x % y;
    x := temp;
  }
  return product / x;
}

func main() {
  putIntLn(lcm(12, 15)); 
}"""
        expect = """60
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_520(self):
        input = """type Displayable interface {
  show();
}

type Integer struct {
  number int;
}

func (i Integer) show() {
  putIntLn(i.number);
}

type Text struct {
  content string;
}

func (t Text) show() {
  putStringLn(t.content);
}

func displayAll(ds [2]Displayable) {
  var j int = 0;
  for (j < 2) {
    ds[j].show();
    j += 1;
  }
}

func main() {
  var integers [2]Integer = [2]Integer{Integer{number: 30}, Integer{number: 40}};
  var displayables [2]Displayable;
  displayables[0] := integers[0];
  displayables[1] := integers[1];
  displayAll(displayables);
  var texts [2]Text = [2]Text{Text{content: "Hello"}, Text{content: "World"}};
  displayables[0] := texts[0];
  displayables[1] := texts[1];
  displayAll(displayables);
}"""
        expect = """30
40
Hello
World
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_521(self):
        input = """type Geometry interface {
  computeArea() float;
}

type Triangle struct {
  base float;
  height float;
}

func (t Triangle) computeArea() float {
  return 0.5 * t.base * t.height;
}

func main() {
  var t Geometry = Triangle{base: 3.0, height: 6.0};
  putFloatLn(t.computeArea());
}"""
        expect = """9.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_522(self):
        input = """type Item interface {
  retrieve() string;
}

type Article struct {
  name string;
}

func (a Article) retrieve() string {
  return "Article: " + a.name;
}

type Marker struct {
  shade string;
}

func (m Marker) retrieve() string {
  return "Marker: " + m.shade;
}

func listAll(elements [2]Item) {
  for var j = 0; j < 2; j += 1 {
    putStringLn(elements[j].retrieve());
  }
}

func main() {
  var elements [2]Item;
  elements[0] := Article{name: "Understanding MiniGo"};
  elements[1] := Marker{shade: "Red"};
  listAll(elements);
}"""
        expect = """Article: Understanding MiniGo
Marker: Red
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_523(self):
        input = """func displayFloatArray(array [10]float) {
  for var j = 0; j < 10; j += 1 {
    putFloat(array[j]); putString(" ");
  }
  putLn();
}

func main() {
  var floatArray [3][10]float = [3][10]float{{1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.0}, {10.0,9.9,8.8,7.7,6.6,5.5,4.4,3.3,2.2,1.1}, {0.0,1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9}};
  for var j = 0; j < 3; j += 1 {
    displayFloatArray(floatArray[j]);
  }
}"""
        expect = """1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9 10.0 
10.0 9.9 8.8 7.7 6.6 5.5 4.4 3.3 2.2 1.1 
0.0 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_524(self):
        input = """type Printer interface {
  print();
}

type Value struct {
  amount int;
}

func (v Value) print() {
  putIntLn(v.amount);
}

func printAll(values [3]Printer) {
  for var j = 0; j < 3; j += 1 {
    values[j].print();
  }
}

func main() {
  var vals [3]Value = [3]Value{Value{amount: 100}, Value{amount: 200}, Value{amount: 300}};
  var printers [3]Printer;
  printers[0] := vals[0];
  printers[1] := vals[1];
  printers[2] := vals[2];
  printAll(printers);
}"""
        expect = """100
200
300
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_525(self):
        input = """var grid [2][2]int = [2][2]int{{5, 6}, {7, 8}};

func total2x2(arr [2][2]int) int {
  var total int = 0;
  for var x int = 0; x < 2; x := x + 1 {
    for var y int = 0; y < 2; y := y + 1 {
      total += arr[x][y];
      if (x == y) { 
        return total * total - total / (total + 2); 
      }
    }
  }
  return total;
}

func main() {
  putIntLn(total2x2(grid));
}"""
        expect = """25
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_526(self):
        input = """type Square struct {
  side float;
}

func calculateArea(s Square) float {
  return s.side * s.side;
}

func main() {
  var sq Square = Square{side: 2.5};
  var area float = calculateArea(sq);
  putFloatLn(area);
}"""
        expect = """6.25
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_527(self):
        input = """type Figure interface {
  calculateArea() float;
}

type Triangle struct {
  base int;
  height int;
}

func (t Triangle) calculateArea() float {
  return 0.5 * (t.base) * (t.height);
}

type Square struct {
  side int;
}

func (s Square) calculateArea() float {
  return s.side * s.side;
}

func main() {
  var figures [2]Figure;
  figures[0] := Triangle{base: 3, height: 6};
  figures[1] := Square{side: 4};
  putFloatLn(figures[0].calculateArea());
  putFloatLn(figures[1].calculateArea());
}"""
        expect = """9.0
16.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_528(self):
        input = """func main() {
  var container OuterContainer = OuterContainer{id: 200, m_inner: InnerContainer{value: 888}};
  putIntLn(container.m_inner.value);
}

type InnerContainer struct {
  value int;
}

type OuterContainer struct {
  id int;
  m_inner InnerContainer;
}"""
        expect = """888
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_529(self):
        input = """type TreeNode struct {
  value int;
  left TreeNode;
  right TreeNode;
}

func addNode(root TreeNode, val int) TreeNode {
  if (root.value == -1) {
    return TreeNode{value: val, left: TreeNode{value: -1}, right: TreeNode{value: -1}};
  }

  if (val < root.value) {
    root.left := addNode(root.left, val);
  } else {
    root.right := addNode(root.right, val);
  }

  return root;
}

func traverseInOrder(root TreeNode) {
  if (root.value != -1) {
    traverseInOrder(root.left);
    putInt(root.value); putString(" ");
    traverseInOrder(root.right);
  }
}

func main() {
  var root TreeNode = TreeNode{value: -1};
  var nums [5]int = [5]int{7, 2, 5, 1, 9};

  for var i int = 0; i < 5; i := i + 1 {
    root := addNode(root, nums[i]);
  }

  traverseInOrder(root); putLn();
}"""
        expect = """1 2 5 7 9 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_530(self):
        input = """type Animal struct {
  species string;
  age int;
}

func main() {
  var pet Animal = Animal{species: "Dog"};
  putStringLn(pet.species);
  putIntLn(pet.age);
}"""
        expect = """Dog
0
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_531(self):
        input = """func power(base int, exp int) int {
  if (exp == 0) {
    return 1;
  }
  return base * power(base, exp - 1);
}

func main() {
  var index int = 0;
  for (index < 5) {
    putInt(power(2, index)); putString(" ");
    index += 1;
  }
  putLn();
}"""
        expect = """1 2 4 8 16 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_532(self):
        input = """type Cart struct {
  itemName string;
  prices [3]int;
}

func calculateTotal(cart Cart) int {
  var total int = 0;
  var j int = 0;
  for (j < 3) {
    total += cart.prices[j];
    j += 1;
  }
  return total;
}

func main() {
  var shopping Cart = Cart{itemName: "Groceries", prices: [3]int{50, 100, 150}};
  putIntLn(calculateTotal(shopping));
}"""
        expect = """300
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_533(self):
        input = """const threshold = 7;

func main() {
  count := 0;
  for (count < 15) {
    count += 1;
    if (count % threshold == 0) {
      continue;
    }
    putIntLn(count);
  }
}"""
        expect = """1
2
3
4
5
6
8
9
10
11
12
13
15
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_534(self):
        input = """func sumDigits(n int) int {
  if (n == 0) {
    return 0;
  }
  return (n % 10) + sumDigits(n / 10);
}

func main() {
  var number int = 12345;
  var digitSum int = sumDigits(number);
  putIntLn(digitSum);
}"""
        expect = """15
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_535(self):
        input = """func swapElements(items [4]int) [4]int {
  var holder int;
  var index int = 0;
  for (index < 2) {
    holder := items[index];
    items[index] := items[3 - index];
    items[3 - index] := holder;
    index += 1;
  }
  return items;
}

func main() {
  var numbers = [4]int{5, 6, 7, 8};
  numbers := swapElements(numbers);
  var k int = 0;
  for (k < 4) {
    putInt(numbers[k]); putString(" ");
    k += 1;
  }
  putLn();
}"""
        expect = """8 7 6 5 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_536(self):
        input = """var grid [2][2]int = [2][2]int{{5, 10}, {15, 20}};

func calculateSum(m [2][2]int) int {
  var total int = 0;
  for var row int = 0; row < 2; row += 1 {
    for var col int = 0; col < 2; col += 1 {
      total += m[row][col];
    }
  }
  return total;
}

func main() {
  putIntLn(calculateSum(grid));
}"""
        expect = """50
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_537(self):
        input = """type Learner struct {
  studentID int;
  grades [3]int;
}

func main() {
  var pupil = Learner{studentID: 2, grades: [3]int{75, 88, 92}};
  putIntLn(pupil.grades[1]);
  putIntLn(pupil.grades[0]);
}"""
        expect = """88
75
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_538(self):
        input = """type Creature interface {
  vocalize() string;
}

type Wolf struct {
  furColor string;
}

func (w Wolf) vocalize() string {
  return "Howl";
}

type Feline struct {
  clawCount int;
}

func (f Feline) vocalize() string {
  return "Purr";
}

func emitSound(c Creature) {
  putStringLn(c.vocalize());
}

func main() {
  var wolfInstance = Wolf{furColor: "grey"};
  var felineInstance = Feline{clawCount: 8}
  var creature Creature;
  creature := wolfInstance;
  emitSound(creature);
  creature := felineInstance;
  emitSound(creature);
}"""
        expect = """Howl
Purr
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_539(self):
        input = """func switchMatrix(mat [2][3]int) [3][2]int {
  var newMatrix [3][2]int;
  for row := 0; row < 2; row += 1 {
    for col := 0; col < 3; col += 1 {
      newMatrix[col][row] := mat[row][col];
    }
  }
  return newMatrix;
}

func main() {
  var original [2][3]int = [2][3]int{{9,10,11},{12,13,14}};
  var transposed [3][2]int = switchMatrix(original);
  putIntLn(transposed[1][0]); // Output: 10
  putIntLn(transposed[2][1]); // Output: 14
}"""
        expect = """10
14
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_540(self):
        input = """const threshold = 50;

func main() {
  var score int = 75;
  var result string;

  if (score > threshold) {
    result := "Passed";
  } else {
    result := "Failed";
  }
  putStringLn(result);
}"""
        expect = """Passed
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_541(self):
        input = """var numbers [5]int = [5]int{3, 7, 10, 1, 5};

func displayNumbers() {
  for var j = 0; j < 5; j := j + 1 {
    putInt(numbers[j]); 
    putString(" ");
  }
  putLn();
}

func main() {
  displayNumbers();
}"""
        expect = """3 7 10 1 5 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_542(self):
        input = """const euler = 2.718;

func main() {
  var base float = 2.0;
  var exponent float = 3.0;
  var result float = euler * base * exponent;
  putFloatLn(result);
}"""
        expect = """16.307999
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_543(self):
        input = """func main() {
  var squares [5]int;
  for var index = 0; index < 5; index += 1 {
    squares[index] := index * index;
  }
  putIntLn(squares[2]); // Output: 4
}"""
        expect = """4
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_544(self):
        input = """type Vehicle interface {
  drive();
}

type Bike struct {
  model string;
}

func (b Bike) drive() {
  putStringLn("Bike " + b.model + " is riding");
}

func execute(v Vehicle) {
  v.drive();
}

func main() {
  var myRide Vehicle = Bike{model: "Yamaha"}
  execute(myRide)
}"""
        expect = """Bike Yamaha is riding
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_545(self):
        input = """type Grid struct {
  values [3][3]int;
}

func fetchCorner(g Grid) int {
  return g.values[0][2];
}

func main() {
  var g Grid = Grid{values: [3][3]int{{5, 6, 7}, {8, 9, 10}, {11, 12, 13}}};
  putIntLn(fetchCorner(g));
}"""
        expect = """7
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_546(self):
        input = """type ScoreKeeper interface {
  calculate() int;
}

type Test struct {
  mark int;
}

func (t Test) calculate() int {
  return t.mark;
}

type Contest struct {
  tally int;
}

func (c Contest) calculate() int {
  return c.tally;
}

func aggregateScores(scoreList [2]ScoreKeeper) int {
  return scoreList[0].calculate() + scoreList[1].calculate();
}

func main() {
  var scores [2]ScoreKeeper;
  scores[0] := Test{mark: 92};
  scores[1] := Contest{tally: 28};
  putInt(aggregateScores(scores));
}"""
        expect = """120"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_547(self):
        input = """func shuffle(arr [5]int) [5]int {
  var shuffled [5]int;
  for var i = 0; i < 5; i += 1 {
    shuffled[i] := arr[4 - i];
  }
  return shuffled;
}

func main() {
  var nums [5]int = [5]int{14, 15, 16, 17, 18};
  var newNums [5]int = shuffle(nums);
  putIntLn(newNums[0]); // 18
  putIntLn(newNums[4]); // 14
}"""
        expect = """18
14
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_548(self):
        input = """func add(x int, y int) int {
  return x + y;
}

func main() {
  var total int = add(3, 7);
  putIntLn(total);
}"""
        expect = """10
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_549(self):
        input = """type Array2D struct {
  matrix [3][3]int;
}

func (a Array2D) diagonalSum() int {
  return a.matrix[0][0] + a.matrix[1][1] + a.matrix[2][2];
}

func (a Array2D) rotate() Array2D {
  var rotated Array2D = Array2D{};
  for var i int = 0; i < 3; i := i + 1 {
    for var j int = 0; j < 3; j := j + 1 {
      rotated.matrix[j][2 - i] := a.matrix[i][j];
    }
  }
  return rotated;
}

func main() {
  var a Array2D = Array2D{matrix: [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}};
  var b Array2D = a.rotate();
  putIntLn(a.diagonalSum());    // Output: 1 + 5 + 9 = 15
  putIntLn(b.matrix[0][1]);     // Output: 4
  putIntLn(b.matrix[2][0]);     // Output: 2
}"""
        expect = """15
4
9
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_550(self):
        input = """func computePower(base int, exp int) int {
  var result int = 1;
  var i int = 0;
  for (i < exp) {
    result *= base;
    i += 1;
  }
  return result;
}

func main() {
  var num int = 5;
  var power int = 3;
  putIntLn(computePower(num, power));
}"""
        expect = """125
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_551(self):
        input = """const greeting = "The square is: ";

func calculateArea(side int) int {
  return side * side;
}

func main() {
  var length int = 6;
  var area int = calculateArea(length);
  putString(greeting);
  putIntLn(area);
}"""
        expect = """The square is: 36
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_552(self):
        input = """func main() {
  var numbers = [4]int{10, 20, 30, 40};
  putIntLn(numbers[1]);
  putIntLn(numbers[2]);
  putIntLn(numbers[3]);
}"""
        expect = """20
30
40
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_553(self):
        input = """func main() {
  var value1 float = 8.0;
  var value2 float = 2.0;
  var quotient float = value1 / value2;
  putFloatLn(quotient);
}"""
        expect = """4.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_554(self):
        input = """func fillArray(m int) [5]int {
  var arr = [5]int{0, 0, 0, 0, 0};
  var j int = 0;
  for (j < 5) {
    arr[j] := m * (j + 2);
    j += 1;
  }
  return arr;
}

func main() {
  var filledArray [5]int = fillArray(4);
  putIntLn(filledArray[0]);
  putIntLn(filledArray[4]);
}"""
        expect = """8
24
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_555(self):
        input = """type Novel struct {
  name string;
  chapters int;
}

func displayNovel(n Novel) {
  putString(n.name + " ");
  putIntLn(n.chapters);
}

func main() {
  var novels [2]Novel = [2]Novel{Novel{name: "The Go Programming Language", chapters: 15}, Novel{name: "Algorithms Unlocked", chapters: 10}};
  displayNovel(novels[0]); 
  displayNovel(novels[1]);
}"""
        expect = """The Go Programming Language 15
Algorithms Unlocked 10
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_556(self):
        input = """type Polygon interface {
  perimeter() int;
}

type Triangle struct {
  sideA int;
  sideB int;
  sideC int;
}

func (t Triangle) perimeter() int {
  return t.sideA + t.sideB + t.sideC;
}

func main() {
  var tri Polygon = Triangle{sideA: 3, sideB: 4, sideC: 5};
  putIntLn(tri.perimeter());
}"""
        expect = """12
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_557(self):
        input = """func (s Student) introduce() {
  putStringLn("Hi, my name is " + s.name);
}

func introducePerson(i Introducer) {
  i.introduce();
}

func main() {
  var s Student = Student{name: "Bob"};
  var i Introducer = s;
  introducePerson(i);
}

type Student struct {
  name string;
}

type Introducer interface {
  introduce();
}"""
        expect = """Hi, my name is Bob
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_558(self):
        input = """func showMatrix(mat [3][5]int) {
  for var row = 0; row < 3; row := row + 1 {
    for var col = 0; col < 5; col += 1 {
      putInt(mat[row][col]); putString(" ");
    }
    putLn();
  }
}

func main() {
  var mat [3][5]int = [3][5]int{{1, 2, 3, 4, 5}, {5, 4, 3, 2, 1}, {0, 1, 2, 3, 4}};
  showMatrix(mat);
}"""
        expect = """1 2 3 4 5 
5 4 3 2 1 
0 1 2 3 4 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_559(self):
        input = """func findMin(nums [4]int) int {
  var minimum int = nums[0];
  var index int = 1;
  for (index < 4) {
    if (nums[index] < minimum) {
      minimum := nums[index];
    }
    index += 1;
  }
  return minimum;
}

func main() {
  var values [4]int = [4]int{7, 2, 9, 3};
  var minValue int = findMin(values);
  putIntLn(minValue);
}"""
        expect = """2
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_560(self):
        input = """func main() {
  var data [5]int;
  data[0] := 8;
  data[1] := data[0] * 3;
  data[2] := data[1] - 4;
  putIntLn(data[2]); // Output: 20
}"""
        expect = """20
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_561(self):
        input = """type Circle struct {
  radius int;
}

func circumference(c Circle) int {
  return 2 * 3 * c.radius;
}

func (c Circle) area() int {
  return 3 * c.radius * c.radius;
}

func main() {
  var myCircle Circle = Circle{radius: 7};
  putInt(myCircle.area() + circumference(Circle{radius: 10}));
}"""
        expect = """207"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_562(self):
        input = """var values [3]float = [3]float{2.0, 3.0, 4.0};
const limit = 12.0;

func main() {
  var sum float = values[0] + values[1] + values[2];
  putBoolLn(sum < limit);
}"""
        expect = """true
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_563(self):
        input = """func calculate(arr [5]int) int {
  var total int = 0;
  var j int = 0;
  for (j < 5) {
    total += arr[j];
    j += 1;
  }
  return total;
}

func main() {
  var numbers [5]int = [5]int{15, 25, 35, 45, 55};
  putIntLn(calculate(numbers));
}"""
        expect = """175
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_564(self):
        input = """func findBounds(arr [4]int) [2]int {
  var low int = arr[0];
  var high int = arr[0];
  var j int = 1;
  for (j < 4) {
    if (arr[j] < low) {
      low := arr[j];
    }
    if (arr[j] > high) {
      high := arr[j];
    }
    j += 1;
  }
  var output [2]int;
  output[0] := low;
  output[1] := high;
  return output;
}

func main() {
  var values = [4]int{5, 3, 10, 1};
  var bounds [2]int = findBounds(values);
  putInt(bounds[0]); putString(" "); putIntLn(bounds[1]);
}"""
        expect = """1 10
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_565(self):
        input = """type LogRecord struct {
  severity string;
  timestamps [3]int;
}

func (r LogRecord) displayTimestamps() {
  var index int = 0;
  for (index < 3) {
    putInt(r.timestamps[index]);
    putString(" ");
    index += 1;
  }
  putLn();
}

func main() {
  var record = LogRecord{severity: "DEBUG", timestamps: [3]int{1, 3, 5}};
  record.displayTimestamps();
}"""
        expect = """1 3 5 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_566(self):
        input = """type Learner struct {
  fullName string;
  grades [3]int;
}

func calculateAverage(l Learner) int {
  var sum int = 0;
  var idx int = 0;
  for (idx < 3) {
    sum += l.grades[idx];
    idx += 1;
  }
  return sum / 3;
}

func main() {
  var learner Learner = Learner{fullName: "Alice", grades: [3]int{70, 85, 90}};
  putStringLn(learner.fullName);
  putIntLn(calculateAverage(learner));
}"""
        expect = """Alice
81
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_567(self):
        input = """type Block struct {
  data int;
}

func showFirst(blocks [3]Block) {
  putInt(blocks[0].data);
}

func main() {
  var blocks = [3]Block{Block{data: 15}, Block{data: 25}, Block{}};
  showFirst(blocks);
}"""
        expect = """15"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_568(self):
        input = """type Vector2D struct {
  a float;
  b float;
}

func (vec Vector2D) magnitude() float {
  return vec.a * vec.a + vec.b * vec.b;
}

func main() {
  var vec Vector2D = Vector2D{b: 6.0, a: 8.0};
  putFloatLn(vec.magnitude());
}"""
        expect = """100.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_569(self):
        input = """type Coordinate struct {
  latitude int;
  longitude int;
}

func (coord Coordinate) shift(deltaLat int, deltaLong int) Coordinate {
  coord.latitude += deltaLat; 
  coord.longitude += deltaLong; 
  return coord;
}

func main() {
  var coord Coordinate = Coordinate{longitude: 20, latitude: 30};
  var newCoord Coordinate = coord.shift(5, -10);
  putIntLn(newCoord.latitude);
  putIntLn(newCoord.longitude);
}"""
        expect = """35
10
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_570(self):
        input = """func calculateTotal(x, y, z, p, q, r, s, t, u, v, w float, items [3][1]string) {
  putStringLn(items[0][0] + " " + items[1][0] + " " + items[2][0]);
  putFloatLn(x + y + z + p + q + r + s + t + u + v + w);
}

func main() {
  calculateTotal(8.5, 0x1C, 0b0110, 0.5, 42, 8, 2, 7, 5, 20 / 4.0, 0o123, [3][1]string{{"Greetings"}, {"from"}, {"calculateTotal"}});
}"""
        expect = """Greetings from calculateTotal
195.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_571(self):
        input = """const maxCount = 10;

func main() {
  for j := 0; j < maxCount; j := j + 1 {
    if (j % 3 == 0) {
      continue;
    }
    putIntLn(j);
  }
}"""
        expect = """1
2
4
5
7
8
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_572(self):
        input = """type Coordinates struct {
  lat float;
  lon float;
}

func (c1 Coordinates) computeDistance(c2 Coordinates) float {
  return (c1.lat - c2.lat) * (c1.lat - c2.lat) + (c1.lon - c2.lon) * (c1.lon - c2.lon)
}

func main() {
  var loc Coordinates = Coordinates{lat: 12.5, lon: 45.0};
  putFloatLn(loc.computeDistance(Coordinates{lon: 47.0, lat: 15.0}));
}"""
        expect = """10.25
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_573(self):
        input = """func main() {
  var matrix [3][2]int = [3][2]int{{7, 8}, {9, 10}, {11, 12}};
  putIntLn(matrix[1][0]);  // Output: 9
  putIntLn(matrix[2][1]);  // Output: 12
}"""
        expect = """9
12
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_574(self):
        input = """type Person struct {
  fullName string;
  years int;
}

func isSenior(p Person) boolean {
  return p.years >= 65;
}

func main() {
  var individual Person = Person{fullName: "Bob", years: 70};
  putBoolLn(isSenior(individual));
}"""
        expect = """true
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_575(self):
        input = """type Coordinate struct {
  latitude  int;
  longitude int;
}

type Renderable interface {
  render() string;
}

func (c Coordinate) render() string {
  return "Coordinate(" + formatInt(c.latitude) + ", " + formatInt(c.longitude) + ")";
}

func main() {
  var r Renderable = Coordinate{longitude: 10, latitude: 20};
  putStringLn(r.render());
}

func formatInt(value int) string {
  var result = "";
  var digits = [10]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
  for (value != 0) {
    remainder := value % 10;
    value := value / 10;
    result := digits[remainder] + result;
  }
  return result;
}"""
        expect = """Coordinate(20, 10)
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_576(self):
        input = """func main() {
  var counter int = 0;
  for (counter < 3) {
    putInt(counter);
    putString(" ");
    counter += 1;
  }
  putLn();
}"""
        expect = """0 1 2 
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_577(self):
        input = """type Polygon interface {
  perimeter() float;
}

type Triangle struct {
  side1 float;
  side2 float;
  side3 float;
}

func (t Triangle) perimeter() float {
  return t.side1 + t.side2 + t.side3;
}

var defaultTriangle = Triangle{}

func main() {
  var p Polygon = Triangle{side1: 3.0, side2: 4.0, side3: defaultTriangle.side1 + 1.0};
  putFloatLn(p.perimeter());
}"""
        expect = """8.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_578(self):
        input = """type Grid struct {
  x int;
  y int;
}

func multiply(m Grid) int {
  return m.x * m.y;
}

func main() {
  var g Grid = Grid{x: 2, y: 5};
  putIntLn(multiply(g)); 
}"""
        expect = """10
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_579(self):
        input = """func countFalse(array [4]boolean) int {
  var total int = 0;
  var index int = 0;
  for (index < 4) {
    if (!array[index]) {
      total += 1;
    }
    index += 1;
  }
  return total;
}

func main() {
  var states = [4]boolean{false, true, false, true};
  putIntLn(countFalse(states));
}"""
        expect = """2
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_580(self):
        input = """func isPrime(x int) boolean {
  if (x <= 1) {
    return false;
  }
  for var i = 2; i * i <= x; i += 1 {
    if (x % i == 0) {
      return false;
    }
  }
  return true;
}

func main() {
  var num int = 17;
  if (isPrime(num)) {
    putStringLn("Prime");
  } else {
    putStringLn("Not Prime");
  }
}"""
        expect = """Prime
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_581(self):
        input = """var flag boolean = false;
const toggle = true;

func main() {
  putBool(flag || toggle);
}"""
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_582(self):
        input = """type Notifier interface {
  notify() string;
}

type Service struct {
  title string;
}

func (s Service) notify() string {
  return "Service: " + s.title;
}

var n Notifier = Service{title: "WebHosting"};

func main() {
  putStringLn(n.notify());
}"""
        expect = """Service: WebHosting
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_583(self):
        input = """type Student struct {
  name string;
  grade int;
}

func main() {
  var s Student = Student{name: "Bob", grade: 85};
  putStringLn(s.name);
  putIntLn(s.grade);
}"""
        expect = """Bob
85
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_584(self):
        input = """func sumElements(arr [4]int) int {
  var total = 0;
  for var j = 0; j < 4; j += 1 {
    total += arr[j];
  }
  return total;
}

func main() {
  var numbers = [4]int{10, 20, 30, 40};
  var result = sumElements(numbers);
  putIntLn(result);
}"""
        expect = """100
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_585(self):
        input = """type Rectangle struct {
  length int;
  width int;
}

type AreaCalculator interface {
  calculateArea() int;
}

func (r Rectangle) calculateArea() int {
  return r.length * r.width;
}

var items [2]AreaCalculator;

func main() {
  var r1 Rectangle = Rectangle{width:3, length:4};
  var r2 Rectangle = Rectangle{length:5, width:6};
  items[0] := r1; items[1] := r2;
  putIntLn(items[0].calculateArea());
  putIntLn(items[1].calculateArea());
}"""
        expect = """12
30
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_586(self):
        input = """type Board struct {
  title string;
  grid [3][3]int;
}

func main() {
  var b Board = Board{grid: [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, title: "GameBoard"};
  putStringLn(b.title);
  putIntLn(b.grid[1][2]); // 6
  putIntLn(b.grid[2][0]); // 7
}"""
        expect = """GameBoard
6
7
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_587(self):
        input = """type Accumulator struct {
  total int;
}

func (a Accumulator) add(value int) Accumulator {
  a.total += value;
  return a;
}

func main() {
  var a Accumulator = Accumulator{total: 0};
  var count int = 0;
  for (count < 4) {
    a := a.add(3);
    putIntLn(a.total);
    count += 1;
  }
}"""
        expect = """3
6
9
12
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_588(self):
        input = """func factorial(n int) int {
  var result int = 1;
  var j int = 1;
  for (j <= n) {
    result *= j;
    j += 1;
  }
  return result;
}

func main() {
  var num int = 5;
  putIntLn(factorial(num));
}"""
        expect = """120
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))

    def test_589(self):
        input = """type Circle struct {
  radius int;
}

type PerimeterCalculator interface {
  computePerimeter() int;
}

func (c Circle) computePerimeter() int {
  return 2 * c.radius * 3;
}

var shapesArray [1]PerimeterCalculator;

func main() {
  var circle Circle = Circle{radius:7};
  shapesArray[0] := circle;
  putIntLn(shapesArray[0].computePerimeter());
}"""
        expect = """42
"""
        self.assertTrue(TestCodeGen.test(input, expect, next(num)))
