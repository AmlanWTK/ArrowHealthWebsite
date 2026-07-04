import sys

with open(r'd:\carehub\arrow_health_website\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

app_mockup_lines = lines[3201:3378]

start_doc = -1
end_doc = -1
for i, line in enumerate(lines):
    if '<div class=\"doctor-showcase\">' in line and i > 2600 and i < 2700:
        start_doc = i
    if start_doc != -1 and i > start_doc and '<div class=\"booking-button\">Book from app</div>' in line:
        end_doc = i + 2
        break

if start_doc != -1 and end_doc != -1:
    new_lines = lines[:start_doc] + app_mockup_lines + lines[end_doc+1:]
    with open(r'd:\carehub\arrow_health_website\index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f'Successfully replaced doctor-showcase ({start_doc}-{end_doc}) with app-mockup-wrapper ({len(app_mockup_lines)} lines).')
else:
    print('Failed to find doctor-showcase.')
