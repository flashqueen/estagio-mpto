import json
from django.http.response import HttpResponse
from django.db import transaction
from django.db.models import Q


def make_rest(Serializer):

    Model = Serializer.Model()

    def _delete_by_id(request, id):
        status  = 200
        result = {}


        try:
            instance = Model.objects.get(id=id)
            instance.delete()
            status = 204
            result = None
        except Model.DoesNotExist:
            status = 404
            result = {
                'message': f'Estado  com ID igual a {id} nao existe'
            }
        except Exception as e:
            instance = 400
            result = {
                'message': str(e)
            }

        return HttpResponse(
            status=status,
            content_type='application/json',
            content=json.dumps(result) if result else ''
        )

    def _update_by_id(request, id):
        status  = 200
        result = {}


        try:
            with transaction.atomic():
                instance = Model.objects.get(id=id)
                data = json.loads(request.body)

                for key, value in data.items():
                    setattr(instance, key, value)

                instance.save()
                result = Serializer.serializer(instance)
        except Model.DoesNotExist:
            status = 404
            result = {
                'message': f'Estado  com ID igual a {id} nao existe'
            }
        except Exception as e:
            status = 400
            result = {
                'message': str(e)
            }

        return HttpResponse(
            status=status,
            content_type='application/json',
            content=json.dumps(result) if result else ''
        )

    def _get_by_id(request, id):
        status  = 200
        result = {}


        try:
            result = Serializer.serializer(
                Model.objects.get(id=id)
            )
        except Model.DoesNotExist:
            status = 404
            result = {
                'message': f'Estado  com ID igual a {id} nao existe'
            }

        return HttpResponse(
            status=status,
            content_type='application/json',
            content=json.dumps(result)
        )

    def _do_filter(base_query, filters):
        data = json.loads(filters) if filters else []
        stages = {}
        for expression in data:
            stage_number = expression.get('stage', 1)
            stage = stages.get(stage_number, [])
            if stage_number >= 0:
                stage.append(
                    Q(**{
                        expression.get('property'): expression.get('value')
                    })
                )
            else:
                stage.append(
                    ~Q(**{
                        expression.get('property'): expression.get('value')
                    })
                )
            stages.update({
                stage_number:  stage
            })

        query = None
        for stage_number in stages.keys():
            expressions = stages.get(stage_number)
            sub_query = None

            for expression in expressions:
                if not sub_query:
                    sub_query = expression
                else:
                    sub_query |= expression

            if not query:
                query = sub_query
            else:
                query &= sub_query

        return base_query.filter(query)if query else base_query
    
    def _list(request):
        query = Model.objects.all()
        response = HttpResponse()
        response.status_code = 501

        try:
            query = _do_filter(
                query,
                request.GET.get('filters')
            )

            if query.exists():
                response = HttpResponse(
                    content_type='application/json',
                    content=json.dumps([
                        Serializer.serializer(state) for state in query
                    ])
                    )
            else:
                response.status_code = 404

            return response
        except Exception as e:
            response = HttpResponse(
                status = 400,
                content_type='application/json',
                content = json.dumps({
                    'message': str(e)
                })
            )

    def _create(request):
        response = None

        try:
            with transaction.atomic():
                data = json.loads(request.body)
                instance = Serializer.deserializer(data)
                instance.save()

                response = HttpResponse(
                    content=json.dumps(
                        Serializer.serializer(instance)
                    ),
                    status=201
                )
        except Exception as e:
            response = HttpResponse(
                content=json.dumps({
                    'message': str(e)
                }),
                status=400
            )

        return response

    def _index(request):
        response = None
        if request.method == 'GET':
            response = _list(request)

        elif request.method == 'POST':
            response = _create(request)


        return response

    def _by_id(request, id):
            if request.method == 'GET':
                return _get_by_id(request, id)
            elif request.method == 'DELETE':
                return _delete_by_id(request, id)
            elif request.method == 'PUT':
                return _update_by_id(request, id)
            else:
                return HttpResponse(status=501)

    
    return _index, _by_id