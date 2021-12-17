# Solid 开发原则

参考：

1. <http://www.10tiao.com/html/788/201810/2247489713/1.html>
2. <http://www.cnblogs.com/TomXu/archive/2011/12/15/2288411.html>

用来更好地进行面向对象编程，五大原则分别是：

1.  The Single Responsibility Principle（单一职责 SRP）：一个类或者方法只完成一种功能
2.  The Open/Closed Principle（开闭原则 OCP）: 一个类或者方法对内关闭，对外开放
3.  The Liskov Substitution Principle（里氏替换原则 LSP）：
4.  The Interface Segregation Principle（接口分离原则 ISP）
5.  The Dependency Inversion Principle（依赖倒置原则 DIP）

## [单一职责 SRP](http://www.cnblogs.com/TomXu/archive/2012/01/06/2305513.html)

原文描述：类发生更改的原因应该只有一个

一个类只应该负责一件事。如果一个类有多个职责，那么它变成了耦合的。对一个职责的修改会导致对另一个职责的修改

> 注意：这个原则不仅适用于类，也适用于软件组件和微服务

例如，考虑下面的设计：

```
class Animal {
    constructor(name: string){ }
    getAnimalName() { }
    saveAnimal(a: Animal) { }
}
```

上面的 Animal 就违反了单一职责原则（SRP）

它为什么违反了 SRP？

SRP 指出，类应该有一个职责，在这里，我们可以得出两个职责：动物数据库管理和动物属性管理。构造函数和 getAnimalName 管理动物属性，而 saveAnimal 管理 Animal 在数据库中的存储。

这种设计将来会带来什么问题？

如果应用程序的修改影响了数据库管理功能，使用 Animal 属性的类就必须修改和重新编译，以适应这种新的变化。这个系统就有点像多米诺骨牌，触碰一张牌就会影响到其他牌。

为了使这个类符合 SRP，我们创建了另一个类，它负责将动物存储到数据库中这个单独的职责：

```javascript
class Animal {
  constructor(name: string) {}
  getAnimalName() {}
}
class AnimalDB {
  getAnimal(a: Animal) {}
  saveAnimal(a: Animal) {}
}
```

> 在设计我们的类时，我们应该把相关的特性放在一起，这样，每当它们需要改变的时候，它们都是因为同样的原因而改变。如果它们因不同的原因而改变，我们就应该尝试将它们分开。——Steve Fenton

恰当运用这条原则，我们的应用程序就会变成高内聚的。

### 我们如何知道一个对象的多个行为构造多个职责还是单个职责？

1.  Information holder – 该对象设计为存储对象并提供对象信息给其它对象。
2.  Structurer – 该对象设计为维护对象和信息之间的关系
3.  Service provider – 该对象设计为处理工作并提供服务给其它对象
4.  Controller – 该对象设计为控制决策一系列负责的任务处理
5.  Coordinator – 该对象不做任何决策处理工作，只是 delegate 工作到其它对象上
6.  Interfacer – 该对象设计为在系统的各个部分转化信息（或请求）

## [开闭原则 OCP](http://www.cnblogs.com/TomXu/archive/2012/01/09/2306329.html)

原文描述：软件实体（类，模块，方法等等）应当对扩展开放，对修改关闭，即软件实体应当在不修改的前提下扩展

open for extension（对扩展开放）的意思是说当新需求出现的时候，可以通过扩展现有模型达到目的。而 Close for modification（对修改关闭）的意思是说不允许对该实体做任何修改，说白了，就是这些需要执行多样行为的实体应该设计成不需要修改就可以实现各种的变化，坚持开闭原则有利于用最少的代码进行项目维护。

英文原文：<http://freshbrewedcode.com/derekgreer/2011/12/19/solid-javascript-the-openclosed-principle/>

让我们继续以 Animal 类为例。

```
class Animal {
    constructor(name: string){ }
    getAnimalName() { }
}
```

我们希望遍历一个动物列表，发出它们的声音。

```javacript
//...
const animals: Array<Animal> = [
    new Animal('lion'),
    new Animal('mouse')
];
function AnimalSound(a: Array<Animal>) {
    for(int i = 0; i <= a.length; i++) {
        if(a[i].name == 'lion')
            log('roar');
        if(a[i].name == 'mouse')
            log('squeak');
    }
}
AnimalSound(animals);
```

