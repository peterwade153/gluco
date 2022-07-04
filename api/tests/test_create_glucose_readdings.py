from rest_framework import status

from . import BaseAPITestCase


class CreateGlucoseAPITestCase(BaseAPITestCase):
    
    def test_list_levels(self):
        data = {
            "user_id": "cccccccc-cccc-cccc-cccc-cccccccccccc",
            "seriennummer": "e09bb0f0-018b-429b-94c7-62bb306a0136",
            "aufzeichnungstyp": 0,
            "glukosewert_verlauf": 139,
            "glukose_scan": 0
        }
        response = self.client.post('/api/v1/levels/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
