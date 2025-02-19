from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.shortcuts import render
from .models import *
from .forms import PnsBigoForm, PnsModelForm, PnsCombiForm, PnsManagerForm

def pns(request):

    pns_bigo =  PnsBigo.objects.all()
    pns_mobile = PnsModel.objects.filter(type='모바일').order_by('type1')
    pns_combi = PnsCombi.objects.all()

    pns_sosang = PnsModel.objects.filter(type='소상공인')

    manager1 = PnsManager.objects.filter(type='일반고객')

    manager2 = PnsManager.objects.filter(type='소상공인')

    content = {
        'bigolist': pns_bigo, 
        'pns_mobile':pns_mobile,
        'pns_combi': pns_combi, 
        'pns_sosang' :pns_sosang, 
        'manager1' : manager1, 
        'manager2' : manager2
    }

    return render(request, 'pns_main.html',content )


def admin_page(request):
    def get_model_data(model):
        """모델 데이터를 리스트 형태로 변환"""
        fields = [field.name for field in model._meta.fields]
        data = model.objects.all().values(*fields)  # QuerySet → 딕셔너리 리스트 변환
        return {'name': model.__name__, 'fields': fields, 'data': data}

    models = [get_model_data(PnsBigo), get_model_data(PnsModel), get_model_data(PnsCombi), get_model_data(PnsManager)]

    return render(request, 'pns_admin.html', {'models': models})

# 데이터 추가
def add_item(request, model_type):
    if model_type == "bigo":
        form = PnsBigoForm(request.POST or None)
    elif model_type == "model":
        form = PnsModelForm(request.POST or None)
    elif model_type == "combi":
        form = PnsCombiForm(request.POST or None)
    elif model_type == "manager":
        form = PnsManagerForm(request.POST or None)
    else:
        return redirect('admin_page')

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('admin_page')

    return render(request, 'add_item.html', {'form': form})


# def edit_item(request):
#     if request.method == 'POST':
#         model_type = request.POST.get('model_type')
#         item_id = request.POST.get('item_id')

#         print(model_type, item_id)
        
#         if model_type == "bigo":
#             item = get_object_or_404(PnsBigo, id=item_id)
#             form = PnsBigoForm(request.POST, instance=item)
#         elif model_type == "model":
#             item = get_object_or_404(PnsModel, id=item_id)
#             form = PnsModelForm(request.POST, instance=item)
#         elif model_type == "combi":
#             item = get_object_or_404(PnsCombi, id=item_id)
#             form = PnsCombiForm(request.POST, instance=item)
#         elif model_type == "manager":
#             item = get_object_or_404(PnsManager, id=item_id)
#             form = PnsManagerForm(request.POST, instance=item)
#         else:
#             return JsonResponse({'success': False, 'error': 'Invalid model type'})

#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#         else:
#             return JsonResponse({'success': False, 'error': 'Form invalid'})

#     return JsonResponse({'success': False, 'error': 'Invalid request'})



def edit_item(request, model_type, item_id):
    if model_type == "pnsbigo":
        item = get_object_or_404(PnsBigo, id=item_id)
        form = PnsBigoForm(request.POST or None, instance=item)
    elif model_type == "model":
        item = get_object_or_404(PnsModel, id=item_id)
        form = PnsModelForm(request.POST or None, instance=item)
    elif model_type == "combi":
        item = get_object_or_404(PnsCombi, id=item_id)
        form = PnsCombiForm(request.POST or None, instance=item)
    elif model_type == "pnsmanager":
        item = get_object_or_404(PnsManager, id=item_id)
        form = PnsManagerForm(request.POST or None, instance=item)
    else:
        return redirect('admin_page')

   
    # POST 요청 처리
    if request.method == "POST" and form.is_valid():
        form.save()

        # AJAX 요청이면 JSON 응답 반환
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True})

        # 일반 요청이면 페이지 리디렉션
        return redirect('admin_page')

    # AJAX 요청에 대한 처리
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'edit_modal_form.html', {'form': form})

    # 일반 요청에 대한 처리
    return render(request, 'pns_admin.html', {'form': form})


# # 데이터 수정
# def edit_item(request, model_type, item_id):
#     print(f"Model Type: {model_type}, Item ID: {item_id}") 

#     if model_type == "pnsbigo":
#         item = get_object_or_404(PnsBigo, id=item_id)
#         form = PnsBigoForm(request.POST or None, instance=item)
#     elif model_type == "pnsmodel":
#         item = get_object_or_404(PnsModel, id=item_id)
#         form = PnsModelForm(request.POST or None, instance=item)
#     elif model_type == "pnscombi":
#         item = get_object_or_404(PnsCombi, id=item_id)
#         form = PnsCombiForm(request.POST or None, instance=item)
#     elif model_type == "pnsmanager":
#         item = get_object_or_404(PnsManager, id=item_id)
#         form = PnsManagerForm(request.POST or None, instance=item)
#     else:
#         return redirect('admin_page')

#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect('admin_page')

#     return render(request, 'pns_admin.html', {'form': form})

# 데이터 삭제
def delete_item(request, model_type, item_id):
    if model_type == "bigo":
        item = get_object_or_404(PnsBigo, id=item_id)
    elif model_type == "model":
        item = get_object_or_404(PnsModel, id=item_id)
    elif model_type == "combi":
        item = get_object_or_404(PnsCombi, id=item_id)
    elif model_type == "manager":
        item = get_object_or_404(PnsManager, id=item_id)
    else:
        return redirect('admin_page')

    if request.method == "POST":
        item.delete()
        return redirect('admin_page')

    return render(request, 'delete_confirm.html', {'item': item})