函数 AnimalSound 不符合开闭原则，因为它不能对新的动物关闭。如果我们添加一种新的动物-蛇：

```
//...
const animals: Array<Animal> = [
    new Animal('lion'),
    new Animal('mouse'),
    new Animal('snake')
]
//...
```

我们就不得不修改 AnimalSound 函数：

```
//...
function AnimalSound(a: Array<Animal>) {
    for(int i = 0; i <= a.length; i++) {
        if(a[i].name == 'lion')
            log('roar');
        if(a[i].name == 'mouse')
            log('squeak');
        if(a[i].name == 'snake')
            log('hiss');
    }
}
AnimalSound(animals);
```

如你所见，对于每一种新的动物，一段新的逻辑会被添加到 AnimalSound 函数。这是一个非常简单的例子。当应用程序变得庞大而复杂时，你会看到，每添加一种新动物，if 语句就得在 AnimalSound 函数中重复一遍。

如何使它（AnimalSound）符合 OCP？

```
class Animal {
        makeSound();
        //...
}
class Lion extends Animal {
    makeSound() {
        return 'roar';
    }
}
class Squirrel extends Animal {
    makeSound() {
        return 'squeak';
    }
}
class Snake extends Animal {
    makeSound() {
        return 'hiss';
    }
}
//...
function AnimalSound(a: Array<Animal>) {
    for(int i = 0; i <= a.length; i++) {
        log(a[i].makeSound());
    }
}
AnimalSound(animals);
```

Animal 现在有了一个新方法 makeSound。我们让每一种动物扩展 Animal 类并实现 makeSound 方法。

每一种动物都加入自己的发声方法（makeSound）实现。AnimalSound 遍历动物数组并调用每种动物的 makeSound 方法。

现在，如果我们添加一种新动物，AnimalSound 不需要修改。我们需要做的就是把新动物加入到动物数组中。

AnimalSound 方法符合 OCP 原则了。

再举个例子。假如你有一家商店，你使用下面的类给自己最喜欢的客户 20% 的折扣：

```
class Discount {
    giveDiscount() {
        return this.price * 0.2
    }
}
```

当你决定给 VIP 客户双倍的折扣（40%）时，你可能会这样修改这个类：

```
class Discount {
    giveDiscount() {
        if(this.customer == 'fav') {
            return this.price * 0.2;
        }
        if(this.customer == 'vip') {
            return this.price * 0.4;
        }
    }
}
```

这就违反了 OCP 原则。OCP 禁止这样做。如果想给不同类型的客户一个新的折扣百分比，就得添加一段新的逻辑。

为了使它遵循 OCP 原则，我们将新建一个类来扩展 Discount。在这个新类中，我们将重新实现它的行为：

```
class VIPDiscount: Discount {
    getDiscount() {
        return super.getDiscount() * 2;
    }
}
```

如果你决定给超级 VIP 客户 80% 的折扣，那么代码是下面这个样子：

```
class SuperVIPDiscount: VIPDiscount {
    getDiscount() {
        return super.getDiscount() * 2;
    }
}
```

就是这样，扩展而不修改。

## [里氏替换原则 LSP](http://www.cnblogs.com/TomXu/archive/2012/01/10/2310244.html)

原文描述：Subtypes must be substitutable for their base types.
派生类型必须可以替换它的基类型。

简单描述：子类必须可以替换它的超类。

在面向对象编程里，继承提供了一个机制让子类能共享基类的代码，这是通过在基类型里封装通用的数据和行为来实现的，这个原则的目的是确保子类可以替换它的基类而没有错误。如果你发现自己的代码在检查类的类型，那么它一定违反了这个原则

让我们以 Animal 为例。

```
//...
function AnimalLegCount(a: Array<Animal>) {
    for(int i = 0; i <= a.length; i++) {
        if(typeof a[i] == Lion)
            log(LionLegCount(a[i]));
        if(typeof a[i] == Mouse)
            log(MouseLegCount(a[i]));
        if(typeof a[i] == Snake)
            log(SnakeLegCount(a[i]));
    }
}
AnimalLegCount(animals);
```

上述方法违反了 LSP 原则（也违反了 OCP 原则）。它必须知道每一种 Animal 类型，并调用相应的数腿函数。

