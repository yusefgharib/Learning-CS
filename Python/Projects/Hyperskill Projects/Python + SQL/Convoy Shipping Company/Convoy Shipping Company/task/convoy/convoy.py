import sqlite3, csv, json, dicttoxml, pandas as pd
from xml.dom.minidom import parseString

def convert_to_csv():
    global file_name
    my_df = pd.read_excel(file_name, sheet_name="Vehicles", dtype=str)
    file_name = file_name.replace(".xlsx", ".csv")
    my_df.to_csv(file_name, index=False)
    print(my_df.shape[0], 'line was' if my_df.shape[0] == 1 else 'lines were', 'imported to', file_name)

def clean_csv(fn=None):
    global file_name, rows, edited
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if not all(char.isdigit() for char in rows[i][j]):
                edited += 1
                rows[i][j] = "".join(filter(str.isdigit, rows[i][j]))
    file_name = file_name[0:-4] + '[CHECKED].csv'
    print(edited, 'cell was' if edited == 1 else 'cells were', 'corrected in', file_name)
    with open(file_name, "w", encoding='utf-8') as f:
        file_writer = csv.writer(f, delimiter=",", lineterminator="\n")
        file_writer.writerow(headers)
        for row in rows:
            file_writer.writerow(row)

def convert_to_sqlite():
    global file_name, rows
    headers.append('score')
    sq_dtypes = headers[:]
    csv_file_name, file_name = file_name[:], file_name.replace('[CHECKED].csv', '.s3db')
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    for i in range(len(headers)):
        sq_dtypes[i] += " INTEGER PRIMARY KEY" if sq_dtypes[i] == "vehicle_id" else " INTEGER NOT NULL"
    cursor.execute(f"CREATE TABLE convoy ({','.join(sq_dtypes)});")
    for row in add_scores(rows):
        cursor.execute(f"INSERT INTO convoy {tuple(headers)} VALUES {tuple(row)};")
    conn.commit()
    conn.close()
    print(len(rows), 'record was' if len(rows) == 1 else 'records were', 'inserted into', file_name)

def add_scores(rows):
    for i, row in enumerate(rows):
        fuel_consumed = 450 / 100 * float(row[2])
        stops, score = (fuel_consumed / float(row[1])), 0
        score += 2 if stops < 1 else 1 if 2 > stops >= 1 else 0
        score += 2 if fuel_consumed <= 230 else 1
        score += 2 if float(row[3]) >= 20 else 0
        rows[i].append(str(score))
    return rows

def convert_to_json_xml():
    js_file_name, xml_file_name = file_name.replace('.s3db', '.json'), file_name.replace('.s3db', '.xml')
    json_dict, xml_dict = {'convoy': []}, {'convoy': []}
    for i in range(len(rows)):
        if int(rows[i][-1]) > 3:
            json_dict['convoy'].append({headers[j]: rows[i][j] for j in range(len(rows[i]) - 1)})
        else:
            xml_dict['convoy'].append({headers[j]: rows[i][j] for j in range(len(rows[i]) - 1)})

    with open(js_file_name, 'w') as f:
        json.dump(json_dict, f)
    print(len(json_dict['convoy']), 'vehicle was' if len(json_dict['convoy']) == 1 else 'vehicles were', 'saved into', js_file_name)

    item_func = lambda x: 'vehicle'
    xml = dicttoxml.dicttoxml(xml_dict, root=False, attr_type=False, item_func=item_func)
    xml_format = parseString(xml).toprettyxml().replace('<?xml version="1.0" ?>', '')
    with open(xml_file_name, 'w') as f:
        f.write("<convoy></convoy>" if len(xml_dict['convoy']) == 0 else xml_format)
    print(len(xml_dict['convoy']), 'vehicle was' if len(xml_dict['convoy']) == 1 else 'vehicles were', 'saved into', xml_file_name)

file_name = input("Input file name\n")
if file_name.endswith(".xlsx"):
    convert_to_csv()
if file_name.endswith('.csv'):
    with open(file_name) as file:
        file_reader = csv.reader(file, delimiter=",")
        rows = [line for line in file_reader]
        headers, rows, edited = rows[0], rows[1:], 0
    if '[CHECKED]' not in file_name:
        clean_csv()
    convert_to_sqlite()
if file_name.endswith('.s3db'):
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
    rows, headers = [row for row in cursor.execute('SELECT * FROM convoy;')], [i[0] for i in cursor.description]
    conn.close()
convert_to_json_xml()
