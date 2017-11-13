from django.shortcuts import render
from os import path
import xml.etree.ElementTree
#from django.http import HttpResponse

# Create your views here.
def index(request):
    logs = path.realpath("visor\\gits\\2taller\\log.xml")
    e = xml.etree.ElementTree.parse(logs).getroot()
    list_output = []
    output_id = []
    for atype in e.findall('log_project'):
        if atype.text is not None:
            for line in atype.text.splitlines():
                if "Error" in line:
                    list_output.append(line)
                    output_id.append(atype.get('id'))
    #file = open(logs)
    #content = file.read()
    context = {"output_list": list_output,
               "output_id": output_id}
    return render(request, 'visor/index.html', context)
