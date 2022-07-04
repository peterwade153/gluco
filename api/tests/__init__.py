from rest_framework.test import APITestCase

from api.models import GlucoseLevel



class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.record1 = GlucoseLevel.objects.create(
            user_id = "cccccccc-cccc-cccc-cccc-cccccccccccc",
            seriennummer = "e09bb0f0-018b-429b-94c7-62bb306a0136",
            gerätezeitstempel= "2021-10-02T09:08:00Z",
            aufzeichnungstyp= 0,
            glukosewert_verlauf= 138,
            glukose_scan= 0
        )
        self.record2 = GlucoseLevel.objects.create(
            user_id = "cccccccc-cccc-cccc-cccc-cccccccccccc",
            seriennummer = "e09bb0f0-018b-429b-94c7-62bb306a0136",
            gerätezeitstempel= "2021-10-02T09:08:00Z",
            aufzeichnungstyp= 0,
            glukosewert_verlauf= 138,
            glukose_scan= 0
        )
        self.record3 = GlucoseLevel.objects.create(
            user_id = "cccccccc-cccc-cccc-cccc-cccccccccccc",
            seriennummer = "e09bb0f0-018b-429b-94c7-62bb306a0136",
            gerätezeitstempel= "2021-10-02T09:08:00Z",
            aufzeichnungstyp= 0,
            glukosewert_verlauf= 138,
            glukose_scan= 0
        )