每次创建一个新的动物类，都得修改这个函数：

```
//...
class Pigeon extends Animal {

}
const animals[]: Array<Animal> = [
    //...,
    new Pigeon();
]
function AnimalLegCount(a: Array<Animal>) {
    for(int i = 0; i <= a.length; i++) {
        if(typeof a[i] == Lion)
            log(LionLegCount(a[i]));
        if(typeof a[i] == Mouse)
            log(MouseLegCount(a[i]));
         if(typeof a[i] == Snake)
            log(SnakeLegCount(a[i]));
        if(typeof a[i] == Pigeon)
            log(PigeonLegCount(a[i]));
    }
}
AnimalLegCount(animals);
```

为了使这个函数符合 LSP 原则，我们将遵循 Steve Fenton 提出的 LSP 要求：

- 如果超类（Animal）有一个方法接受超类类型（Anima）的参数，那么它的子类（Pigeon）应该接受超类类型（Animal 类型）或子类类型（Pigeon 类型）作为参数。

- 如果超类返回一个超类类型（Animal）, 那么它的子类应该返回一个超类类型（Animal 类型）或子类类型（Pigeon 类型）。

现在，我们可以重新实现 AnimalLegCount 函数了：

```
function AnimalLegCount(a: Array<Animal>) {
    for(let i = 0; i <= a.length; i++) {
        a[i].LegCount();
    }
}
AnimalLegCount(animals);
```

AnimalLegCount 函数并不关心传递的动物类型，它只管调用 LegCount 方法。它只知道参数必须是 Animal 类型，要么是 Animal 类，要么是它的子类。

现在，Animal 类必须实现 / 定义一个 LegCount 方法：

```
class Animal {
    //...
    LegCount();
}
```

而它的子类必须实现 LegCount 方法：

```
//...
class Lion extends Animal{
    //...
    LegCount() {
        //...
    }
}
//...
```

当它被传递给 AnimalLegCount 函数时，它会返回一头狮子的腿数。

如你所见，AnimalLegCount 不需要知道动物的类型就可以返回它的腿数，它只调用了 Animal 类型的 LegCount 方法，因为根据约定，Animal 类的一个子类必须实现 LegCount 函数。

## [接口隔离原则 ISP](http://www.cnblogs.com/TomXu/archive/2012/02/14/2330137.html)

原文描述：Clients should not be forced to depend on methods they do not use.
不应该强迫客户依赖于它们不用的方法

简单描述：创建特定于客户端的细粒度接口。不应该强迫客户端依赖于它们不使用的接口

当用户依赖的接口方法即便只被别的用户使用而自己不用，那它也得实现这些接口，换而言之，一个用户依赖了未使用但被其他用户使用的接口，当其他用户修改该接口时，依赖该接口的所有用户都将受到影响。这显然违反了开闭原则，也不是我们所期望的。

接口隔离原则 ISP 和单一职责有点类似，都是用于聚集功能职责的，实际上 ISP 可以被理解才具有单一职责的程序转化到一个具有公共接口的对象

这个原则是为了克服实现大接口的缺点。让我们看看下面的 IShape 接口：

```
interface IShape {
    drawCircle();
    drawSquare();
    drawRectangle();
}
```

这个接口可以绘制正方形、圆形、矩形。实现 IShape 接口的类 Circle、Square 和 Rectangle 必须定义方法 drawCircle()、drawSquare()、drawRectangle()。

```
class Circle implements IShape {
    drawCircle(){
        //...
    }
    drawSquare(){
        //...
    }
    drawRectangle(){
        //...
    }
}
class Square implements IShape {
    drawCircle(){
        //...
    }
    drawSquare(){
        //...
    }
    drawRectangle(){
        //...
    }
}
class Rectangle implements IShape {
    drawCircle(){
        //...
    }
    drawSquare(){
        //...
    }
    drawRectangle(){
        //...
    }
}
```

上面的代码很有趣。类 Rectangle 实现了它没有使用的方法 drawCircle 和 drawSquare，同样，Square 实现了 drawCircle 和 drawRectangle，Circle 实现了 drawSquare 和 drawRectangle。

如果我们向 IShape 接口添加另一个方法，比如 drawTriangle()：

```
interface IShape {
    drawCircle();
    drawSquare();
    drawRectangle();
    drawTriangle();
}
```

