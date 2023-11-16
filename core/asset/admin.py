from django.contrib import admin
from .models.asset import Asset
from .models.asset_condition import AssetCondition
from .models.asset_type import AssetType
from .models.asset_status import AssetStatus

# Register your models here.

admin.site.register(Asset)
admin.site.register(AssetCondition)
admin.site.register(AssetType)
admin.site.register(AssetStatus)
