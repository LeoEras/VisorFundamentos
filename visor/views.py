from django.shortcuts import render
import re
from os import path
import glob, os
import xml.etree.ElementTree
import json
from django.http import JsonResponse
from django.template import RequestContext
#from django.http import HttpResponse

listErrorPython = ['StandardError', 'ArithmeticError', 'BufferError', 'LookupError', 'EnvironmentError',
					   'AssertionError', 'AttributeError', 'EOFError',
					   'FloatingPointError', 'GeneratorExit', 'IOError', 'ImportError', 'IndexError', 'KeyError',
					   'KeyboardInterrupt', 'MemoryError',
					   'NameError', 'NotImplementedError', 'OSError', 'OverflowError', 'ReferenceError', 'RuntimeError',
					   'StopIteration', 'SyntaxError',
					   'IndentationError', 'TabError', 'SystemError', 'SystemExit', 'TypeError', 'UnboundLocalError',
					   'UnicodeError', 'UnicodeEncodeError',
					   'UnicodeDecodeError', 'UnicodeTranslateError', 'ValueError', 'VMSError', 'WindowsError',
					   'ZeroDivisionError', 'FileNotFoundError']

# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.is_ajax():
            id_file = request.POST.get('id')
            path_file = path.realpath("visor\\gits\\2taller\\")
            file_open = open("".join(glob.iglob(os.path.join(path_file, "*" + id_file + "*"))), encoding='utf-8')
            file_open = file_open.read()
            #return JsonResponse({'file_open': json.dumps(file_open.decode("utf-8"))})
            return JsonResponse({'file_open': file_open})
    logs = path.realpath("visor\\gits\\2taller\\log.xml")
    e = xml.etree.ElementTree.parse(logs).getroot()
    list_output = []
    output_id = []
    error_caller_file = []
    line_error = []
    for atype in e.findall('log_project'):
        list_of_possible_error_files = []
        list_of_possible_line_error = []
        name_proy = atype.get('name_project')
        if atype.text is not None:
            for line in atype.text.splitlines():
                for item in listErrorPython:
                    if item in line:
                        list_output.append(line)
                        output_id.append(atype.get('id'))

            for line in atype.text.splitlines():
                if "File" in line and "line" in line and ".py" in line and name_proy in line: #El nombre del proyecto no debe de ir en blanco
                    line = line.replace('"', "")
                    line = str.split(line, "/")
                    for item in line:
                        if ".py" in item:
                            item = item.split(",")
                            list_of_possible_error_files.append(item[0])
                            list_of_possible_line_error.append(int(re.search(r'\d+', item[1]).group()))


            if len(list_of_possible_error_files) > 0:
                error_caller_file.append(list_of_possible_error_files[-1])
                line_error.append(list_of_possible_line_error[-1])

    for i in range(len(list_output)):
        output_id[i] = output_id[i] + "_" + error_caller_file[i]

    context = {"output_list": list_output,
               "output_id": output_id,
               "line_errors": line_error}
    return render(request, 'visor/index.html', context)
    #return render_to_response('visor/index.html', context_instance=RequestContext(request))