那么，这些类就必须实现新方法，否则就会抛出错误。

我们看到，不可能实现这样一种形状类，它可以画圆，但不能画矩形、正方形或三角形。我们在实现方法时可以只抛出一个错误，表明操作无法执行。

ISP 反对 IShape 接口的这种设计。客户端（这里是 Rectangle、Circle 和 Square）不应该被迫依赖于它们不需要或不使用的方法。另外，ISP 指出，接口应该只执行一个任务（就像 SRP 原则一样），任何额外的行为都应该抽象到另一个接口中。

在这里，我们的 IShape 接口执行了应该由其他接口独立处理的操作。为了使 IShape 接口符合 ISP 原则，我们将对不同接口的操作进行隔离：

```
interface IShape {
    draw();
}
interface ICircle {
    drawCircle();
}
interface ISquare {
    drawSquare();
}
interface IRectangle {
    drawRectangle();
}
interface ITriangle {
    drawTriangle();
}
class Circle implements ICircle {
    drawCircle() {
        //...
    }
}
class Square implements ISquare {
    drawSquare() {
        //...
    }
}
class Rectangle implements IRectangle {
    drawRectangle() {
        //...
    }
}
class Triangle implements ITriangle {
    drawTriangle() {
        //...
    }
}
class CustomShape implements IShape {
   draw(){
      //...
   }
}
```

ICircle 接口仅处理圆的绘制，IShape 处理任何形状的绘制，ISquare 只处理正方形的绘制，IRectangle 处理矩形的绘制。

或者，类（Circle、Rectangle、Square、Triangle）必须继承 IShape 接口，并实现自己的绘制行为。

```
class Circle implements IShape {
    draw(){
        //...
    }
}

class Triangle implements IShape {
    draw(){
        //...
    }
}

class Square implements IShape {
    draw(){
        //...
    }
}

class Rectangle implements IShape {
    draw(){
        //...
    }
}
```

然后，我们可以使用 I- 接口创建具体的形状，如半圆、直角三角形、等边三角形、钝边矩形等。

## [依赖倒置原则 DIP](http://www.cnblogs.com/TomXu/archive/2012/02/15/2330143.html)

依赖倒置原则的描述：
A. High-level modules should not depend on low-level modules. Both should depend on abstractions.
高级模块不应该依赖于低级模块，二者都应该依赖于抽象

B. Abstractions should not depend upon details. Details should depend upon abstractions.
抽象不应该依赖于细节，细节应该依赖于抽象

在软件开发中，我们的应用程序最终主要是由模块组成。当这种情况出现时，我们必须使用依赖注入来解决。高级组件依赖于低级组件发挥作用。

```
class XMLHttpService extends XMLHttpRequestService {}
class Http {
    constructor(private xmlhttpService: XMLHttpService) { }
    get(url: string , options: any) {
        this.xmlhttpService.request(url,'GET');
    }
    post() {
        this.xmlhttpService.request(url,'POST');
    }
    //...
}
```

这里，Http 是高级组件，而 HttpService 是低级组件。这种设计违反了 DIP A：高级模块不应该依赖于低级模块。它应该依赖于它的抽象。

该 Http 类被迫依赖于 XMLHttpService 类。如果我们要修改 Http 连接服务，也许我们想通过 Nodejs 连接到互联网，甚至模拟 http 服务。我们将不得不费力地遍历所有 Http 实例来编辑代码，这违反了 OCP 原则。

Http 类不应该关心使用的 Http 服务的类型。我们做了一个 Connection 接口：

```
interface Connection {
    request(url: string, opts:any);
}
```

Connection 接口有一个 request 方法。有了这个接口，我们就可以向 Http 类传递一个 Connection 类型的参数：

```
class Http {
    constructor(private httpConnection: Connection) { }
    get(url: string , options: any) {
        this.httpConnection.request(url,'GET');
    }
    post() {
        this.httpConnection.request(url,'POST');
    }
    //...
}
```

因此，无论传递给 Http 类的 Http 连接服务是什么类型，它都可以轻松地连接到网络，而无需知道网络连接的类型。

现在，我们重新实现 XMLHttpService 类来实现 Connection 接口：

