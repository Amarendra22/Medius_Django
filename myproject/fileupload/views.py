from django.shortcuts import render
from django.contrib import messages
from .resources import uFileResource
from .models import uFile
from tablib import Dataset
from datetime import datetime
import csv

def simple_upload(request):
    if request.method == 'POST':
        uFile_resource = uFileResource()
        dataset = Dataset()
        new_uFile = request.FILES['myfile']

        if not (new_uFile.name.endswith('xlsx') or new_uFile.name.endswith('.csv')):
            messages.error(request, 'Wrong file format. Please upload an .xlsx file.')
            return render(request, 'upload.html')
        
        try:
            if new_uFile.name.endswith('.xlsx'):
                dataset = Dataset()
                imported_data = dataset.load(new_uFile.read(), format='xlsx')
            elif new_uFile.name.endswith('.csv'):
                imported_data = csv.reader(new_uFile)
                next(imported_data)
        except Exception as e:
            messages.error(request, f'Error reading file: {e}.')
            return render(request, 'upload.html')
        
        for row in imported_data:
            try:
                date = datetime.strptime(row[0], '%d-%m-%Y').date()
            except ValueError:
                messages.error(request, f'Error parsing date for row: {row}. Skipping this row.')
                continue
            
            value = uFile(
                date=date,
                accno=row[1],
                custState=row[2],
                custPin=row[3],
                dpd=row[4],
            )
            try:
                value.save()
            except Exception as e:
                messages.error(request, f'Error saving data: {e}.')
        
        messages.success(request, 'File uploaded successfully.')
    
    return render(request, 'upload.html')
