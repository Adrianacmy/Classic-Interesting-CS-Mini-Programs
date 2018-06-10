import datetime
import csv
import shutil
from tempfile import NamedTemporaryFile


def get_length(file_path):
  with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    reader_list = list(reader)
    return len(reader_list)


def append_data(file_path, name, email):
  fieldnames = ['id', 'name', 'email']
  next_id = get_length(file_path)
  with open(file_path, 'a') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      # writer.writeheader()
      writer.writerow({
          'id': next_id,
          'name': name,
          'email': email,
      })


append_data('data.csv', 'Adriana', 'iamadrianachen@gmail.com')


def edit_data(edit_id=None, email=None, amount=None, sent=None):
  filename = "data.csv"
  temp_file = NamedTemporaryFile(delete=False)

  with open(filename, "rb") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        # print(row['id'] == 4)
        if edit_id is not None:
            if int(row['id']) == int(edit_id):
                row['amount'] = amount
                row['sent'] = sent
        elif email is not None and edit_id is None:
            if str(row['email']) == str(email):
                row['amount'] = amount
                row['sent'] = sent
        else:
            pass
        writer.writerow(row)

    shutil.move(temp_file.name, filename)
    return True


return False


edit_data(email=edit_data(email='adriana@mail.com', amount=99.99, sent='')


