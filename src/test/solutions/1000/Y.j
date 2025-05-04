.source MiniGoClass.java
.class public Y
.super java.lang.Object
.field b F
.field s Ljava/lang/String;
.field c Z
.field x LX;

.method public <init>(FLjava/lang/String;ZLX;)V
.var 0 is this LY; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	fload_1
	putfield Y/b F
	aload_0
	aload_2
	putfield Y/s Ljava/lang/String;
	aload_0
	iload_3
	putfield Y/c Z
	aload_0
	aload 4
	putfield Y/x LX;
Label1:
	return
.limit stack 2
.limit locals 5
.end method

.method public getB()F
Label0:
Label2:
	aload_0
	getfield Y/b F
	freturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method

.method public setS(Ljava/lang/String;)V
Label0:
.var 1 is ss Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Y/s Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
