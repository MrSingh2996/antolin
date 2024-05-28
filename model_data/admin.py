from django import forms
from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import admin, messages
from .models import Customer, ModelData

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class CustomerInline(admin.TabularInline):
    model = Customer
    extra = 1  # Number of empty forms to display

class ModelDataInline(admin.TabularInline):
    model = ModelData
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    change_list_template = "admin/customer_changelist.html"
    list_display = ("name", "serial_number", "customer_number")

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            for line in lines:
                fields = line.split(",")
                if len(fields) >= 3:
                    Customer.objects.create(name=fields[0], serial_number=fields[1], customer_number=fields[2])
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        return render(request, "admin/csv_form.html", {"form": form})

@admin.register(ModelData)
class ModelDataAdmin(admin.ModelAdmin):
    change_list_template = "admin/modeldata_changelist.html"
    list_display = ("model_name", "glue", "water", "roving", "roller_temperature", "tool_temp_top", "tool_temp_middle", "tool_temp_bottom", "wjc_pressure", "date", "shift")

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            for line in lines:
                fields = line.split(",")
                if len(fields) >= 11:
                    ModelData.objects.create(model_name=fields[0], glue=fields[1], water=fields[2], roving=fields[3], roller_temperature=fields[4], tool_temp_top=fields[5], tool_temp_middle=fields[6], tool_temp_bottom=fields[7], wjc_pressure=fields[8], date=fields[9], shift=fields[10])
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        return render(request, "admin/csv_form.html", {"form": form})
