from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers, generics
from rest_framework import status
from django.shortcuts import get_object_or_404



class API_objects(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)


@api_view(['POST'])
def add_items(request):
	item = ItemSerializer(data=request.data)
	if Item.objects.filter(**request.data).exists():                              #create
		raise serializers.ValidationError('This data already exists')

	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    # if there is something in items else raise error            #listview
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request, pk):
	item = Item.objects.get(pk=pk)
	data = ItemSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()                                         #update view
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(Item, pk=pk)
	item.delete()                                               #delete
	return Response(status=status.HTTP_202_ACCEPTED)


