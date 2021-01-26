
def download_survey():
    import os
    import shutil
    import zipfile
    import requests

    request = requests.get(
        "https://drive.google.com/file/d/1dfGerWeWkcyQ9GX9x20rdSGj7WtEpzBB/view?usp=sharing")
    with open("survey2020.zip", "wb") as file:
        file.write(request.content)

    with zipfile.ZipFile('survey2020.zip') as zip:
        zip.extractall('survey2020')

    shutil.move('survey2020/survey_results_public.csv', 'mysurvey.csv')
    shutil.rmtree('survey2020')
    os.remove('survey2020.zip')


download_survey()

# TODO September 26, 2020: refactor code!