```
class XMLHttpService implements Connection {
    const xhr = new XMLHttpRequest();
    //...
    request(url: string, opts:any) {
        xhr.open();
        xhr.send();
    }
}
```

我们可以创建许多 Http 连接类型，并将其传递给 Http 类，而不必担心错误。

```
class NodeHttpService implements Connection {
    request(url: string, opts:any) {
        //...
    }
}
class MockHttpService implements Connection {
    request(url: string, opts:any) {
        //...
    }
}
```

现在，我们可以看到，高级模块和低级模块都依赖于抽象。Http 类（高级模块）依赖于 Connection 接口（抽象），而 Http 服务类型（低级模块）也依赖于 Connection 接口（抽象）。

此外，DIP 原则会强制我们遵循里氏替换原则：Connection 类型 Node-XML-MockHttpService 可以替换它们的父类型连接。

## 总结

### 1、单一职责（Single Responsibility Principle，SRP）

### 2、开闭原则（Open Closed Principle，OCP）

此原则是由 Bertrand Meyer 提出的。原文是：“Software entities should be open for extension,but closed for modification”。

模块应**对扩展开放，而对修改关闭**。模块应尽量在不修改原来的代码的情况下进行扩展。

举个例子，假设现在有一个已经开发完成的规模不小的软件系统，有人提需求说我要再加一个功能，那么这时候去修改源代码显然是不明智的，不仅违反了开闭原则，而且那么多的代码，工作量肯定也很大。为了要实现这个需求，可以在原来的软件系统中扩展出来一个功能，只需要编写调试这个新功能模块的代码，这就是**开放扩展，关闭修改**。

### 3、里氏代换原则（Liskov Substitution Principle，LSP）

里氏代换原则是由 Barbara Liskov 提出的。可以描述为：**子类继承于父类，可以单独调用，如果调用的是父类的话，那么换成子类也完全可以运行。**从开闭原则可以看出，设计模式一个重要的部分是抽象化，里氏代换原则从另一个角度描述了抽象（父类）和具体（子类）之间的关系。举例，猫科动物可以完成捕猎这个动作，而老虎也可以完成捕猎，在这个例子中，猫科动物就是父类，老虎是继承于猫科动物、从猫科动物这个类扩展出来的子类。

可以说：**里氏代换原则是继承复用的一个基础。**

### 4、接口隔离原则（Interface Segregation Principle，ISP）

**每一个接口都是一个角色，客户端不应该依赖于它不需要的接口。**

也就是：**一个类对另一个类的依赖应该建立在最小的接口上**。

意思是这样的：应该把每一个**接口都细化，针对类去设计接口**。如果一个接口里含有太多的方法，而对很多类来说里面的很多方法都是用不到的，那么另外的类在实现这个接口时就要实现很多对它来说没用的方法，浪费人力物力。对一个类来说，实现很多它都能用得上的专用接口总比让它实现一个臃肿而又有很多它用不上的方法要划得来。

采用接口隔离原则对接口进行约束时，要注意以下几点：

接口尽量小，但是要有限度。对接口进行细化可以提高程序设计灵活性是不挣的事实，但是如果过小，则会造成接口数量过多，使设计复杂化。所以一定要适度。

为依赖接口的类定制服务，只暴露给调用的类它需要的方法，它不需要的方法则隐藏起来。只有专注地为一个模块提供定制服务，才能建立最小的依赖关系。

提高内聚，减少对外交互。使接口用最少的方法去完成最多的事情。

运用接口隔离原则，一定要适度，接口设计的过大或过小都不好。

### 5、依赖倒转原则（Dependency Inversion Principle，DIP）

**若引用的对象有底层类型，那么就直接引用底层类型。高层模块不应该依赖于底层模块**

换句话说，在程序里面调用的时候调用子类 ，子类依赖于父类，而父类不要依赖于子类。也就是说，细节依赖于抽象，可是抽象不应该依赖于细节。

依赖倒转原则要求程序设计时应该考虑如何针对抽象编程。

以计算机系统为例，依赖倒转原则要求要**针对接口编程**，而不是针对实现编程。无论键盘鼠标、CPU、内存等等这些硬件都是针对接口设计的，而如果要针对实现来设计，硬盘就要对应到某个特定（品牌/类型）的主板，那么换硬盘时就需要把主板也换掉。

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQxMjQxOTkzM119
-->
