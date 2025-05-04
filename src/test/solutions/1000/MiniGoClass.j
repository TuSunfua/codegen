.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	new Y
	dup
	ldc 12.0
	aconst_null
	iconst_0
	new X
	dup
	ldc 1.2
	iconst_4
	i2f
	iconst_1
	invokespecial X/<init>(FFZ)V
	invokespecial Y/<init>(FLjava/lang/String;ZLX;)V
.var 1 is y LY; from Label2 to Label3
	astore_1
	aload_1
	ldc "oke"
	invokevirtual Y/setS(Ljava/lang/String;)V
	aload_1
	getfield Y/x LX;
	invokevirtual X/getX1()F
Label3:
Label1:
	return
.limit stack 10
.limit locals 2
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
