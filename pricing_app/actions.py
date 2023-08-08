import pandas as pd
from django.http import HttpResponse
from django.utils.text import slugify


def export_to_csv(modeladmin, request, queryset):
    model_name = slugify(queryset.model.__name__).lower()

    fields = [field.name for field in queryset.model._meta.get_fields() if not field.is_relation]

    data = queryset.values(*fields)

    df = pd.DataFrame.from_records(data)

    # Generate a filename for the CSV file
    filename = f"{model_name}_records.csv"

    # Prepare the HTTP response with the CSV file as content
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename={filename}"

    df.to_csv(response, index=False)

    return response


export_to_csv.short_description = "Export selected records to CSV"
