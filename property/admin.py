from django.contrib import admin
from .models import Flat
from .models import Complaint
from .models import Owner
class AdminInline(admin.TabularInline):
    model = Owner.owner_flats.through
    raw_id_fields = ("owner",)

@admin.register(Flat)
class SearchAdmin(admin.ModelAdmin):
    search_fields = ('owner','town','address')
    readonly_fields = ["created_at"]
    list_display = ["address","price","new_building","construction_year","town"]
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number","has_balcony","construction_year","town"]
    raw_id_fields = ("liked_by",)
    exclude = ("flats_in_ownership",)
    inlines = [AdminInline]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("user","flat",)
    
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("owner_flats",)