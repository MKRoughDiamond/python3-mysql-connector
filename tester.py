import argparse
from MySQLConnector import MySQLConnector

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-host', type=str,help='host ip/domain')
    parser.add_argument('-id', type=str, help='id')
    parser.add_argument('-db', type=str, help='Database name')
    
    args = parser.parse_args()

    conn = MySQLConnector(args.host, args.id, args.db)
    
    while True:
        print("====================================================================")
        print("q : query, qs : query with string, gs : get settings, p : print history, c : clear history")
        print("gh : get history, ghd : get history dict, ec : export csv, ep : export pickle, quit : quit")
        a = input("opcode > ")
        print("--------------------------------------------------------------------")
        if a == "gs":
            print(conn.get_settings())
        elif a == "q":
            conn.query()
        elif a == "qs":
            conn.query_with_string(None)
        elif a == "p":
            conn.print_history()
        elif a == "c":
            conn.clear_history()
            conn.print_history()
        elif a == "gh":
            print(conn.get_history())
        elif a == "ghd":
            print(conn.get_history_dict())
        elif a == "ec":
            conn.export_csv()
        elif a == "ep":
            conn.export_pickle()
        elif a == "quit":
            break
        else:
            print("opcode error")
