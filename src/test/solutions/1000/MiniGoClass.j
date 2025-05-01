.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	aastore
.var 1 is arr [[I from Label2 to Label3
	astore_1
	iconst_0
.var 2 is i I from Label2 to Label3
	istore_2
Label6:
	iload_2
	iconst_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	iconst_0
.var 3 is j I from Label9 to Label10
	istore_3
Label13:
	iload_3
	iconst_2
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
Label16:
	aload_1
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/putIntLn(I)V
Label17:
Label11:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label13
Label12:
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
Label3:
Label1:
	return
.limit stack 7
.limit locals 4
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
