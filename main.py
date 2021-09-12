import schoolopy
import yaml
import webbrowser as wb

with open('config.yml', 'r') as f:
    cfg = yaml.safe_load(f)


DOMAIN = 'https://srvusd.schoology.com'

auth = schoolopy.Auth(cfg['key'], cfg['secret'], three_legged=True, domain=DOMAIN)

url = auth.request_authorization()


if url is not None:
    wb.open(url, new=2)

input('Press enter when accepted')


if not auth.authorize():
  raise SystemExit('Account was not authorized.')

sc = schoolopy.Schoology(auth)

userId = sc.get_me().uid

print('Your name is %s' % sc.get_me().name_display)



classes = []



sc.get_section

# GET GRADES
grades = sc.get_user_grades(user_id=userId)

for classByGrade in grades:
  appendList = []
  appendList.append(classByGrade['section_id'])
  appendList.append(sc.get_section(section_id=classByGrade['section_id'])["course_title"])
  for section in classByGrade['final_grade']:
    if section['period_id'] == 'final':  
      appendList.append(section['grade'])

  classes.append(appendList)
  






print("Grades:")
for course in classes:
  print("---------------------------")
  print(course[1] + ": " + str(course[2]) + "%")


    