from django.core.serializers import serialize
import json
class serializeMixin(object):
    def serialize(self,qs):
        json_data=serialize('json',qs)
        p_data=json.loads(json_data)
        final_list=[]
        for obj in p_data:
            emp_data=obj['fields']
            if 'adv_name' in emp_data.keys():
                emp_data["Advisor_ID"] = obj['pk']
            else:
                emp_data["Booking_ID"] = obj['pk']
                emp_data["Advisor_ID"] = emp_data['advisor']
                emp_data.pop('advisor')
            final_list.append(emp_data)
        json_data=json.dumps(final_list)
        return json_data
    def serialize1(self,qs):
        json_data=serialize('json',qs)
        p_data=json.loads(json_data)
        final_list=[]
        for obj in p_data:
            emp_data=obj['fields']
            final_list.append(emp_data)
            for obj in final_list:
                if obj[""] == 'Faiz':
                    json_data=json.dumps(obj)
        return json_data

from django.http import HttpResponse
class HttpResponseMixin(object):
    def render_to_http_resourse(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)
