// Transcrypt'ed from Python, 2023-11-24 17:56:41
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {log} from './math.js';
var __name__ = '__main__';
export var function1 = function () {
	var value1 = document.getElementsByName ('num1') [0].value;
	var value2 = document.getElementsByName ('num2') [0].value;
	if (value1 == '' || value2 == '') {
		window.alert ('Your textbox is empty');
		return ;
	}
	var b0 = 45.64998705;
	var b1 = 11.023;
	var b2 = 9.646;
	var x1 = int (value1);
	var x2 = int (value2);
	var numbers = (b0 + b1 * (1 - log (x1))) + b2 * Math.pow (100 - x2, 1 / 2);
	document.getElementById ('sorted').innerHTML = str (numbers);
};
export var function2 = function () {
	var value1 = document.getElementsByName ('num1') [0].value;
	var value2 = document.getElementsByName ('num2') [0].value;
	var value3 = document.getElementsByName ('num3') [0].value;
	var value4 = document.getElementsByName ('num4') [0].value;
	if (value1 == '' || value2 == '') {
		window.alert ('Your textbox is empty');
		return ;
	}
	var b0 = 45.64998705;
	var b1 = 11.023;
	var b2 = 9.646;
	var x1 = int (value1);
	var x2 = int (value2);
	var numbers1 = (b0 + b1 * (1 - log (x1))) + b2 * Math.pow (100 - x2, 1 / 2);
	var x1 = int (value1) + int (value3);
	var x2 = int (value2) + int (value4);
	var numbers2 = (b0 + b1 * (1 - log (x1))) + b2 * Math.pow (100 - x2, 1 / 2);
	var numbers = (numbers1 / numbers2 - 1) * 100;
	document.getElementById ('sorted').innerHTML = str (numbers) + '%';
};

//# sourceMappingURL=library.map