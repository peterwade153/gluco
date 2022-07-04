from rest_framework.pagination import PageNumberPagination


class GlucosePageNumberPagination(PageNumberPagination):

    page_size = 15
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 50 # max number of glucose level readings
