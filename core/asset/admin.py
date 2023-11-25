from django.contrib import admin
from .models.asset import Asset
from .models.asset_type import AssetType
from .models.asset_status import AssetStatus
from .models.license import License,LicenseCategory
from .models.accessory import Accessory, AccessoryCategory

# Register your models here.

admin.site.register(Asset)
admin.site.register(AssetType)
admin.site.register(AssetStatus)
admin.site.register(License)
admin.site.register(LicenseCategory)
admin.site.register(Accessory)
admin.site.register(AccessoryCategory)