from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import sqlite3

# Create your views here.
def index(request):
    return render(request, "FirstApp/index.html")

def display_data_from_db(request,category):
    # Connect to the SQLite database
    connection = sqlite3.connect('player.db')
    cursor = connection.cursor()

    valid_categories = ['ms', 'ws', 'md', 'wd', 'xd']  # List of allowed categories
    if category not in valid_categories:
        pass

    # Query the database to fetch specific columns
     # Query the database to fetch specific columns from the dynamic table
    if category in ['ms', 'ws']:
        query = f'SELECT rank, name, member_id, point, tournament, country FROM {category}'
    if category in ['md', 'wd', 'xd']:
        query = f'SELECT rank, name1, name2, member1_id, member2_id, point, tournament, country FROM {category}'
        
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()

    # Create a list to store all the rows
    data = []

    # Populate the list with data from the database
    if category in ['ms', 'ws']:
        for row in rows:
            data.append({
                'rank': row[0],
                'name': row[1],
                'member_id': row[2],
                'point': row[3],
                'tournament': row[4],
                'country': row[5],
            })
    if category in ['md', 'wd', 'xd']:
        for row in rows:
            data.append({
                'rank': row[0],
                'name': row[1] + '   |   ' + row[2],
                # 'name2': row[1] + ' | ' + row[2],
                'member_id': str(row[3]) + '   |   ' +  str(row[4]),
                # 'member2_id': row[3] + ' | ' + row[4],
                'point': row[5],
                'tournament': row[6],
                'country': row[7],
            })

    # Close the database connection
    connection.close()

    # Pass the data to the template
    return render(request, 'index.html', {'data': data})