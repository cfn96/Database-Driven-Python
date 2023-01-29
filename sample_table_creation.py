import dictionary as dct

glo_connectionstring = "{"

cardholder = dct.File(file_type="odbc",
                      full_path_name="cardholder",
                      owner_name=glo_connectionstring,
                      accountno="x"*8,
                      lastname="x"*25,
                      firstname="x"*25,
                      middlename="x"*25,
                      suffix="x"*6)
