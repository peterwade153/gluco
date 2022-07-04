from rest_framework import status

from . import BaseAPITestCase


class GlucoseAPITestCase(BaseAPITestCase):
    
    def test_list_levels(self):
        response = self.client.get('/api/v1/levels/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_levels_by_ID(self):
        response = self.client.get(f'/api/v1/levels/{self.record1.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_levels_ordering_by_id(self):
        response = self.client.get('/api/v1/levels/?ordering=id', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_levels_limit_size(self):
        response = self.client.get('/api/v1/levels/?size=5', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_levels_by_page(self):
        response = self.client.get('/api/v1/levels/?page=1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_levels_by_stop_and_start(self):
        response = self.client.get('/api/v1/levels/?start=2021-02-02T03:03:00Z&stop=2021-11-02T03:03:00Z', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
