# 2213841
from Utils import *
from StaticCheck import *
from StaticError import *
import CodeGenerator as cgen
from MachineCode import JasminCode

class Emitter():
    def __init__(self, func):
        self.data = {}
        self.func = func
        self.current = ""
        self.buff = list()
        self.jvm = JasminCode()
        
    def setContext(self, context):
        if self.current:
            self.data[self.current] = self.buff
        if self.data.get(context) is None:
            self.data[context] = list()
        self.buff = self.data[context]
        self.current = context
        
    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        elif typeIn is FloatType:
            return "F"
        elif typeIn is BoolType:
            return "Z"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            return "[" * len(inType.dimens) + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        elif typeIn is cgen.ClassType or typeIn is Id:
            return "L" + inType.name + ";"
        elif typeIn is type(None):
            return "Ljava/lang/Object;"
        else:
            return str(typeIn)

    def getFullType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is FloatType:
            return "float"
        elif typeIn is BoolType:
            return "boolean"
        elif typeIn is cgen.StringType:
            return "java/lang/String"
        elif typeIn is VoidType:
            return "void"
        elif typeIn is ArrayType:
            return "[" * len(inType.dimens) + self.getFullType(inType.eleType)
        elif typeIn is MType:
            return "(" + "".join(list(map(lambda x: self.getFullType(x), inType.partype))) + ")" + self.getFullType(inType.rettype)
        elif typeIn is cgen.ClassType or typeIn is Id:
            return inType.name
        elif typeIn is type(None):
            return "java/lang/Object"

    def emitPUSHICONST(self, in_, frame):
        #in: Int or Sring
        #frame: Frame
        
        frame.push()
        if type(in_) is int:
            i = in_
            if i >= -1 and i <=5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
            elif i >= -2147483648 and i <= 2147483647:
                return self.jvm.emitLDC(str(i))
        elif type(in_) is str:
            frame.pop()
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)

    def emitPUSHFCONST(self, in_, frame):
        #in_: String
        #frame: Frame
        
        f = float(in_)
        frame.push()
        rst = "{0:.1f}".format(f)
        if f == 0.0 or f == 1.0 or f == 2.0:
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDC(in_)       
        
    def emitPUSHNULL(self, frame):
        #frame: Frame
        
        frame.push()
        return self.jvm.emitPUSHNULL()

    ''' 
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''
    def emitPUSHCONST(self, in_, typ, frame):
        #in_: String
        #typ: Type
        #frame: Frame
        
        if type(typ) is IntType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is FloatType:
            return self.emitPUSHFCONST(in_, frame)
        elif type(typ) is BoolType:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC(in_)
        elif type(typ) is ArrayType or type(typ) is cgen.ClassType or type(typ) is Id:
            frame.push()
            return self.jvm.emitLDC(in_)
        elif type(typ) is type(None):
            return self.emitPUSHNULL(frame)
        else:
            raise IllegalOperandException(in_)

    ##############################################################

    def emitALOAD(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...
        
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        if type(in_) is FloatType:
            return self.jvm.emitFALOAD()
        if type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is ArrayType or type(in_) is StringType or type(in_) is cgen.ClassType or type(in_) is Id:
            return self.jvm.emitAALOAD()
        elif type(in_) is type(None):
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))

    def emitASTORE(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...
        
        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        if type(in_) is FloatType:
            return self.jvm.emitFASTORE()
        if type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif type(in_) is ArrayType or type(in_) is StringType or type(in_) is cgen.ClassType or type(in_) is Id:
            return self.jvm.emitAASTORE()
        elif type(in_) is type(None):
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))

    '''    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    '''
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        #in_: Int
        #varName: String
        #inType: Type
        #fromLabel: Int
        #toLabel: Int
        #frame: Frame
        
        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #... -> ..., value
        
        frame.push()
        if type(inType) is IntType:
            return self.jvm.emitILOAD(index)
        if type(inType) is FloatType:
            return self.jvm.emitFLOAD(index)
        if type(inType) is BoolType:
            return self.jvm.emitILOAD(index)
        elif type(inType) is ArrayType or type(inType) is StringType or type(inType) is cgen.ClassType or type(inType) is Id:
            return self.jvm.emitALOAD(index)
        elif type(inType) is type(None):
            return self.jvm.emitALOAD(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''
    def emitREADVAR2(self, name, typ, frame):
        #name: String
        #typ: Type
        #frame: Frame
        #... -> ..., value

        #frame.push()
        raise IllegalOperandException(name)

    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''
    def emitWRITEVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #..., value -> ...
        
        frame.pop()

        if type(inType) is IntType:
            return self.jvm.emitISTORE(index)
        if type(inType) is FloatType:
            return self.jvm.emitFSTORE(index)
        if type(inType) is BoolType:
            return self.jvm.emitISTORE(index)
        if type(inType) is StringType:
            return self.jvm.emitASTORE(index)
        elif type(inType) is ArrayType or type(inType) is cgen.ClassType or type(inType) is Id:
            return self.jvm.emitASTORE(index)
        elif type(inType) is type(None):
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''
    def emitWRITEVAR2(self, name, typ, frame):
        #name: String
        #typ: Type
        #frame: Frame
        #..., value -> ...

        #frame.push()
        raise IllegalOperandException(name)

    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    '''
    def emitATTRIBUTE(self, lexeme, in_, isStatic, isFinal, value):
        #lexeme: String
        #in_: Type
        #isFinal: Boolean
        #value: String
        if isStatic:
            return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), isFinal, value)
        else:
            return self.jvm.emitINSTANCEFIELD(lexeme, self.getJVMType(in_), isFinal, value)
    
    def emitGETSTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        
        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        #lexeme: String
        #in_: Type
        #frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    ''' generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    '''
    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ) is VoidType:
            frame.push()
        frame.pop()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))
    
    def emitINVOKEINTERFACE(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        length = len(list(map(lambda x: frame.pop(), typ.partype))) + 1
        if not type(typ) is VoidType:
            frame.push()
        frame.pop()
        return self.jvm.emitINVOKEINTERFACE(lexeme, self.getJVMType(in_), length)

    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''
    def emitNEGOP(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., value -> ..., result

        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        #in_: Type
        #frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST("true", in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST("false", in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''
    def emitADDOP(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        if lexeme == "+":
            if type(in_) is IntType:
                frame.pop()
                return self.jvm.emitIADD()
            elif type(in_) is FloatType:
                frame.pop()
                return self.jvm.emitFADD()
            elif type(in_) is StringType:
                return self.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), frame)
        else:
            if type(in_) is IntType:
                frame.pop()
                return self.jvm.emitISUB()
            else:
                frame.pop()
                return self.jvm.emitFSUB()

    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emitDIV(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIREM()

    '''
    *   generate iand
    '''

    def emitANDOP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    '''
    *   generate ior
    '''
    def emitOROP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, in_, frame):
        # ..., value1, value2 -> ..., result (0 or 1)

        result = []
        labelTrue = frame.getNewLabel()
        labelEnd = frame.getNewLabel()

        if isinstance(in_, StringType):
            if op in ["==", "!="]:
                result += [
                    self.emitINVOKEVIRTUAL("java/lang/String/equals",
                                        MType([cgen.ClassType("java/lang/Object")], BoolType()), frame)
                ]
                if op == "==":
                    result.append(self.jvm.emitIFNE(labelTrue))  # if true -> jump
                else:
                    result.append(self.jvm.emitIFEQ(labelTrue))  # if false -> jump
            else:
                result += [
                    self.emitINVOKEVIRTUAL("java/lang/String/compareTo",
                                        MType([cgen.ClassType("java/lang/String")], IntType()), frame)
                ]
                if op == "<":
                    result.append(self.jvm.emitIFLT(labelTrue))
                elif op == ">":
                    result.append(self.jvm.emitIFGT(labelTrue))
                elif op == "<=":
                    result.append(self.jvm.emitIFLE(labelTrue))
                elif op == ">=":
                    result.append(self.jvm.emitIFGE(labelTrue))
        elif isinstance(in_, FloatType):
            result.append(self.jvm.emitFCMPL())
            if op == ">":
                result.append(self.jvm.emitIFGT(labelTrue))
            elif op == ">=":
                result.append(self.jvm.emitIFGE(labelTrue))
            elif op == "<":
                result.append(self.jvm.emitIFLT(labelTrue))
            elif op == "<=":
                result.append(self.jvm.emitIFLE(labelTrue))
            elif op == "!=":
                result.append(self.jvm.emitIFNE(labelTrue))
            elif op == "==":
                result.append(self.jvm.emitIFEQ(labelTrue))
        elif isinstance(in_, IntType) or isinstance(in_, BoolType):
            if op == ">":
                result.append(self.jvm.emitIFICMPGT(labelTrue))
            elif op == ">=":
                result.append(self.jvm.emitIFICMPGE(labelTrue))
            elif op == "<":
                result.append(self.jvm.emitIFICMPLT(labelTrue))
            elif op == "<=":
                result.append(self.jvm.emitIFICMPLE(labelTrue))
            elif op == "!=":
                result.append(self.jvm.emitIFICMPNE(labelTrue))
            elif op == "==":
                result.append(self.jvm.emitIFICMPEQ(labelTrue))
        else:
            raise Exception(f"Unsupported type for relational operator: {in_}")

        # false case
        result.append(self.emitPUSHCONST("0", IntType(), frame))
        result.append(self.emitGOTO(labelEnd, frame))

        # true case
        result.append(self.emitLABEL(labelTrue, frame))
        result.append(self.emitPUSHCONST("1", IntType(), frame))

        # end
        result.append(self.emitLABEL(labelEnd, frame))
        return ''.join(result)

    def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
        #op: String
        #in_: Type
        #trueLabel: Int
        #falseLabel: Int
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = list()

        frame.pop()
        frame.pop()
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(falseLabel))
            result.append(self.emitGOTO(trueLabel))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(falseLabel))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(falseLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(falseLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(falseLabel))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(falseLabel))
        result.append(self.jvm.emitGOTO(trueLabel))
        return ''.join(result)

    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''

    def emitMETHOD(self, lexeme, in_, isStatic=False, isAbstract=False):
        #lexeme: String
        #in_: Type
        #isStatic: Boolean
        #isAbstract: Boolean
        
        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic, isAbstract)
    
    def emitIMPLEMENTS(self, lexeme):
        #lexeme: String

        return self.jvm.emitIMPLEMENTS(lexeme)

    '''   generate the end directive for a function.
    '''
    def emitENDMETHOD(self, frame):
        #frame: Frame

        buffer = list()
        if frame:
            buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
            buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def getConst(self, ast):
        #ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())

    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''

    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    '''

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''
    def emitIFTRUE(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)

    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''
    def emitIFFALSE(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)
    
    def emitIFEQ(self, label, frame):   
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFEQ(label)
    
    def emitIFNE(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFNE(label)

    def emitIFICMPGT(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)    
    
    def emitNEW(self, lexem, frame):
        frame.push()
        return self.jvm.emitNEW(lexem)
    
    def emitANEWARRAY(self, in_, frame):
        #in_: Type
        #frame: Frame

        if isinstance(in_, ArrayType):
            type_str = self.getJVMType(in_.eleType)
            if len(in_.dimens) == 1:
                type_str = type_str[1:-1]
            else:
                type_str = '[' * (len(in_.dimens) - 1) + type_str
            return self.jvm.emitANEWARRAY(type_str)
    
    def emitNEWARRAY(self, in_, frame):
        if not isinstance(in_, ArrayType):
            raise IllegalOperandException(str(in_))
        
        dim_count = len(in_.dimens)
        eleType = in_.eleType
        
        if dim_count == 1:
            if isinstance(eleType, (IntType, FloatType, BoolType)):
                # Single-dimensional primitive array: use newarray
                return self.jvm.emitNEWARRAY(self.getFullType(eleType))
            else:
                # Single-dimensional reference array: use anewarray
                return self.emitANEWARRAY(in_, frame)
        else:
            # Multi-dimensional array: use multianewarray
            return self.jvm.emitMULTIANEWARRAY(self.getJVMType(in_), str(dim_count))
            
    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''
    def emitDUP(self, frame):
        #frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''
    def emitI2F(self, frame):
        #frame: Frame

        return self.jvm.emitI2F()

    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    '''

    def emitRETURN(self, in_, frame):
        #in_: Type
        #frame: Frame

        if type(in_) is IntType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is StringType:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is ArrayType or type(in_) is cgen.ClassType or type(in_) is Id:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is type(None):
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()

    ''' generate code that represents a label	
    *   @param label the label
    *   @return code Label<label>:
    '''
    def emitLABEL(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitLABEL(label)

    ''' generate code to jump to a label	
    *   @param label the label
    *   @return code goto Label<label>
    '''
    def emitGOTO(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitGOTO(str(label))

    # Generate some startup code for a class or an interface.
    def emitPROLOG(self, source, name, isClass=True, parent=""):
        #source: String
        #name: String
        #isClass: Boolean
        #parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(source + ".java"))
        if isClass:
            result.append(self.jvm.emitCLASS("public " + name))
        else:
            result.append(self.jvm.emitINTERFACE("public " + name))
        result.append(self.jvm.emitSUPER("java/lang/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        #num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        #num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        for key in self.data:
            filename, buff = self.func(key), self.data[key]
            with open(filename, "w") as file:
                file.write(''.join(buff))

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''
    def printout(self, in_):
        #in_: String

        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()
        