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

def index(request):
    context = {}
    if request.method == 'POST':
        return render(request, 'visor/individual.html', context)
    else:
        return render(request, 'visor/index.html', context)

# Create your views here.
def individual(request):
    list_dir = []
    identificador = request.GET.get('Identificador', "")
    for item in os.listdir("visor\\gits\\"+ identificador + "\\"):
        if ".git" in item:
            continue
        if os.path.isdir(path.realpath("visor\\gits\\" + identificador + "\\" + item)):
            list_dir.append(item)

    if request.method == 'POST':
        if request.is_ajax():
            id_file = request.POST.get('id')
            proj_dir = request.POST.get('selected')
            if id_file is not None:
                path_file = path.realpath("visor\\gits\\" + identificador + "\\" + proj_dir)
                file_open = open("".join(glob.iglob(os.path.join(path_file, "*" + id_file + "*"))), encoding='utf-8')
                file_open = file_open.read()
                return JsonResponse({'file_open': file_open})
            else:
                if proj_dir is not None:
                    list_output, output_id, line_error = getLogData(proj_dir, identificador)
                    return JsonResponse({"output_list": list_output,
                   "output_id": output_id,
                   "line_errors": line_error,
                   "directory_list": list_dir})
    list_output, output_id, line_error = getLogData(list_dir[0], identificador)
    context = {"output_list": list_output,
               "output_id": output_id,
               "line_errors": line_error,
               "directory_list": list_dir}
    return render(request, 'visor/individual.html', context)
    #return render_to_response('visor/individual.html', context_instance=RequestContext(request))

def getLogData(selected_dir, identificador):
    logs = path.realpath("visor\\gits\\" + identificador + "\\" + selected_dir + "\\log.xml")
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

    if len(error_caller_file) > 0:
        for i in range(len(list_output)):
            output_id[i] = output_id[i] + "_" + error_caller_file[i]

    return list_output, output_id, line_error