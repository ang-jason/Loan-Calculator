'use strict';var random={};import{AssertionError,AttributeError,BaseException,DeprecationWarning,Exception,IndexError,IterableError,KeyError,NotImplementedError,RuntimeWarning,StopIteration,UserWarning,ValueError,Warning,__JsIterator__,__PyIterator__,__Terminal__,__add__,__and__,__call__,__class__,__envir__,__eq__,__floordiv__,__ge__,__get__,__getcm__,__getitem__,__getslice__,__getsm__,__gt__,__i__,__iadd__,__iand__,__idiv__,__ijsmod__,__ilshift__,__imatmul__,__imod__,__imul__,__in__,__init__,__ior__,
__ipow__,__irshift__,__isub__,__ixor__,__jsUsePyNext__,__jsmod__,__k__,__kwargtrans__,__le__,__lshift__,__lt__,__matmul__,__mergefields__,__mergekwargtrans__,__mod__,__mul__,__ne__,__neg__,__nest__,__or__,__pow__,__pragma__,__proxy__,__pyUseJsNext__,__rshift__,__setitem__,__setproperty__,__setslice__,__sort__,__specialattrib__,__sub__,__super__,__t__,__terminal__,__truediv__,__withblock__,__xor__,abs,all,any,assert,bool,bytearray,bytes,callable,chr,copy,deepcopy,delattr,dict,dir,divmod,enumerate,
filter,float,getattr,hasattr,input,int,isinstance,issubclass,len,list,map,max,min,object,ord,pow,print,property,py_TypeError,py_iter,py_metatype,py_next,py_reversed,py_typeof,range,repr,round,set,setattr,sorted,str,sum,tuple,zip}from"./org.transcrypt.__runtime__.js";import*as __module_random__ from"./random.js";__nest__(random,"",__module_random__);var __name__="__main__";export var array=[];export var gen_random_int=function(number,seed){var result=null;var result=list(range(number));random.seed(seed);
random.shuffle(result);return result};export var generate=function(){var number=10;var seed=200;array=null;array=gen_random_int(number,seed);var array_str=null;var str_comma="";var array_str=str_comma.join(str(array));print(array_str);document.getElementById("generate").innerHTML=array_str};export var bubble_sort=function(array){var y=0;while(y<2*len(array)+1){for(var i=0;i<len(array)-1;i++)if(array[i]>array[i+1]){var __left0__=tuple([array[i+1],array[i]]);array[i]=__left0__[0];array[i+1]=__left0__[1]}var y=
y+1}};export var sortnumber1=function(){bubble_sort(array);var array_str=null;var str_comma="";var array_str=str_comma.join(str(array));print(array_str);document.getElementById("sorted").innerHTML=array_str};export var sortnumber2=function(){var value=document.getElementsByName("numbers")[0].value;if(value==""){window.alert("Your textbox is empty");return}var array_str=null;document.getElementById("sorted").innerHTML=array_str};export var grab_parameters=function(){var loanAmount=document.getElementById("loanAmount").value;
var loanTenor=document.getElementById("loanTenor").value;var interestRate=document.getElementById("interestRate").value;var termPeriod=document.getElementById("termPeriod").value;console.log(loanAmount,loanTenor,interestRate,termPeriod)};

//# sourceMappingURL=library.map