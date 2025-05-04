.source MiniGoClass.java
.class public X
.super java.lang.Object
.field x1 F
.field x2 F
.field isInit Z

.method public <init>(FFZ)V
.var 0 is this LX; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	fload_1
	putfield X/x1 F
	aload_0
	fload_2
	putfield X/x2 F
	aload_0
	iload_3
	putfield X/isInit Z
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public getX1()F
Label0:
Label2:
	aload_0
	getfield X/x1 F
	freturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method

.method public setInit(Z)V
Label0:
.var 1 is b Z from Label0 to Label1
Label2:
	aload_0
	iconst_1
	iload_1
	iand
	putfield X/isInit Z
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
