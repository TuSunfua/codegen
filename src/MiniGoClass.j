.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	aconst_null
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc "food"
	aastore
	aastore
.var 1 is a [[Ljava/lang/String; from Label2 to Label3
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_0
	ldc "no"
	aastore
	aload_1
	iconst_0
	aaload
	iconst_0
	aaload
	ldc " "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload_1
	iconst_1
	aaload
	iconst_0
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	ldc " I feel hungry"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 7
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
