.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	bipush 42
.var 1 is x I from Label2 to Label3
	istore_1
	bipush 10
	newarray int
.var 2 is arr [I from Label2 to Label3
	astore_2
	aload_2
	iconst_0
	iload_1
	iastore
	iload_1
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
