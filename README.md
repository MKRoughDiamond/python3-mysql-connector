## python3-mysql-connector
- mysql connector with history

### prerequisites
- PyMySQL
- Python3

### Class MySQLConnector

#### Variables
- host : host ip/domains
- id : user id
- db : db to use
- cursor_type : cursor type in PyMySQL

#### Method
- get_settings/set_settings : getter, setter of variables
- query
  1. get password
  2. get query string
  3. get results and put it into history
  4. print history
- query_with_string
  1. get password
  2. get results(with given string) and put it into history
  3. print history
- clear_history : reset history to `[]`
- get_history : return copy of history, `List(Dict)`
- get_history_dict : return copy of history, `Dict(List)`
- export_csv, export_pickle : export history to given filename
