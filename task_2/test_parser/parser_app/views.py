from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from parser_app.services import XlsxDecode, ParseService


class APIParse(APIView):

    def post(self, request):
        if request.FILES.get('file', None):   
            list_id = XlsxDecode.decode(request.FILES['file'])
            results = ParseService.show_data(list_id)
            return Response(results, status=status.HTTP_200_OK)

        id = request.data.get('id', None)
        if not id:
            return Response(status=status.HTTP_200_OK)
        results = ParseService.show_data([id])
        return Response(results, status=status.HTTP_200_OK)
