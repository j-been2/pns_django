from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.shortcuts import render
from .models import *
from .forms import PnsBigoForm, PnsModelForm, PnsCombiForm, PnsManagerForm

import json 

def pns(request):

    pns_bigo =  PnsBigo.objects.filter(de ='N')
    pns_mobile = PnsModel.objects.filter(de='N', type='모바일').order_by('type1')
    pns_combi = PnsCombi.objects.filter(de ='N')

    pns_sosang = PnsModel.objects.filter(de='N',type='소상공인')

    manager1 = PnsManager.objects.filter(de='N',type='일반고객')

    manager2 = PnsManager.objects.filter(de='N',type='소상공인')

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
    def get_model_data(model, table_name):
        """모델 데이터를 리스트 형태로 변환"""
        fields = [field.name for field in model._meta.fields]
        data = model.objects.filter(de='N').values(*fields)  # QuerySet → 딕셔너리 리스트 변환
        return {'table_name':table_name, 'name': model.__name__, 'fields': fields, 'data': data}

    models = [get_model_data(PnsBigo, '참고사항'), 
            get_model_data(PnsModel, '상품 현황'), 
            get_model_data(PnsCombi, '유무선 결합'), 
            get_model_data(PnsManager, '담당자 현황')]

    return render(request, 'pns_admin.html', {'models': models})



def edit(request):
    if request.method in ['GET', 'POST']:
        try:
            # if (isAuthorized(request) == False):
            #     raise AuthError("token is unauthorized.")

            received_data = json.loads(request.body.decode("utf-8"))
            # if 'id' not in received_data:
            #     raise Exception(
            #         '[id] key does not exist in your parameters.')
            

            model_type = received_data.get("modelType")
            item_id = received_data.get("itemId")
            updates = received_data.get("arr", [])

            if model_type == "PnsBigo":
                item = get_object_or_404(PnsBigo, id=item_id)
                update_data = {data["key"]: data["value"] for data in updates}
                form = PnsBigoForm(update_data, instance=item)
                if form.is_valid():
                    form.save()
                    return JsonResponse({"status": "success", "data": "수정 되었습니다."})
                else:
                    return JsonResponse({"status": "error", "message": "검증 실패", "errors": form.errors})

            elif model_type == "PnsModel":
                item = get_object_or_404(PnsModel, id=item_id)
                update_data = {data["key"]: data["value"] for data in updates}
                form = PnsModelForm(update_data, instance=item)
                if form.is_valid():
                    form.save()
                    return JsonResponse({"status": "success", "data": "수정 되었습니다."})
                else:
                    return JsonResponse({"status": "error", "message": "검증 실패", "errors": form.errors})

            elif model_type == "PnsCombi":
                item = get_object_or_404(PnsCombi, id=item_id)
                update_data = {data["key"]: data["value"] for data in updates}
                form = PnsCombiForm(update_data, instance=item)
                if form.is_valid():
                    form.save()
                    return JsonResponse({"status": "success", "data": "수정 되었습니다."})
                else:
                    return JsonResponse({"status": "error", "message": "검증 실패", "errors": form.errors})

            elif model_type == "PnsManager":
                item = get_object_or_404(PnsManager, id=item_id)
                update_data = {data["key"]: data["value"] for data in updates}
                form = PnsManagerForm(update_data, instance=item)
                if form.is_valid():
                    form.save()
                    return JsonResponse({"status": "success", "data": "수정 되었습니다."})
                else:
                    return JsonResponse({"status": "error", "message": "검증 실패", "errors": form.errors})
            else:
                return JsonResponse({"status": "error", "message": "", "errors": ''})


            # Response로 응답
            return JsonResponse({'returnCode': 'OK', 'message': '', 'data': '수정 되었습니다.'})

        except Exception as e:
            # 잘못된 토큰 (로그아웃/만료)
            if str(e) == "token is unauthorized.":
                return JsonResponse({'returnCode': 'NG', 'message': ''}, status=401)

            return JsonResponse({'returnCode': 'NG', 'message': ''})
    else:
        return JsonResponse({'returnCode': 'NG', 'message': ''}, status=405)




def delete(request):
    if request.method in ['GET', 'POST']:
        try:
            # if (isAuthorized(request) == False):
            #     raise AuthError("token is unauthorized.")

            received_data = json.loads(request.body.decode("utf-8"))
            # if 'id' not in received_data:
            #     raise Exception(
            #         '[id] key does not exist in your parameters.')
            

            model_type = received_data.get("modelType")
            item_id = received_data.get("itemId")
            print(model_type, item_id)
            if model_type == "PnsBigo":
                item = get_object_or_404(PnsBigo, id=item_id)
                item.de = 'Y'  # 특정 필드만 변경
                item.save(update_fields=['de'])  # 'de' 필드만 업데이트

                return JsonResponse({"status": "success", "data": "삭제 되었습니다."})

            # elif model_type == "PnsModel":
            #     item = get_object_or_404(PnsModel, id=item_id)
            #     update_data = {data["key"]: data["value"] for data in updates}
            #     form = PnsModelForm(update_data, instance=item)
            #     if form.is_valid():
            #         form.save()
            #         return JsonResponse({"status": "success", "data": "수정 되었습니다."})
            #     else:
            #         return JsonResponse({"status": "error", "message": "검증 실패", "errors": form.errors})

            # elif model_type == "PnsCombi":
            #     item = get_object_or_404(PnsCombi, id=item_id)
            #     update_data = {data["key"]: data["value"] for data in updates}
            #     form = PnsCombiForm(update_data, instance=item)
            #     if form.is_valid():
            #         form.save()
            #         return JsonResponse({"status": "success", "data": "수정 되었습니다."})
            #     else:
            #         return JsonResponse({"status": "error", "message": "검증 실패", "errors": form.errors})

            # elif model_type == "PnsManager":
            #     item = get_object_or_404(PnsManager, id=item_id)
            #     update_data = {data["key"]: data["value"] for data in updates}
            #     form = PnsManagerForm(update_data, instance=item)
            #     if form.is_valid():
            #         form.save()
            #         return JsonResponse({"status": "success", "data": "수정 되었습니다."})
            #     else:
            #         return JsonResponse({"status": "error", "message": "검증 실패", "errors": form.errors})

            # Response로 응답
            return JsonResponse({'returnCode': 'OK', 'message': '', 'data': '수정 되었습니다.'})

        except Exception as e:
            print(e)
            # 잘못된 토큰 (로그아웃/만료)
            if str(e) == "token is unauthorized.":
                return JsonResponse({'returnCode': 'NG', 'message': ''}, status=401)

            return JsonResponse({'returnCode': 'NG', 'message': ''})
    else:
        return JsonResponse({'returnCode': 'NG', 'message': ''}, status=405)






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