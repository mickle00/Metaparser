import xmltodict

def get_parsed(file_path):
    return xmltodict.parse(open(file_path).read())

def print_list_views(parsed):
    for view in parsed['CustomObject']['listViews']:
        print view['fullName']
        for column in view.get('columns', []):
            print '\t' + column

def print_fields(parsed):
    for field in parsed['CustomObject']['fields']:
        print field['fullName'] + ' - ' + field.get('label', field['fullName'])

def print_fields_html(parsed):
    print '<html><table>'
    for field in parsed['CustomObject']['fields']:
        print '<tr><td>' + field['fullName'] + '</td><td>' + field.get('label', field['fullName']) + '</td></tr>'
    print '</table></html>'

doc = get_parsed('examples/Case.object')
print_fields_html(doc)
# print_list_views(doc)
# print_fields(doc)
