import typehint as th
import inspect
import ast
import _ast
import subprocess
import tempfile
import ctypes

class ClowLang:
    def __init__(self, cc='cc', cflags=('-lstdc++', '-fPIC', '-shared')):
        self.types = th.TypeHints()
        self._cc_args = [cc] + list(cflags)
        self._functions = []

    def compiled(self, f):
        self._functions.append(f)

    def _compile_functions(self, path):
        ir = '\n'.join(self.generate_code(f) for f in self._functions)

        with make_temp(suffix='.cpp') as cpp:
            cpp.write(ir.encode())
            cpp.flush()
            subprocess.check_output(self._cc_args + [cpp.name, '-o', path])

    def compile_tempfile(self):
        with make_temp(suffix='.so', delete=False) as obj:
            self._compile_functions(obj.name)
            return obj.name

    def compile_and_attach(self):
        with make_temp(suffix='.so', delete=False) as obj:
            self._compile_functions(obj.name)
            return ctypes.cdll.LoadLibrary(obj.name)

    def generate_code(self, f):
        source = inspect.getsource(f.__code__)
        module = ast.parse(source)
  
        return Templates.FUNCTION.format(function=f.__name__, ret='int')

class Templates:
    FUNCTION = """
        extern "C" @ret@ @function@()
        {
            return 0;
        }
    """

def _fix_template(template):
    shift = '\n'.join(line[8:] for line in template.split('\n')).strip()
    opened = False
    for c in shift:
        if c == '@':
            yield '}' if opened else '{'
            opened = not opened
        elif c in '{}':
            yield c * 2
        else:
            yield c

def _fix_templates():
    for name in dir(Templates):
        if name[0].isupper():
            fixed = ''.join(_fix_template(getattr(Templates, name)))
            setattr(Templates, name, fixed)

_fix_templates()
make_temp = tempfile.NamedTemporaryFile
