from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

import requests

from FirstProgect.settings import BASE_DIR

# Create your views here.

from .forms import companyDatasetForm
from .models import companyDataset


class companySearchMapListView(View):
    template_name = 'company_maplist.html'
    

    def get(self, request, *args, **kwargs):
        context = {'MyApiKey': self.MyApiKey_}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        search_str_ = self.request.POST.get('search_')
        if not search_str_:
            context = {
                'search_result': search_str_,
                'MyApiKey': self.MyApiKey_
            }
        else:
            handleFileSystemStorage = FileSystemStorage()
            obj_list = searchInFile('BGMOPEN1.csv', search_str_,
                                    handleFileSystemStorage, 2)
            addr_list, num_list, name_list = '', '', ''
            obj_list = sorted(obj_list, key=lambda x: -int(x[4]))
            addr_list = ','.join(x[0] for x in obj_list)
            num_list = ','.join(x[1] if int(x[4]) != 0 else str(0)
                                for x in obj_list)
            name_list = ','.join(x[3] for x in obj_list)
            context = {
                'addr_list': addr_list,
                'name_list': name_list,
                'num_list': num_list,
                'search_result': search_str_,
                'MyApiKey': self.MyApiKey_
            }
        return render(request, self.template_name, context)


class companySearchListView(View):
    template_name = 'company_list.html'

    def get(self, request, *args, **kwargs):
        api_ = APIresult()
        context = {'list_length': 0, 'object_list': None, 'api_result': api_}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        search_str_ = self.request.POST.get('search_')
        if not search_str_:
            context = {
                'list_length': 0,
                'object_list': None,
                'search_result': search_str_,
            }
        else:
            handleFileSystemStorage = FileSystemStorage()
            obj_list = searchInFile('BGMOPEN1.csv', search_str_,
                                    handleFileSystemStorage, 2)
            obj_list = sorted(obj_list, key=lambda x: -int(x[4]))
            context = {
                'list_length': obj_list.__len__(),
                'object_list': obj_list,
                'search_result': search_str_,
            }
        return render(request, self.template_name, context)


def APIresult():
    # BaseRequestURL = 'https://schema.nat.gov.tw/'
    # ExtraRequestURL = '/v1/data/CompanyandBusiness/company/JurisiticPersonType/JuristicPersonName'
    requestURL = 'http://data.gcis.nat.gov.tw/od/data/api/5F64D864-61CB-4D0D-8AD9-492047CC1EA6?$format=json&$filter=Business_Accounting_NO eq 20828393&$skip=0&$top=50'
    # requestURL = 'https://schema.nat.gov.tw/v1/data/CompanyandBusiness/company/JurisiticPersonType/JuristicPersonBAN/22099131/'
    # 好像卡在正規表示式
    response = requests.get(requestURL)
    data = response.text
    return data


def searchInFile(fileName, searchStr, handler, idx=0):
    searchResult = []
    # Because, the Kit was not at the same path with this project.
    # To fix this, need to use Virtualenv.
    fileURL = handler.location
    fileURL = fileURL + '\\' + fileName
    searchStr = searchStr.split(' ')
    # fileURL = handler.url(fileName)
    with open(fileURL, 'r', encoding="utf-8") as file_:
        for i, row in enumerate(file_):
            if i < idx:
                pass
            #elif searchStr in row:
            else:
                if searchStr[0] in row:
                    check = 1
                    for str_ in searchStr:
                        if str_ not in row:
                            check = 0
                            break
                    if check == 1:
                        row = strQ2B(row)
                        row = "".join(row)
                        row = row.replace(' ', '')
                        row = row.replace('"', '')
                        row = row.split(",")
                        if row.__len__() == 16:
                            searchResult.append(row)
    return searchResult


def strQ2B(string_in):
    # 把字串全形轉半形
    rstring = ""
    for uchar in string_in:
        if uchar == '，':
            uchar = '.'
        u_code = ord(uchar)
        if u_code == 12288:  # 全形空格直接轉換
            u_code = 32
        elif 65281 <= u_code <= 65374:  # 全形字元（除空格）根據關係轉化
            u_code -= 65248
        rstring += chr(u_code)
    return rstring


def strB2Q(string_in):
    # 把字串半形轉全形
    rstring = ""
    for uchar in string_in:
        u_code = ord(uchar)
        if u_code == 32:  # 全形空格直接轉換
            u_code = 12288
        elif 33 <= u_code <= 126:  # 全形字元（除空格）根據關係轉化
            u_code += 65248
        rstring += chr(u_code)
    return rstring


@login_required(login_url='/admin/')
def uploadCompanyDataset(request):
    form = companyDatasetForm(request.POST or None, request.FILES or None)
    file_name = None
    file_url = None
    file_status = False
    if form.is_valid() and request.FILES:
        handleFileSystemStorage = FileSystemStorage()
        if not handleFileSystemStorage.exists(
                request.FILES['input_file'].name):
            handleFileSystemStorage.save(request.FILES['input_file'].name,
                                         request.FILES['input_file'])
            file_name = request.FILES['input_file'].name
            file_url = handleFileSystemStorage.url(file_name)
        else:
            file_name = request.FILES['input_file'].name
            file_url = handleFileSystemStorage.url(file_name)
            file_status = True
        form = companyDatasetForm()
    context = {
        'form': form,
        'file_name': file_name,
        'file_url': file_url,
        'file_status': file_status,
    }
    return render(request, 'company_upload.html', context)
