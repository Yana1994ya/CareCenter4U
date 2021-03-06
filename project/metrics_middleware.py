import json
import time

from django.db import connection
from django.conf import settings
from django.http import HttpResponse


class MetricsMiddleware:
    """
    MetricsMiddleware adds performance metrics to the response.

    It adds the following
      - Request processing time.
      - Number of queries
      - Actual sql queries
      - duplicate queries
      - sql total time
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.start_time = time.time()
        response = self.get_response(request)

        # Add metrics only when DEBUG is True.
        if not settings.DEBUG:
            return response

        metrics = self.gather_metrics()
        response = self.add_metrics_to_response(response, **metrics)

        return response

    @staticmethod
    def gather_metrics():
        queries_count = len(connection.queries)
        sql_time = 0

        sql_queries = []
        duplicate_queries = []
        for index, query in enumerate(connection.queries):
            sql_query = str(query["sql"])
            sql_query = sql_query.replace("\"", "'")

            if sql_query in sql_queries:
                duplicate_queries.append(sql_query)

            sql_queries.append(sql_query)

            sql_time += float(query["time"])

        return {
            'queries_count': queries_count,
            'sql_queries': sql_queries,
            'duplicate_queries': duplicate_queries,
            'sql_total_time': sql_time
        }

    def add_metrics_to_response(self, response, **kwargs):
        # and response.get('content-type') == "application/json":
        if isinstance(response, HttpResponse):
            try:
                request_processing_time = time.time() - self.start_time
                response["number_of_queries"] = kwargs['queries_count']
                response["sql_queries"] = kwargs['sql_queries']
                response["duplicate_queries"] = kwargs['duplicate_queries']
                response["sql_total_time"] = kwargs['sql_total_time']
                response["request_processing_time"] = "{}s".format(round(request_processing_time, 3))

            except TypeError as e:
                return response

        return response
