import dis
def magic_calculation(a,b):
    return a + b
result = magic_calculation(0,1)
print(result)

>>> bytecode = dis.Bytecode(magic_calculation)
>>> for instr in bytecode:
... print(instr.opname)
...
LOAD_GLOBAL
LOAD_FAST
CALL_FUNCTION
RETURN_VALUE
